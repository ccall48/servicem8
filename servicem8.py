#!/usr/bin/python3
""" Usage:
client = ServiceM8("john@example.com", "secretpassword")
client.job()
client.job(2339) or client.job("2339")
    - String searches need to be entered in single or double quotes.

print(client.job())
print(client.job(2339)) or print(client.job("2339"))
"""
import functools

import requests

url = { "assets":"https://api.servicem8.com/api_1.0/asset",
        "assettype":"https://api.servicem8.com/api_1.0/assettype",
        "assettypefield":"https://api.servicem8.com/api_1.0/assettypefield",
        "attachment":"https://api.servicem8.com/api_1.0/attachment",
        "badge":"https://api.servicem8.com/api_1.0/badge",
        "category":"https://api.servicem8.com/api_1.0/category",
        "company":"https://api.servicem8.com/api_1.0/company",
        "companycontact":"https://api.servicem8.com/api_1.0/companycontact",
        "emailtemplate":"https://api.servicem8.com/api_1.0/emailtemplate",
        "feedback":"https://api.servicem8.com/api_1.0/feedback",
        "form":"https://api.servicem8.com/api_1.0/form",
        "formfield":"https://api.servicem8.com/api_1.0/formfield",
        "formresponse":"https://api.servicem8.com/api_1.0/formresponse",
        "job":"https://api.servicem8.com/api_1.0/job",
        "jobactivity":"https://api.servicem8.com/api_1.0/jobactivity",
        "joballocation":"https://api.servicem8.com/api_1.0/joballocation",
        "jobcontact":"https://api.servicem8.com/api_1.0/jobcontact",
        "jobmaterial":"https://api.servicem8.com/api_1.0/jobmaterial",
        "jobpayment":"https://api.servicem8.com/api_1.0/jobpayment",
        "knowledgearticle":"https://api.servicem8.com/api_1.0/knowledgearticle",
        "location":"https://api.servicem8.com/api_1.0/location",
        "material":"https://api.servicem8.com/api_1.0/material",
        "note":"https://api.servicem8.com/api_1.0/note",
        "queue":"https://api.servicem8.com/api_1.0/queue",
        "securityrole":"https://api.servicem8.com/api_1.0/securityrole",
        "smstemplate":"https://api.servicem8.com/api_1.0/smstemplate",
        "staff":"https://api.servicem8.com/api_1.0/staff",
        "staffmessage":"https://api.servicem8.com/api_1.0/staffmessage.",
        "task":"https://api.servicem8.com/api_1.0/task",
        "taxrate":"https://api.servicem8.com/api_1.0/taxrate",
        "vendor":"https://api.servicem8.com/api_1.0/vendor",
        "webhooksubscriptions": "https://api.servicem8.com/webhook_subscriptions"}

class Response:
    """
    Potential gotcha's:
      - any attribute in this class not starting with '_' is considered an api field, any attribute this class has
        should be considered "private"
    """
    def __init__(self, client, data, endpoint):
        self._client = client
        self._raw = data
        self._endpoint = endpoint
        self._changes = {}
        self.__dict__.update(data)

    def __str__(self):
        return (f"{self.name}: {self.uuid}")

    def __getattr__(self, item):
        """
        called only when attribute is not present in the object
        Override default behaviour to get Objects associated with the uuid stored in the current object.

        eg.
        client.job(834).company
        will return a Response() Object representing the company with the uuid of the company_uuid in the job Response()
        """
        var = f"{item}_uuid"
        uuid = self._raw.get(f"{item}_uuid")
        if uuid is None:
            return self._client.__getattribute__(item.replace('_', ''))(Filter('job_uuid', Filter.equal, self.uuid))
        # if no match, return None
        if uuid == '':
            return None
        if var in self._raw:
            return self._client.__getattribute__(item)(Filter('uuid', Filter.equal, uuid))
        raise AttributeError

    def __getattribute__(self, item):
        """
        intercept __getattribute__ to check _changes for attribute changes
        """
        if item.startswith('_'):
            return super().__getattribute__(item)
        ret = self._changes.get(item)
        if ret is None:
            ret = self._raw.get(item)
            if ret is None:
                return super().__getattribute__(item)
        return ret

    def __setattr__(self, key, value):
        """
        intercepts __setattr__ to cache changes in _changes
        """
        if key.startswith('_'):
            super().__setattr__(key, value)
            return
        self._changes.update({key: value})
        return

    def update(self):
        """
        sync _changes to serviceM8
        """
        if self._client._make_post_request(f"{self._endpoint}/{self.uuid}.json", payload=self._changes):
            self._raw.update(self._changes)
            self._changes = dict()
            return True
        return None


class Job(Response):

    def __str__(self):
        return (f"{self.generated_job_id}: {self.job_address.replace('\n', ' ')}")
    @property
    def attachment(self):
        return self._client.attachment(filters=Filter('related_object_uuid', Filter.equal, self.uuid))


class Filter:
    equal = 'eq'
    not_equal = 'ne'
    greater_then = 'gt'
    less_then = 'lt'

    def __init__(self, field, condition, variable):
        self.field = field
        self.condition = condition
        self.variable = variable

    def __str__(self):
        return f"filter={self.field}%20{self.condition}%20'{self.variable}'"


class ServiceM8:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def _make_post_request(self, endpoint, payload):
        headers = {"accept": "application/json", "content-type": "application/json"}
        response = requests.post(endpoint, json=payload, headers=headers, auth=(self.username, self.password))
        if response.status_code == 200:
            return response
        return None

    def _make_get_request(self, endpoint, filters=None, return_class=Response, allow_singular=True):
        if filters is not None:
            urls = f"{endpoint}.json?%24{filters}"
        else:
            urls = f"{endpoint}.json"
        response = requests.get(urls, auth=(self.username, self.password))
        if response.status_code == 200:
            response = response.json()
            if len(response) == 0:
                return None
            elif len(response) == 1 and allow_singular:
                return return_class(self, response[0], endpoint)
            else:
                return [return_class(self, res, endpoint) for res in response]

    @staticmethod
    def sm8_endpoint(f):
        @functools.wraps(f)
        def requested(self, *args, **kwargs):
            return f(self, url[f.__name__], *args, **kwargs)
        return requested


    @sm8_endpoint
    def assets(self, endpoint, filters=None):
        return self._make_get_request(endpoint, filters)

    @sm8_endpoint
    def assettype(self, endpoint, filters=None):
        return self._make_get_request(endpoint, filters)

    @sm8_endpoint
    def assettypefield(self, endpoint, filters=None):
        return self._make_get_request(endpoint, filters)

    @sm8_endpoint
    def attachment(self, endpoint, filters=None):
        return self._make_get_request(endpoint, filters)

    @sm8_endpoint
    def badge(self, endpoint, filters=None):
        return self._make_get_request(endpoint, filters)

    @sm8_endpoint
    def category(self, endpoint, filters=None):
        return self._make_get_request(endpoint, filters)

    @sm8_endpoint
    def company(self, endpoint, filters=None):
        return self._make_get_request(endpoint, filters)

    @sm8_endpoint
    def companycontact(self, endpoint, filters=None):
        return self._make_get_request(endpoint, filters)

    @sm8_endpoint
    def emailtemplate(self, endpoint, filters=None):
        return self._make_get_request(endpoint, filters)

    @sm8_endpoint
    def feedback(self, endpoint, filters=None):
        return self._make_get_request(endpoint, filters)

    @sm8_endpoint
    def form(self, endpoint, filters=None):
        return self._make_get_request(endpoint, filters)

    @sm8_endpoint
    def formfield(self, endpoint, filters=None):
        return self._make_get_request(endpoint, filters)

    @sm8_endpoint
    def formresponse(self, endpoint, filters=None):
        return self._make_get_request(endpoint, filters)

    @sm8_endpoint
    def job(self, endpoint, filters=None):
        if type(filters) == int:
            filters = Filter('generated_job_id', Filter.equal, filters)
        return self._make_get_request(endpoint, filters, return_class=Job)

    @sm8_endpoint
    def jobactivity(self, endpoint, filters=None):
        return self._make_get_request(endpoint, filters, allow_singular=False)

    @sm8_endpoint
    def joballocation(self, endpoint, filters=None):
        return self._make_get_request(endpoint, filters)

    @sm8_endpoint
    def jobcontact(self, endpoint, filters=None):
        return self._make_get_request(endpoint, filters)

    @sm8_endpoint
    def jobmaterial(self, endpoint, filters=None):
        return self._make_get_request(endpoint, filters)

    @sm8_endpoint
    def jobpayment(self, endpoint, filters=None):
        return self._make_get_request(endpoint, filters)

    @sm8_endpoint
    def knowledgearticle(self, endpoint, filters=None):
        return self._make_get_request(endpoint, filters)

    @sm8_endpoint
    def location(self, endpoint, filters=None):
        return self._make_get_request(endpoint, filters)

    @sm8_endpoint
    def material(self, endpoint, filters=None):
        return self._make_get_request(endpoint, filters)

    @sm8_endpoint
    def note(self, endpoint, filters=None):
        return self._make_get_request(endpoint, filters)

    @sm8_endpoint
    def queue(self, endpoint, filters=None):
        return self._make_get_request(endpoint, filters)

    @sm8_endpoint
    def securityrole(self, endpoint, filters=None):
        return self._make_get_request(endpoint, filters)

    @sm8_endpoint
    def smstemplate(self, endpoint, filters=None):
        return self._make_get_request(endpoint, filters)

    @sm8_endpoint
    def staff(self, endpoint, filters=None):
        return self._make_get_request(endpoint, filters)

    @sm8_endpoint
    def staffmessage(self, endpoint, filters=None):
        return self._make_get_request(endpoint, filters)

    @sm8_endpoint
    def task(self, endpoint, filters=None):
        return self._make_get_request(endpoint, filters)

    @sm8_endpoint
    def taxrate(self, endpoint, filters=None):
        return self._make_get_request(endpoint, filters)

    @sm8_endpoint
    def vendor(self, endpoint, filters=None):
        return self._make_get_request(endpoint, filters)

    @sm8_endpoint
    def webhooksubscriptions(self, endpoint):
        return self._make_get_request(endpoint)

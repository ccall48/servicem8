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
import pprint

import requests
import json

url = { "assets":"https://api.servicem8.com/api_1.0/asset.json",
        "assettype":"https://api.servicem8.com/api_1.0/assettype.json",
        "assettypefield":"https://api.servicem8.com/api_1.0/assettypefield.json",
        "attachment":"https://api.servicem8.com/api_1.0/attachment.json",
        "badge":"https://api.servicem8.com/api_1.0/badge.json",
        "category":"https://api.servicem8.com/api_1.0/category.json",
        "company":"https://api.servicem8.com/api_1.0/company.json",
        "companycontact":"https://api.servicem8.com/api_1.0/companycontact.json",
        "emailtemplate":"https://api.servicem8.com/api_1.0/emailtemplate.json",
        "feedback":"https://api.servicem8.com/api_1.0/feedback.json",
        "form":"https://api.servicem8.com/api_1.0/form.json",
        "formfield":"https://api.servicem8.com/api_1.0/formfield.json",
        "formresponse":"https://api.servicem8.com/api_1.0/formresponse.json",
        "job":"https://api.servicem8.com/api_1.0/job.json",
        "jobactivity":"https://api.servicem8.com/api_1.0/jobactivity.json",
        "joballocation":"https://api.servicem8.com/api_1.0/joballocation.json",
        "jobcontact":"https://api.servicem8.com/api_1.0/jobcontact.json",
        "jobmaterial":"https://api.servicem8.com/api_1.0/jobmaterial.json",
        "jobpayment":"https://api.servicem8.com/api_1.0/jobpayment.json",
        "knowledgearticle":"https://api.servicem8.com/api_1.0/knowledgearticle.json",
        "location":"https://api.servicem8.com/api_1.0/location.json",
        "material":"https://api.servicem8.com/api_1.0/material.json",
        "note":"https://api.servicem8.com/api_1.0/note.json",
        "queue":"https://api.servicem8.com/api_1.0/queue.json",
        "securityrole":"https://api.servicem8.com/api_1.0/securityrole.json",
        "smstemplate":"https://api.servicem8.com/api_1.0/smstemplate.json",
        "staff":"https://api.servicem8.com/api_1.0/staff.json",
        "staffmessage":"https://api.servicem8.com/api_1.0/staffmessage.json",
        "task":"https://api.servicem8.com/api_1.0/task.json",
        "taxrate":"https://api.servicem8.com/api_1.0/taxrate.json",
        "webhooksubscriptions":"https://api.servicem8.com/webhook_subscriptions",
        "vendor":"https://api.servicem8.com/api_1.0/vendor.json"}


class Response:
    def __init__(self, client, data):
        self._client = client
        self._raw = data
        self.__dict__.update(data)


    def __getattr__(self, item):
        var = f"{item}_uuid"
        uuid = self._raw.get(f"{item}_uuid")
        if uuid is None:
            return self._client.__getattribute__(item.replace('_', ''))(Filter('job_uuid', Filter.equal, self.uuid))
        if uuid == '':
            return None
        if var in self._raw:
            return self._client.__getattribute__(item)(Filter('uuid', Filter.equal, uuid))
        raise AttributeError

class Job(Response):
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

    def _make_request(self, endpoint, filters=None, return_class=Response, allow_singular=True):
        if filters is not None:
            urls = f"{endpoint}?%24{filters}"
        else:
            urls = endpoint
        print(urls)
        response = requests.get(urls, auth=(self.username, self.password))
        if response.status_code == 200:
            response = response.json()
            if len(response) == 0:
                return None
            elif len(response) == 1 and allow_singular:
                return return_class(self, response[0])
            else:
                return [return_class(self, res) for res in response]

    @staticmethod
    def sm8_endpoint(f):
        @functools.wraps(f)
        def requested(self, *args, **kwargs):
            return f(self, url[f.__name__], *args, **kwargs)
        return requested


    @sm8_endpoint
    def assets(self, endpoint, filters=None):
        return self._make_request(endpoint, filters)

    @sm8_endpoint
    def assettype(self, endpoint, filters=None):
        return self._make_request(endpoint, filters)

    @sm8_endpoint
    def assettypefield(self, endpoint, filters=None):
        return self._make_request(endpoint, filters)

    @sm8_endpoint
    def attachment(self, endpoint, filters=None):
        return self._make_request(endpoint, filters)

    @sm8_endpoint
    def badge(self, endpoint, filters=None):
        return self._make_request(endpoint, filters)

    @sm8_endpoint
    def category(self, endpoint, filters=None):
        return self._make_request(endpoint, filters)

    @sm8_endpoint
    def company(self, endpoint, filters=None):
        return self._make_request(endpoint, filters)

    @sm8_endpoint
    def companycontact(self, endpoint, filters=None):
        return self._make_request(endpoint, filters)

    @sm8_endpoint
    def emailtemplate(self, endpoint, filters=None):
        return self._make_request(endpoint, filters)

    @sm8_endpoint
    def feedback(self, endpoint, filters=None):
        return self._make_request(endpoint, filters)

    @sm8_endpoint
    def form(self, endpoint, filters=None):
        return self._make_request(endpoint, filters)

    @sm8_endpoint
    def formfield(self, endpoint, filters=None):
        return self._make_request(endpoint, filters)

    @sm8_endpoint
    def formresponse(self, endpoint, filters=None):
        return self._make_request(endpoint, filters)

    @sm8_endpoint
    def job(self, endpoint, filters=None):
        if type(filters) == int:
            filters = Filter('generated_job_id', Filter.equal, filters)
        return self._make_request(endpoint, filters, return_class=Job)

    @sm8_endpoint
    def jobactivity(self, endpoint, filters=None):
        return self._make_request(endpoint, filters, allow_singular=False)

    @sm8_endpoint
    def joballocation(self, endpoint, filters=None):
        return self._make_request(endpoint, filters)

    @sm8_endpoint
    def jobcontact(self, endpoint, filters=None):
        return self._make_request(endpoint, filters)

    @sm8_endpoint
    def jobmaterial(self, endpoint, filters=None):
        return self._make_request(endpoint, filters)

    @sm8_endpoint
    def jobpayment(self, endpoint, filters=None):
        return self._make_request(endpoint, filters)

    @sm8_endpoint
    def knowledgearticle(self, endpoint, filters=None):
        return self._make_request(endpoint, filters)

    @sm8_endpoint
    def location(self, endpoint, filters=None):
        return self._make_request(endpoint, filters)

    @sm8_endpoint
    def material(self, endpoint, filters=None):
        return self._make_request(endpoint, filters)

    @sm8_endpoint
    def note(self, endpoint, filters=None):
        return self._make_request(endpoint, filters)

    @sm8_endpoint
    def queue(self, endpoint, filters=None):
        return self._make_request(endpoint, filters)

    @sm8_endpoint
    def securityrole(self, endpoint, filters=None):
        return self._make_request(endpoint, filters)

    @sm8_endpoint
    def smstemplate(self, endpoint, filters=None):
        return self._make_request(endpoint, filters)

    @sm8_endpoint
    def staff(self, endpoint, filters=None):
        return self._make_request(endpoint, filters)

    @sm8_endpoint
    def staffmessage(self, endpoint, filters=None):
        return self._make_request(endpoint, filters)

    @sm8_endpoint
    def task(self, endpoint, filters=None):
        return self._make_request(endpoint, filters)

    @sm8_endpoint
    def taxrate(self, endpoint, filters=None):
        return self._make_request(endpoint, filters)

    @sm8_endpoint
    def vendor(self, endpoint, filters=None):
        return self._make_request(endpoint, filters)

if __name__ == "__main__":
    with open('creds') as creds:
        credentials = creds.read().split()
    client = ServiceM8(*credentials)
    jobs = client.job()
    print(client.attachment()[0]._raw)
    job = client.job(834)
    print(job._raw)
    print(job.jobactivity[0]._raw)
    for att in job.attachment:
        print(att._raw)

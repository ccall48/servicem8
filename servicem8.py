#!/usr/bin/python3
""" Usage:
client = ServiceM8("john@example.com", "secretpassword")
client.job()
client.job(2339) or client.job("2339")
    - String searches need to be entered in single or double quotes.

print(client.job())
print(client.job(2339)) or print(client.job("2339"))
"""
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
        "vendor":"https://api.servicem8.com/api_1.0/vendor.json"}

class ServiceM8:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def assets(self, asset=None):
        r = requests.get(url['assets'], auth=(self.username, self.password))
        if asset is None:
            return json.dumps(r.json(), indent=2)
        else:
            for i in r.json():
                if i['assets_all'] == str(asset):
                    return json.dumps(i, indent=2)

    def assettype(self):
        r = requests.get(url['assettype'], auth=(self.username, self.password))
        return json.dumps(r.json(), indent=2)

    def assettypefield(self):
        r = requests.get(url['assettypefield'], auth=(self.username, self.password))
        return json.dumps(r.json(), indent=2)

    def attachment(self, attachment=None): #add attachment search?
        r = requests.get(url['attachment'], auth=(self.username, self.password))
        return json.dumps(r.json(), indent=2)

    def badge(self):
        r = requests.get(url['badge'], auth=(self.username, self.password))
        return json.dumps(r.json(), indent=2)

    def category(self):
        r = requests.get(url['category'], auth=(self.username, self.password))
        return json.dumps(r.json(), indent=2)

    def company(self, company=None):
        r = requests.get(url['company'], auth=(self.username, self.password))
        if company is None:
            return json.dumps(r.json(), indent=2)
        else:
            for i in r.json():
                if i['name'] == str(company):
                    return json.dumps(i, indent=2)

    def companycontact(self): #add company contact search?
        r = requests.get(url['companycontact'], auth=(self.username, self.password))
        return json.dumps(r.json(), indent=2)

    def emailtemplate(self):
        r = requests.get(url['emailtemplate'], auth=(self.username, self.password))
        return json.dumps(r.json(), indent=2)

    def feedback(self):
        r = requests.get(url['feedback'], auth=(self.username, self.password))
        return json.dumps(r.json(), indent=2)

    def form(self):
        r = requests.get(url['form'], auth=(self.username, self.password))
        return json.dumps(r.json(), indent=2)

    def formfield(self):
        r = requests.get(url['formfield'], auth=(self.username, self.password))
        return json.dumps(r.json(), indent=2)

    def formresponse(self):
        r = requests.get(url['formresponse'], auth=(self.username, self.password))
        return json.dumps(r.json(), indent=2)

    def job(self, job=None):
        r = requests.get(url['job'], auth=(self.username, self.password))
        if job is None:
            return json.dumps(r.json(), indent=2)
        else:
            for i in r.json():
                if i['generated_job_id'] == str(job):
                    return json.dumps(i, indent=2)

    def jobactivity(self):
        r = requests.get(url['jobactivity'], auth=(self.username, self.password))
        return json.dumps(r.json(), indent=2)

    def joballocation(self):
        r = requests.get(url['joballocation'], auth=(self.username, self.password))
        return json.dumps(r.json(), indent=2)

    def jobcontact(self): #add job contact search
        r = requests.get(url['jobcontact'], auth=(self.username, self.password))
        return json.dumps(r.json(), indent=2)

    def jobmaterial(self): #add job material search?
        r = requests.get(url['jobmaterial'], auth=(self.username, self.password))
        return json.dumps(r.json(), indent=2)

    def jobpayment(self, jobpayment=None): #add search job payment?
        r = requests.get(url['jobpayment'], auth=(self.username, self.password))
        return json.dumps(r.json(), indent=2)

    def knowledgearticle(self):
        r = requests.get(url['knowledgearticle'], auth=(self.username, self.password))
        return json.dumps(r.json(), indent=2)

    def location(self):
        r = requests.get(url['location'], auth=(self.username, self.password))
        return json.dumps(r.json(), indent=2)

    def material(self, material=None): # add lookup material
        r = requests.get(url['material'], auth=(self.username, self.password))
        return json.dumps(r.json(), indent=2)

    def note(self):
        r = requests.get(url['note'], auth=(self.username, self.password))
        return json.dumps(r.json(), indent=2)

    def queue(self):
        r = requests.get(url['queue'], auth=(self.username, self.password))
        return json.dumps(r.json(), indent=2)

    def securityrole(self):
        r = requests.get(url['securityrole'], auth=(self.username, self.password))
        return json.dumps(r.json(), indent=2)

    def smstemplate(self):
        r = requests.get(url['smstemplate'], auth=(self.username, self.password))
        return json.dumps(r.json(), indent=2)

    def staff(self):
        r = requests.get(url['staff'], auth=(self.username, self.password))
        return json.dumps(r.json(), indent=2)

    def staffmessage(self):
        r = requests.get(url['staffmessage'], auth=(self.username, self.password))
        return json.dumps(r.json(), indent=2)

    def task(self):
        r = requests.get(url['task'], auth=(self.username, self.password))
        return json.dumps(r.json(), indent=2)

    def taxrate(self):
        r = requests.get(url['taxrate'], auth=(self.username, self.password))
        return json.dumps(r.json(), indent=2)

    def vendor(self):
        r = requests.get(url['vendor'], auth=(self.username, self.password))
        return json.dumps(r.json(), indent=2)

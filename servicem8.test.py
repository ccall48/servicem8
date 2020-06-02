#!/usr/bin/python3
import requests
import json

USER = "john@email.com" # <- servicem8 email
PASS = "secretpassword" # <- servicem8 password

url = "https://api.servicem8.com/api_1.0/"
ext = {"assets_all":"assettype.json", "assets_type":"assettype/uuid.json", "note":"note.json",
       "job":"job.json", "job_contacts":"jobcontact.json", "payments":"jobpayment.json", "queue":"queue.json",
       "client":"company.json", "material":"material.json", "scheduled":"jobactivity.json", "vendor":"vendor.json",
       "roles":"securityrole.json", "sms_temp":"smstemplate.json", "tasks":"task.json"
       }

"""
To run script, from directory use:
from servicem8 import ServiceM8

dependencies are requests & json.
"""

class ServiceM8():
    """
    ServiceM8.jobs()
        -   print(ServiceM8.jobs()) Prints an indented json list of all jobs.

    ServiceM8.job_search(<job>)
        -   print(ServiceM8.job_search(<job>)) Prints an indented json list of a job.
        -   Where <job> is an integer or string of a job id eg. ServiceM8.searchjobs(2346) or
            ServiceM8.searchjobs(2346) are both valid search criteria.
        -   Prints result if job exists, or returns nothing.

    ServiceM8.job_payments()
        -   print(ServiceM8.job_payments()) Prints an indented json list of all payments.
    """
    def jobs():
        r = requests.get(url + ext['job'], auth=(USER, PASS))
        return json.dumps(r.json(), indent=2)

    def job_search(job_id):
        r = requests.get(url + ext['job'], auth=(USER, PASS))
        for i in r.json():
            if i['generated_job_id'] == str(job_id):
                return json.dumps(i, indent=2)

    def job_payments():
        r = requests.get(url + ext['payments'], auth=(USER, PASS))
        return json.dumps(r.json(), indent=2)

    """
    ServiceM8.company()
        -   print(ServiceM8.company()) Returns an indented json list of all clients/companies.

    ServiceM8.company_search("<client name>")
        -   print(ServiceM8.company_search()) Returns an indented json list of a client/company.
        -   Where <client name> is string of a client/company name id eg.
            ServiceM8.searchjobs("Doe, John") is a valid search criteria.
        -   Prints result if job exists, or returns nothing.

    """
    def company():
        r = requests.get(url + ext['client'], auth=(USER, PASS))
        return json.dumps(r.json(), indent=2)

    def company_search(search):
        r = requests.get(url + ext['client'], auth=(USER, PASS))
        for i in r.json():
            if i['name'] == str(search):
                return json.dumps(i, indent=2)

    """
    ServiceM8.material()
        -   Prints an indented json list of all materials.

    ServiceM8.material_search("<material>")
        -   Where <material> is an integer or string of a material item number eg.
            -   ServiceM8.searchmaterial(198234) or ServiceM8.searchmaterial("198234")
                or
                ServiceM8.searchmaterial(Pipe Clamp) or ServiceM8.searchmaterial("Pipe Clamp")
                should all be valid search criterias.

        -   print(ServiceM8.material_search("<material>")) Prints result if material exists, or returns nothing.
    """
    def material():
        r = requests.get(url + ext['material'], auth=(USER, PASS))
        return json.dumps(r.json(), indent=2)

    def material_search(item_id):
        r = requests.get(url + ext['material'], auth=(USER, PASS))
        for i in r.json():
            if i['item_number'] == str(item_id):
                return json.dumps(i, indent=2)

    """
    ServiceM8.scheduled()
        -   print(ServiceM8.scheduled()) Prints an indented json list of all scheduled jobs.

    """
    def scheduled():
        r = requests.get(url + ext['scheduled'], auth=(USER, PASS))
        return json.dumps(r.json(), indent=2)

    """
    ServiceM8.assets_all()
        -   print(ServiceM8.assets_all()) Prints an indented json list of all recorded assets

    ServiceM8.asset_type()
        -  print(ServiceM8.asset_type()) # needs uuid for asset?
    """
    def assets_all():
        r = requests.get(url + ext['assets_all'], auth=(USER, PASS))
        return json.dumps(r.json(), indent=2)

    #def asset_type():
    #    r = requests.get(url + ext['assets_type'], auth=(USER, PASS))
    #    print(json.dumps(r.json(), indent=2))

    """
    ServiceM8.job_contacts()
        -   print(ServiceM8.job_contacts()) Prints an indented json list of all job contacts.

    servicem8.job_contact_search("<first name>", "<last name>")
        - print(servicem8.job_contact_search("<first name>", "<last name>"))
    """
    def job_contacts():
        r = requests.get(url + ext['job_contacts'], auth=(USER, PASS))
        return json.dumps(r.json(), indent=2)

    def job_contact_search(first, last):
        r = requests.get(url + ext['job_contacts'], auth=(USER, PASS))
        for i in r.json():
            if i['first'] == str(first) and i['last'] == str(last):
                return json.dumps(i, indent=2)

    """
    ServiceM8.notes()
        -   print(ServiceM8.notes()) Prints an indented json list of notes.
    """
    def notes():
        r = requests.get(url + ext['note'], auth=(USER, PASS))
        return json.dumps(r.json(), indent=2)

    """
    ServiceM8.queue()
        -   print(ServiceM8.queue()) Prints an indented json list of job queues.
    """
    def queues():
        r = requests.get(url + ext['queue'], auth=(USER, PASS))
        return json.dumps(r.json(), indent=2)

    """
    ServiceM8.sms_templates()
        -   print(ServiceM8.sms_templates()) Prints an indented json list of sms templates.
    """
    def sms_templates():
        r = requests.get(url + ext['sms_temp'], auth=(USER, PASS))
        return json.dumps(r.json(), indent=2)

    """
    ServiceM8.tasks()
        -   print(ServiceM8.tasks()) Prints an indented json list of tasks.
    """
    def tasks():
        r = requests.get(url + ext['tasks'], auth=(USER, PASS))
        return json.dumps(r.json(), indent=2)

    """
    ServiceM8.vendor()
        -   print(ServiceM8.vendor()) Prints an indented json list of vendors details.
    """
    def vendor():
        r = requests.get(url + ext['vendor'], auth=(USER, PASS))
        return json.dumps(r.json(), indent=2)

    """
    ServiceM8.roles()
        -   print(ServiceM8.roles()) Prints an indented json list of user roles.
    """
    def roles():
        r = requests.get(url + ext['roles'], auth=(USER, PASS))
        return json.dumps(r.json(), indent=2)

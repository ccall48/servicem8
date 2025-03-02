# Makes use of ServiceM8 REST API
Python script to make use of ServiceM8 REST API for a private integration.
Will add more endpoints as I get time.

Documentation can be found here: https://developer.servicem8.com/docs

Commits & Pull requests welcome if you want to contribute.

# Usage examples

    from servicem8 import ServiceM8<br>
    client = ServiceM8("john@example.com", "secretpassword")

endpoints can be accessed directly from the client object:

    client.job()
      - returns all jobs as Response objects
    
    client.staff()
      - returns all staff as Response objects

filters work as you would expect

    from servicem8 import Filter
    filter = Filter("active", Filter.equal, 0)
    client.staff(filters=filter)

The only object that supports filtering without a filter object is Job, and only for generated_job_id

    client.job(100)  # returns job #100


Some "Magic" lazy loading has been implemented with uuid fields
    
    job = client.job(100)
    job.category  # will return a Response object representing a category
    job.completion_actioned_by  # will return a Response object representing the staff member
                                  that completed this job

to return the raw json response:

    client.job().json()
      - returns all jobs in indented json format.


# Makes use of ServiceM8 REST API
Python script to make use of ServiceM8 REST API for a private integration.
Will add more endpoints as I get time.

Documentation can be found here: https://developer.servicem8.com/docs

Commits & Pull requests welcome if you want to contribute.

# Usage example
from servicem8 import ServiceM8
client = ServiceM8("john@example.com","secretpassword")

client.job()
>>> returns all jobs unformated json.

print(client.job())
>>> returns all jobs in indented json format.

print(client.job(2155)) or print(client.job("2155"))
>>> returns job 2155 in indented json format, if it exists or None.

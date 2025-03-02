from typing import Union

from servicem8 import ServiceM8, Response

"""
file should have a space seperated file of credentials, although if you playing
with the testing of this repo, im sure this code would have been immediately
readable

eg:

  username password
"""
with open('.creds') as creds:
    creds = creds.read()

def main():
    username, password = creds.split(' ')
    client = ServiceM8(username, password)

    # Check that all UUID fields lazyload into `Response` objects
    job = client.job(110)
    for k in job._raw.keys():
        if k.endswith('_uuid'):
            try:
                obj = job.__getattr__(k.replace('_uuid', ''))
                print(k, obj)
                # this check makes sure that a related object was searched for, None here just means nothing was found
                assert isinstance(obj, Union[Response, None])
            except AssertionError as e:
                print(f'{k} doesnt map to a Response object as it should')
                raise e


if __name__ == '__main__':
    main()
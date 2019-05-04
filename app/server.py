import os
import json
from bottle import get, post, run


depoyment_env = os.environ.get('DEPLOYMENT_ENV')

if depoyment_env == 'PRODUCTION':
    cofiguration_file = 'production.config'
elif depoyment_env == 'STAGING':
    cofiguration_file = 'staging.config'
else:
    raise ValueError('Could not find DEPLOYMENT_ENV environment variable!')

os.chdir(os.path.dirname(__file__))
app_config = json.load(open(cofiguration_file))


@get('/')
def greetings():
    return app_config["greetings"]

@get('/deployment-environment')
def env_var():
    return depoyment_env

@get('/reverse-string/<input>')
def reverse_string(input):
    return input[::-1]

@post('/square/<input:int>')
def square(input):
    return str(input * input)


run(host='0.0.0.0', port=app_config["port"], debug=app_config["debug"])

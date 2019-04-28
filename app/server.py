from bottle import get, post, run

@get('/reverse-string/<input>')
def reverse_string(input):
    return input[::-1]

@post('/square/<input:int>')
def square(input):
    return str(input * input)

run(host='0.0.0.0', port=8081, debug=True)

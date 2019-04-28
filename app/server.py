from bottle import get, post, run

@get('/reverse-string/<input>')
def reverse_string(input):
    return input[::-1]

@post('/square/<input:int>')
def square(input):
    return str(input * input)

run(host='localhost', port=5000, debug=True)

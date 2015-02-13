from bottle import default_app, route, run, template
from generator import issue_maker

@route('/')
def issue_print():

    sent = issue_maker()
    return template('main_temp', sent = str(sent))

application = default_app()
run(host='localhost', port=8080, debug=True)
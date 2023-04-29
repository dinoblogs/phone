from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<html>
<head>
<title>Krishna Website</title>

</head>
<body>
<h1>Testing123...</h1>
</body>

</html>
    '''
app.config['TRAP_HTTP_EXCEPTIONS']=True

@app.errorhandler(Exception)
def handle_error(e):
    try:
        if e.code < 400:
            return flask.Response.force_type(e, flask.request.environ)
        elif e.code == 404:
            return make_error_page("Page Not Found", "The page you're looking for was not found krishna"), 404
        raise e
    except:
        return make_error_page("Error", "Something went wrong lrosjna"), 500
@app.route('/about')
def about():
    return 'About'

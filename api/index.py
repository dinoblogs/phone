from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<html>
<head>
<meta name="a.validate.02" content="IRvV_pLvtxSzYEIrilFKHjdtzFxyP_jyAgZz" />
<title>Krishna Website</title>

</head>
<body>
<h1>Testing123...</h1>
</body>

</html>
    '''

@app.route('/about')
def about():
    return 'About'

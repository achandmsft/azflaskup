'''
# Deploying a Python Flask app on Azure
Go to http://shell.azure.com and run the following (Or run locally using the Azure CLI (http://aka.ms/cli)) -  
# Deploy the app   
    $ git clone https://github.com/achandmsft/azflaskup
    $ cd azflaskup
    $ az webapp up --name <enter a unique name for your app> --location centralus
# Make changes and redeploy the app
    $ code app.py 
    $ az webapp up --name <enter a unique name for your app> --location centralus   
For more on Azure CLI, go to http://aka.ms/cli (az webapp up reference can be found under http://aka.ms/azwebappup)
'''

# Deploy the app using az webapp up, then goto http://<address output by az webapp up> 
from flask import Flask, request
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"

# Deploy the app using az webapp up, then goto http://<address output by az webapp up>/query?country=YourCountry&name=YourName
@app.route('/query')
def query_example():
    location = request.args.get('country')
    name = request.args.get('name')
    return '''<h1>Welcome {} from {}!</h1>'''.format(name, location)

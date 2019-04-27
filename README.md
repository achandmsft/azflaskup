# Deploy a Python Flask app using the [Azure CLI](http://aka.ms/cli) 
Go to http://shell.azure.com and run the commands in the following sections (Or run this locally from Azure CLI (http://aka.ms/cli) and make changes locally using [VSCode](http://aka.ms/vscode) -  
# Deploy the app using [az webapp up](http://aka.ms/azwebappup)  
    $ git clone <TODO> myPythonapp
    $ cd myPythonapp
    $ az webapp up --name myPythonapp --location centralus
# Make changes and redeploy the app
    $ code application.py 
    $ az webapp up --name myPythonapp --location centralus   

# Contributing
This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

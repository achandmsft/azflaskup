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

# Contributing
This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

# Deploying a Python app on Azure
Go to http://shell.azure.com and run the following (Or run locally using the [Azure CLI](http://aka.ms/cli)) -  

# Deploy the app   
The name for your app must be globally unique as it will prefix the website address: http://yourapp.azurewebsites.net/  

    $ git clone https://github.com/achandmsft/azflaskup
    $ cd azflaskup
    $ az webapp up --name <enter a globally unique name for your app> --location centralus

# Make changes and redeploy the app
    $ code app.py 
    $ az webapp up --name <enter a unique name for your app> --location centralus   

For more on Azure CLI, go to http://aka.ms/cli (az webapp up: http://aka.ms/azwebappup)

# Known issue
If you get an exception with the above in shell.azure.com that resource group name is invalid, run az login and complete the instructions clicking on the devicelogin link and pasting the code from the az login output.

# Contributing
This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

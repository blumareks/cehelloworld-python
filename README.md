# cehelloworld-python
CodeEngine hello world application in Python


Code Engine hello world example in python from local source code: https://cloud.ibm.com/docs/codeengine?topic=codeengine-fun-create-local

```
ibmcloud login --sso 
```

select Resource Group: 

```
ibmcloud target -g RESOURCE_GROUP_NAME 
```



create a CE Project `Approval Flow`;  select it 

```
ibmcloud ce project select -n 'Approval Flow'

ibmcloud ce fn create --name pylorem-local --runtime python-3.11 --build-source .
```

details:

```
ibmcloud ce function get -n pylorem-local
```

call the url: 

```
curl https://
```
if you need to update the function later - use update instead of create: 

```
ibmcloud ce fn update --name pylorem-local --runtime python-3.11 --build-source .
```

## dependencies

how to add dependencies: https://cloud.ibm.com/docs/codeengine?topic=codeengine-fun-create-local#fun-package-local

for Python: https://cloud.ibm.com/docs/codeengine?topic=codeengine-fun-create-local#function-python-dep-local


Create your function by saving your code into a `__main__.py` file

create a function that includes a dependency for a specific Python module by creating a requirements.txt file. In this case, both the source code and requirements file are located in the same folder.

Create a requirements.txt containing your required dependencies for your function

Create your files as a function in Code Engine. In this case, you are in the directory where the local files exist so you can use . as the build source.

ibmcloud ce fn create --name pylorem --runtime python-3.11 --build-source .

# Link to Live Application hosted on Microsft Azure

https://hacker-gallery.azurewebsites.net

# Setup Environment and Run App Locally

### Note: Make sure, you have Python 3 installed. (preferebly 3.8)  

1. Open the folder where all files are extracted
2. Now, create and activate virtual environment for python, using below command in windows powershell:
```
> python -m venv venv
> Set-ExecutionPolicy Unrestricted -Scope Process
> venv\scripts\activate
```
Or in Linux/Mac:
```
$ python3 -m venv venv
$ . venv/bin/activate
```
3. Now, install requirements with this command:
```
pip install -r requirements.txt
```
4. Now run the application using below command:
```
flask run
```
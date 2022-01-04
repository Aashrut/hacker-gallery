# Link to Live Application hosted on Microsft Azure

https://hacker-gallery.azurewebsites.net

# Setup Environment and Run App Locally

### Note: Make sure, you have Python 3 installed. (preferebly 3.8)  

1. Download the zip file and unzip it. Open the folder where all files are extracted.
2. Now, open Terminal/Powershell there. Create and activate virtual environment for python, using below commands:  

In Windows Powershell:
```
> python -m venv venv
> Set-ExecutionPolicy Unrestricted -Scope Process
> venv\scripts\activate
```
`Set-ExecutionPolicy` command will give unrestricted aceess to current process, so it will let you run activate script.   

Or In Linux/Mac:
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
After running, You can access this app on http://127.0.0.1:5000

# Features

- Add/Update/Show/Delete Images
- Beautiful, Responsive and User-friendly UI
- Provides flash massages when user perform any actions.
- Uses 4 different HTTP methods, GET, POST, PUT, DELETE
- Simple and easy navigation buttons

# Tech Stack

- Front End
    - HTML
    - CSS (Bootstrap 5)
    - JavaScript
- Back End
    - Flask (Python)
- DataBase
    - Sqlite 3
- Hosting Services
    - Microsoft Azure App Service
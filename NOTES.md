### Opening Notes

-   All code enclosed in {} must be replaced with something else. i.e. `mkdir {project_name}` must be `mkdir hotdog` when your project name is hotdog

# Setting up this project in your local repository

1. Fork the project in GitHub
1. Clone the project
    ```
    git clone {https or ssh link}
    ```
1. Open the project in VS Code
    ```
    code react-django-tutorial
    ```
1. Create a virtual environment with Python and activate the virtual environment
    ```
    python -m venv venv
    . venv/Scripts/activate
    ```
1. Install the necessary Python dependencies
    ```
    pip install -r requirements.txt
    ```

# Starting a React-Django project

1. Make sure that you have everything you need first setup
    - Python
    - Node.js and npm
    - VS Code
1. Make a new folder for your project, create a virtual environment, and activate your virtual environment
    ```
    mkdir {project_name}
    python -m venv venv
    source venv/Scripts/activate
    ```
1. Install the necessary Python dependencies
    ```
    pip install django djangorestframework
    ```
1. Start a project
    ```
    django-admin startproject {project_name}
    cd {project_name}
    django-admin startapp {app_name}
    ```
1. Add your app to `{project_name}/{project_name}/settings.py`
    - Open `{project_name}/{project_name}/settings.py` and look for the `INSTALL_APPS` list.
    - Add there `'{app_name}.apps.ApiConfig'`
        - You can see what to add by browsing the app you just created, opening `apps.py` and seeing the class initialized there. By default, there should be an `ApiConfig` class there.
    - Add `'rest_framework'`

### Just a few notes:

-   Models: Database models
-   Views: API Endpoints
-   `{project_name}/{project_name}` will be referred to as your "Main project folder" and `{project_name}` will be your "Root project folder"

# Creating an endpoint (view)

1. Inside your app folder, open `views.py`
1. The following line of code will be a sample for making an API endpoint

    ```
    from django.shortcuts import render
    from django.http import HttpResponse

    # Create your views here.

    def main(request):
        return HttpResponse("Hello")
    ```

    - You can change the function name as well as the contents that will be passed by HttpResponse (It's argument)

1. Go inside `{app_name}/urls.py` and import the function from your views
    ```
    from .views import {function_name}
    ```
1. Add to the contents of `urlpatterns`

    ```
    path("home", main)
    ```

    - You can add what ever path you want inside the string parameter

1. Go inside `{main_folder]/urls.py` and import `include` from `django.urls`
    ```
    from django.urls import include
    ```
1. Add to the contents of `urlpatterns`
    ```
    path("{app_name}/", include("{app_name}.urls"))
    ```

# Start the database and run your app

1. Just copy and paste the following. Make sure that you are inside your root app folder `{project_name}`

    ```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```

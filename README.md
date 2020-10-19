# Courses app
This task was given for the practical application of knowledge on REST API with the help of DJANGO and Django REST framework

## Installation
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Requirments


After uploading files, it's necessary to create a new virtual environment.
To do this use these commands(for Windows):

```bash
pip install virtualenv
python -m venv myvenv #or you can use another name for your venv
myvenv\Scripts\activate
```
Now that we're inside a virtual environment, we can install our package requirements:

```bash
pip install django
pip install djangorestframework
pip install pygments  # We'll be using this for the code highlighting
```

## Running the project

```bash
cd tutorial
pyhton manage.py runserver
```
In the terminal you will see a link to the local host. Like this one:
http://127.0.0.1:8000

_Then you can go through the sections:
* http://127.0.0.1:8000/  - Сourses list
* http://127.0.0.1:8000/course/ {course id}  - Course detail


## Built With


* [Django](https://docs.djangoproject.com/en/3.1/) - "The web framework for perfectionists with deadlines."
* [Django Rest Framework](https://www.django-rest-framework.org/)- toolkit for building Web APIs.
* [Django Rest Framework (Tutorial)](https://www.django-rest-framework.org/tutorial/1-serialization/)-To understand what serialization is
* [YT vebinars](https://www.youtube.com/watch?v=C6S3dMt1s_M&t=4852s) - for RESTful API Implementation
* Stackoverflow - answers to solve some problems


## Authors


 **Nurai Omurbek** - *Initial work* - **[Naurabay](https://github.com/Naurabay/)**


## Acknowledgments

* It's better to start with a common understanding for a start.
* Read the documentation first
* There are a lot of cool videos on YouTube
* **Need to sleep at night**

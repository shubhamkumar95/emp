Emps
========================================

About
-----
Combination of employee app and polls(used by django tutorials) app to understand the working of Django Rest Framework

Agenda
-------------

Introduction to REST and REST Framework.
Installation
Serialization
Request and Response
ApiViews
GenericApiViews
Mixins
Authentication And Permissions
Viewsets and Routers


Prerequisites
-------------

- Python >= 3
- pip3
- virtualenv
- django > 2
- djangorestframework

Installation
------------

#. Create a Python 3.6 virtualenv and setup a local development environment.

    $ virtualenv -p python3.6 ems
    $ source ems/bin/activate
    $ cd emps
    $ pip3 install -r requirements.txt


#. Run the migrations for databases:

    $ python3.6 manage.py makemigrations
    $ python3.6 manage.py migrate

#. Create Superuser to logged in Django admin panel (it is one time procedure)

    $ python3.6 manage.py createsuperuser

#. Start server in Development mode:

    $ python3.6 manage.py runserver


#. Hit http://0.0.0.0:8080/admin url in browser and login using superuser credentials which was created in initial steps.


Data models
-----------

#. Question
    
    This model contains all the details about questions.

#. Choice

	This model contains all the details about choices related to questions.

#. Vote

	This model lets the user to vote for poll according to choices given by the questions.






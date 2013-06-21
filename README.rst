========================
relabs
========================
django 1.5.1

To use this project follow these steps:

#. Create your working environment
#. Install Django
#. Create the new project using this template
#. Install additional dependencies
#. Use the django-admin.py to create the project

Working Environment
===================

You have several options in setting up your working environment.  We recommend
using virtualenv to seperate the dependencies of your project from your system's
python environment.  If on Linux or Mac OS X, you can also use virtualenvwrapper to help manage multiple virtualenvs across different projects.

Virtualenv Only
---------------

First, make sure you are using virtualenv (http://www.virtualenv.org). Once
that's installed, create your virtualenv::

    $ virtualenv --distribute you_project_name

You will also need to ensure that the virtualenv has the project directory
added to the path. Adding the project directory will allow `django-admin.py` to
be able to change settings using the `--settings` flag.

Installing Django
=================

To install Django in the new virtual environment, run the following command::

    $ pip install django

Creating your project
=====================

To create a new Django project called '**you_project_name**' using
django-project-devel, run the following command::

    $ django-admin.py startproject --template=this_template__django-project-devel.zip --extension=py,rst,html you_project_name

Installation of Dependencies
=============================

Depending on where you are installing dependencies:

In development::

    $ pip install -r requirements/local.txt

For production::

    $ pip install -r requirements.txt

*note: We install production requirements this way because many Platforms as a
Services expect a requirements.txt file in the root of projects.*

Acknowledgements
================

  To Do

 References
 ==========

 South::
 	http://south.readthedocs.org/en/latest/tutorial/index.html

 	$ ./manage.py schemamigration per_apps --initial
 	or
 	$ ./manage.py schemamigration per_apps --auto

 	grant all privileges on dev_relabs_db.* to 'dev_relabs_user'@xxx identified by 'you_password';

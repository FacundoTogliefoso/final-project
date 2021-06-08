===================
Final project for coder house python course
===================

===================
Docker Installation
===================
Pre-requisites
=================

* Docker
* Docker compose

Clone repository
================
::

    mkdir ~/projects
    cd ~/projects
    git clone git@github.com:FacundoTogliefoso/final-project.git
    cd ~/projects/final-project

Create docker image
===================
::


    docker-compose up --build

Makemigrations and migrate
===================
::

    docker exec -it finalproject /bin/bash
    python manage.py makemigrations
    python manage.py migrate
    
===================
Manual Installation
===================
Pre-requisites
=================

* Install pip virtualenv

=====
Steps
=====


Clone repository
================

    mkdir ~/projects
    cd ~/projects
    git clone git@github.com:FacundoTogliefoso/final-project.git
    cd ~/projects/final-project

Activate virtualenv and go to project folder::
=====================
    pipenv shell

Additional Libraries::

    $ pip install -r requirements.txt

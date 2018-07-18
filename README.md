# CastBuddy Back-End

This is the back-end of the CastBuddy server-side software. It has an incoming REST endpoint designed for Hologram to push data into the database, and it has outgoing REST endpoints to retrieve data from the database.

## Database Configuration

In all cases of this app running, it requires access to a MySQL database. Prior to any development or deployment, ensure that:

1. Such a database exists with a schema called castbuddy.
1. The database must have the username cb_admin configured with read and write access to the castbuddy schema.
1. On all development and deployment servers, configure the following environment variables:
  1. `DB_ROOT` set to the URI of the database, e.g. `database.rds.amazonaws.com`
  1. `CB_PASS` set to cb_admin's password for the database

## Development

### Required Packages

Install the following packages in the following order:

1. Install [Python](https://wiki.python.org/moin/BeginnersGuide/Download)
    1. On Mac, it's suggested you first install [homebrew](https://brew.sh/) and install python3 through it via `brew install python3`.
1. Install [PIP](https://pip.pypa.io/en/stable/installing/)
    1. On Mac, it's suggested you first install [homebrew](https://brew.sh/) and install pip3 through it via `brew install pip3` (on mac, all calls to pip will be pip3 instead).
1. Install [virtualenv](https://virtualenv.pypa.io/en/stable/installation/) via PIP.

### Environment Setup

Development should be done in a python virtual environment to keep the packages necessary for this project decoupled from any individual's local environment.

1. Open a terminal and `cd` into the repo root.
1. Create a directory called "venv".
1. Create a new virtual environment in the venv directory with `virtualenv venv`.
1. Open the file venv/bin/activate and add this line to the end: `export FLASK_APP=./application.py`.
1. Enter the new virtual environment with `source venv/bin/activate`.
1. Install the project's top-level dependencies with `pip install -r requirements-top.txt`
1. You can exit the virtualenv with `deactivate`.

### IDE Setup

If your IDE supports python parsing, configure your workspace to use the python binary located in ./venv/bin/python.

Depending on your IDE, when you open the project for the first time you may be prompted to install pylint. If you want to use the python linter, you must install it manually in the virtualenv.

1. In a terminal enter the virtualenv.
1. Install pylint with `python -m pip install -U pylint`.

### Run App

1. In a terminal enter the virtual environment.
1. Run the app with `flask run`.
1. The console should tell you your app is being served at http://127.0.0.1:5000/ (aka localhost:5000).

### Maintaining Requirements

You'll notice there are two requirement files: requirements-top.txt and requirements.txt. The idea behind this is that only a select few libraries are specifically called in the python project. Those select few libraries are listed in requirements-top.txt as the "top-level" dependencies, without a specific version number. When setting up a development environment and running `pip install -r requirements-top.txt`, further dependencies of the used libraries are installed.

As you develop, if you need to add libraries to the project, be sure to record them in requirements-top.txt.

When you're ready to push up to the server, requirements.txt needs to be updated. This file will be a "snapshot" record of all libraries in your development environment, including sub-dependencies and version numbers (this is analogous to npm's package.json and package-lock.json paradigm), so that when deploying to production, the _exact_ environment used in development can be reproduced in deployment.

Follow this process to update requirements.txt before pushing:

1. Make sure requirements-top.txt is updated.
1. Clear all libraries currently in venv:
    1. `pip freeze > requirements.txt`
    1. `pip uninstall -r requirements.txt -y`
1. Re-install dependencies from requirements-top.txt: `pip install -r requirements-top.txt`
1. Try running the flask app to make sure requirements-top.txt actually captures all necessary dependencies: `flask run`
    1. If you get errors due to missing dependencies, resolve them and update requirements-top.txt accordingly.
1. Once you're sure you have only the libraries necessary for the project to run in venv, run `pip freeze > requirements.txt` to update requirements.txt.
1. Commit and push.

Source: https://www.kennethreitz.org/essays/a-better-pip-workflow.

## Deployment

Deployment can be done in a number of ways according to [Flask's documentation](http://flask.pocoo.org/docs/0.12/deploying/). One of the simpler ways to deploy is with gunicorn:

1. Ensure Python is installed on the deploy server.
1. `git clone` the repository on the server.
1. Follow the steps in [Environment Setup](environment-setup), this time using requirements.txt.
1. Enter the virtual environment.
1. Serve the app with `gunicorn app:app -w 4 > api.log 2>&1 &`. This will serve on the default port of 8000.
1. Use a reverse proxy like nginx to link an external port/address to localhost:8000.

To takedown the app, run `pkill gunicorn`.
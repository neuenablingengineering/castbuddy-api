# CastBuddy Data API

## Development

Development can be done in a native python environment, or utilizing a virtual environment. The latter is suggested just to keep your workspace clean.

Regardless of whether you develop in the venv, you must keep it maintained though, meaning if you add any packages to the project via pip, make sure you run `pip freeze > requirements.txt` in the repo root, and include requirements.txt in a commit and push. This is because we currently deploy to AWS Elastic Beanstalk, which uses the requirements.txt file to build the environment within which the app runs.

### Required Packages

Install the following packages in the following order:

1. Install [Python](https://wiki.python.org/moin/BeginnersGuide/Download)
    1. On Mac, it's suggested you first install [homebrew](https://brew.sh/) and install python3 through it via `brew install python3`.
1. Install [PIP](https://pip.pypa.io/en/stable/installing/)
    1. On Mac, it's suggested you first install [homebrew](https://brew.sh/) and install pip3 through it via `brew install pip3` (on mac, all calls to pip will be pip3 instead).
1. Install [virtualenv](https://virtualenv.pypa.io/en/stable/installation/) via PIP.

### Environment Setup

To run the app, set up your environment with the following:

1. Open a terminal and `cd` into the repo root.
1. Create a directory called "venv".
1. Create a new virtual environment in the venv directory with `virtualenv venv`.
1. Open the file venv/bin/activate and add this line to the end: `export FLASK_APP=./application.py`.
1. Enter the new virtual environment with `source venv/bin/activate`.
1. Install the project's dependencies with `pip install -r requirements.txt`
1. You can exit the virtualenv with `deactivate`.

Note: installing the dependencies can be done in your native environment instead of a virtual environment, but it will install the dependencies permanently in your native environment.

### IDE Setup

If your IDE supports python parsing, if you are using virtualenv, configure your workspace to use the python binary located in ./venv/bin/python.

Depending on your IDE, when you open the project for the first time you may be prompted to install pylint. If you want to use the python linter, you must install it manually in the virtualenv.

1. In a terminal enter the virtualenv.
1. Install pylint with `python -m pip install -U pylint`.

### Run App

1. In a terminal enter the virtual environment.
1. Run the app with `flask run`.
1. The console should tell you your app is being served at http://127.0.0.1:5000/ (aka localhost:5000).

## Deployment

Deployment can be done in a number of ways according to [Flask's documentation](http://flask.pocoo.org/docs/0.12/deploying/). One of the simpler ways to deploy is with gunicorn:

1. Ensure Python is installed on the deploy server.
1. `git clone` the repository on the server.
1. Follow the steps in [Environment Setup](environment-setup).
1. Enter the virtual environment.
1. Additionally install gunicorn with `pip install gunicorn`.
1. Serve the app with `gunicorn app:app -w 4`
1. To takedown the app, run `pkill gunicorn`
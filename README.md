# CastBuddy Data API

## Development

### Required Packages

Install the following packages in the following order:

1. Install [Python](https://wiki.python.org/moin/BeginnersGuide/Download)
1. Install [PIP](https://pip.pypa.io/en/stable/installing/)
1. Install [virtualenv](https://virtualenv.pypa.io/en/stable/installation/) (via PIP)

### Environment Setup

To run the app, set up your environment with the following:

1. Open a terminal and `cd` into the repo root.
1. Create a directory called "venv".
1. Create a new virtual environment with `virtualenv venv`.
1. Enter the new virtual environment with `source venv/bin/activate`.
1. Install the project's dependencies with `pip install -r requirements.txt`
1. You can exit the virtualenv with `deactivate`.

### Run App

1. Enter the virtual environment.
1. Run the app with `flask run`.
1. The console should tell you your app is being served at http://127.0.0.1:5000/ (aka localhost:5000).
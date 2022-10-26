# Working on Dextre

## Setting up a development instance

- Install PostgreSQL and create a blank database 
```shell
sudo apt install postgresql postgresql-contrib
sudo su potgres
psql
```
In `psql`:
```
CREATE USER uwcs_dextre WITH PASSWORD 'password';
CREATE DATABASE uwcs_dextre WITH OWNER = uwcs_dextre;
\q
```

- Install NodeJS and NPM \
There are two approaches you can take here:
  - Use [Node Version Manager](https://github.com/nvm-sh/nvm) to install NodeJS. This is an easy way to install and use multiple versions on your machine.
  - Install via your package manager:
  ```shell
    curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -
    sudo apt-get install -y nodejs
  ```
  
- Install system-wide dependencies
```shell
sudo apt-get install virtualenv build-essential python3 python3-pip python3-dev redis libxml2-dev libxmlsec1-dev libxmlsec1-openssl
npm install -g sass
```

- Clone the GitHub repository and move into that directory
```shell
git clone https://github.com/UWCS/uwcs-dextre.git
cd uwcs-dextre/
```

- Create a Python virtual environment and install Python dependencies
```shell
python3 -m venv venv
source venv/bin/activate
pip3 install wheel
pip3 install -r requirements.txt
```

- Install Node dependencies
```shell
npm ci
```

- Head to the `dev.py` settings file in `dextre/settings` and ensure any database settings match the database you created earlier. If you are deploying to production, create an appropriate `production.py` file in the same directory, using `production.py.example` as a starting point.

- Create a directory in the root directory called `media` - this is where Wagtail stores any uploaded images or documents.

- Apply database migrations and create an admin user
```shell
python3 manage.py migrate
python3 manage.py createsuperuser
```

- Start the development server
```shell
python3 manage.py runserver
```

- Head to http://localhost:8000 and you should see a blank site with the text "Welcome to your new Wagtail site!"

- Go to http://localhost:8000/cms and sign in with the admin user you just created. Head to Pages in the sidebar, and create the following base pages with the following hierarchy:
```
UWCS Home *type - home page
|- About *type - about page
|- News *type - blog index page
|- Events *type - events index page
 |- Events archive * type - events archive page
```

- Set your new home page as the root page of the website by heading to Settings -> Sites in the CMS and click edit on the default site in there. Then click "Choose a different root page" under these settings and pick your home page. Click Save and continue as normal.

### Optional steps for local development
- Start a celery worker for asynchronous tasks (namely for shell account creation and sending a selection of emails). In production, the celery instance is run using Supervisor, but this is not requried for local development. Ensure you have redis-server set up before trying this step. Open a new terminal in the root directory and run:
```shell
source venv/bin/activate
celery -A dextre worker -l info
```

- You can configure an SMTP server for sending email in `dev.py` by following the instructions on the [Django website](https://docs.djangoproject.com/en/3.2/topics/email/#smtp-backend). Alternatively, you can supply an API key for Sendgrid and use that instead.

## Formatting & General Guidelines
- Black is used to ensure formatting guidelines are followed across the project. Before submitting a PR, run `black .` from the root directory of the project to ensure all files are correctly formatted, otherwise the CI will fail upon push or PR.
- The Gitmoji standard is used for commit messages. See [the Gitmoji website](https://gitmoji.dev/) for a guide of how it works and the emoji icons to use in commit messages.
- Work on new features or changes in a feature branch. If an issue on GitHub exists, use the issue number as the branch name, otherwise use something descriptive. Try to ensure commit messages describe what the change actually is as opposed to generic messages.
- Point any PRs created to the `develop` branch.

## Deployments & Releases
When changes are merged to `develop`, someone in the tech team will eventually deploy the website to the staging environment. This runs separately from the production instance, including with a separate database. This instance points to idp-test at Warwick, so single-sign-on should still work but routed through the test instances of WSO at Warwick. Use this environment to check that nothing is majorly broken.

When you are ready to deploy to live, create a PR merging `develop` into `master`, and make the PR name the version number of the "release". Version numbers follow the format YYYY.MM, where YYYY and MM represent the year and month of the deployment. If you have multiple deploys in a month, add on a .X where X increases incrementally from 1. Once merged, someone in the tech team will follow the steps provided to deploy to the production instance.
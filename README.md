# uwcs-dextre

### Contents
* [About](#about)
* [Installation](#installation)
  * [Dependencies](#dependencies)
  * [Installation and Configuration](#installation-and-configuration)
* [License](#license)

### About
uwcs-dextre is the latest in a long line of University of Warwick Computing Society websites, started immediately before the 2020-21 academic year. The site uses Python, Django and the [Wagtail CMS](https://github.com/torchbox/wagtail) (currently).

The name 'Dextre' comes from the ISS module of the same name. The previous website, named 'Zarya', shares a name with another eponymous module of the ISS. The name for that version having been derived from the computer game Overwatch.

### Installation
This section details the deployment of uwcs-dextre on a Linux system.

#### Dependencies
uwcs-dextre depends upon a variety of softwares though at its core the website is built upon the Django web framework. The list of dependencies are:

* Python 3.8 (has also been tested with Python 3.9 and 3.10)
* Redis
* Sass (Ruby)
* Bower (npm/node)
* Postgresql
* Virtualenv
* Supervisor

The deployment of the website on the UWCS systems also uses Apache 2 and mod_wsgi for a web server, though it would be possible to use nginx too. The site also uses a transactional email provided for email, though normal SMTP is planned to be used and configured using Django's standard configuration settings.

#### Installation and Configuration
**These instructions are soon going to be rewritten. Versions here are probably out of date and need updating**

With the packaged dependencies installed and configured (most/all should be available with any Linux distribution's package manager), the steps for installation of the website are as follows, though you may want to stop after step 5 if you are not going to deploy the website for production purposes:

1. (Optional) Create a virtualenv to run the server from - make sure it's using python 3.8 or 3.9
2. `git clone` the repository to the location you wish to serve the site from (e.g: `/var/www/uwcs-dextre`)
3. Install the `wheel` package which is required for the configuration of some other python packages using `pip install wheel` (using the virtualenv if you are using one)   
4. Install the requirements using `pip install -r requirements.txt` (make sure you're using the virtualenv if you're using one)
5. `cd uwcs-dextre/dextre/settings` and create an appropriate settings file `production.py` from the provided sample `production.py.example`
6. `cd uwcs-dextre/` and bring the backend database up to speed by running `python manage.py migrate` - if you're using a virtualenv do make sure you are running python from it
7. *(Note May 2022: I don't think you need this step anymore, and was only needed for development anyway)* Download the [Bulma](https://bulma.io/) CSS files from their website, and copy `bulma.scss` and the `css` and `sass` folders from the downloaded zip file into `uwcs-dextre/static/scss`
8. `cd uwcs-dextre/dextre/components` and then install the Bower dependencies using `bower install` (if you are not deploying for production, you may skip to point 11 at the end of the list)
9. `cd uwcs-dextre/` and run `python manage.py compress --force` and `python manage.py collectstatic`, accepting where applicable
10. Create a directory `uwcs-dextre/media`, ensuring your web server has sufficient access to this folder (`rwx` permissions)
11. Create the appropriate configuration files for Supervisor to run Celery automatically and allow it to recover on restart
12. Create the configuration file(s) for the web server of your choosing
13. Run your web server (if you're developing locally, simply run `python manage.py runserver`

#### Ubuntu 20.04 development setup
**As above, these instructions are soon going to be updated rewritten in more detail.**

These are (mostly) tested on Josh's system using WSL 2 & Ubuntu 20.04. They aren't complete and should be used in conjunction with the configuration instructions detailed above.

If you blindly follow these instructions, you should have a working instance of the website.

Setup PostgreSQL database:
```
sudo apt-get install postgresql postgresql-contrib
sudo -u postgres createuser -D -A -P dextre
(enter 'password' as password)
sudo -u postgres createdb -Odextre dextre
```

Install system-wide runtime/build dependencies:
```
sudo apt-get install virtualenv build-essential python3 python3-pip redis ruby-sass
```

Install NodeJS

*I'd recommend using something like [Node Version Manager](https://github.com/nvm-sh/nvm) to install Node instead of just installing from your package manager. This makes it nicer to have multiple versions of NPM and NodeJS installed on your machine at once.*

```
curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -
sudo apt-get install -y nodejs
```

Create python virtualenv and install python dependencies:
```
python3 -m venv venv
source venv/bin/activate
pip3 install wheel
pip3 install -r requirements.txt
```

Fetch bower components:
```
cd dextre/components
npm install bower
bower install
```

Ensure the database settings in `dev.py` and `production.py` match the database you created earlier.

Seed the database:
```
python3 manage.py migrate
python3 manage.py createsuperuser
```

Start development server:
```
python3 manage.py runserver
```

Go to http://localhost:8000 and you should see a basic instance of the site!

Head to http://localhost:8000/cms and sign in with the superuser you just created. Head to Pages, and create the following pages with the below hierarchy:
```
UWCS Home *type - home page
|- About *type - about page
|- News *type - blog index page
|- Events *type - events index page
 |- Events archive * type - events archive page
```

You should now have the basic structure set up for the website to function. You can go ahead and add other pages and content to it.

The last step is to start a celery worker for background tasks. Ensure you have redis-server set up before trying this step. Open a new terminal and run:

```
source dextre-env/bin/activate
celery -A dextre worker -l info
```

### License
This project is distributed under the MIT license.

The MIT License (MIT)
=====================

Copyright © 2016 David Richardson

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the “Software”), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

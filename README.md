# cartotron


### Structure

The project currently has 6 main directories:

* **cartotron** - main project directory with settings and urls
* **shop** - data models, views and templates for viewing store products
* **cart** - data models, views and templates for managing the cart
* **frontend** - app to hold common front end resources (JS and CSS)
* **sql** - raw SQL scripts for db schema and basic sample data
* **templates** - project level shared templates

### Requirements

* Python 2.7.x
* MySQL (5.7 recommended)


### Setup

The project should be run in a virtual environment  (isolated Python environment) to stop any conflicts from happening.  You can read more [here](https://virtualenv.pypa.io/en/latest/)

You should already have MySQL 5.7 and MySQL Workbench set up.

Steps:

* `pip install virtualenv` - install virtualenv
* `virtualenv cartotron` - create a new virtualenv
* `source /path/to/virtualenv/bin/activate` (OSX/Linux) or `C:\path\to\virtualenv\Scripts\activate` (Windows) - activate the virtualenv
* `pip install -r requirements.txt` - install project specific python packages
* `python manage.py createsuperuser` - create yourself an admin user

Optional (if you do not set up the database with the SQL scripts)

* `python manage.py migrate` - create the database tables



You can log in at [http://localhost:8000/admin/](http://localhost:8000/admin/) by default
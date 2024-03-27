# Hole Recording Gruppe

Hole Recording Gruppe is a record label operating in Portland, Oregon, USA.

## Technologies

* Python3.10
* Virtualenv
* Django 5.0.3
* Node 16.14.0


## Installation and Usage

```shell
# clone the repo
git clone https://github.com/seanpierce/hole-recording-gruppe.com

cd hole-recording-gruppe.com

# install virtual environment
python -m venv ./venv

# connect to venv
source ./venv/[windows: "Source", Linux/ Mac: "bin"]/activate

 # install requirements
pip install -r requirements.txt

# create admin and migrate db
python manage.py createsuperuser

python manage.py migrate

# run the site
python mange.py runserver

# build (and watch) the stylesheets/ sass
npm run build-sass
```
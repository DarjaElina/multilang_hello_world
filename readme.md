# Multilang app on django "hello world!"

- This project is created for testing multilanguage switching in django

- Requires python3 installed on system

```bash
# example brew
brew search python
brew install python@3.11
```

- Setup env

```bash
pip install virtualenv # not necessary

# creating and fresh activation venv
virtualenv venv
source venv/bin/activate

# install requirements
pip install -r requirements.txt

# dump requirements if needed
pip freeze > requirements.txt
```

```bash
# add langs to locales
python manage.py makemessages -l <langcode> 
# compile messages 
python manage.py compilemessages
```

```bash
# make migrations
python manage.py makemigrations
# migrate to DB (sqlite3)
python manage.py migrate

# run application
python manage.py runserver
```
```bash
# using predefined start script
chmode +x start.sh
./start.sh
```

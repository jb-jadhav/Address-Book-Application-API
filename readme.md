----install venv
pip  virtualinstallenv

----activate virtualenv
virtualenv venv
venv\Scripts\activate

--- install requirement file
pip install requirement.txt

---makemigration 
python manage.py makemigrations

---migrate
python manage.py migrate

---- run developemnt server
python manage.py runserver

--- starting developement server at 
http://127.0.0.1:8000/

---- see result in online result using sqlite
https://sqliteonline.com/ 
-------click on [file] icon
-------clicn on [open db] icon
-------select in db.sqlite3 in addressbook app

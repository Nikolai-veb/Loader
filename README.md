# Loader

# Install

git clone https://github.com/Nikolai-veb/Loader.git

cd Loader

source venv/bin/activate

pip install -r requirements.txt

python manage.py runserver

# Tests

python manage.py test gallery.tests.test_models.py

python manage.py test gallery.tests.test_views.py

# To access the admin panel use

127.0.0.1:8000/admin

Nikname = "Admin"

Password = "12345"

#!/bin/bash

# sudo chmod +x wait-for-it.sh

echo "Waiting for database..."
/app/wait-for-it.sh db:5432 --timeout=30 --strict -- echo "Database is ready."

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Collect static files (if needed)
# python manage.py collectstatic --noinput

# Run the Django app
exec python manage.py runserver 0.0.0.0:8000

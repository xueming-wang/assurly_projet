#!/bin/bash

docker-compose up -d --build

echo "Applying migrations..."
sleep 5

docker exec -it assurly_project_backend python manage.py makemigrations assurly
docker exec -it assurly_project_backend python manage.py migrate

echo "Migrations applied"
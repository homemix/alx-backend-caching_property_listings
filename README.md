# Caching in Django

# Objective
Initialize a Django project for the property listing app, configure PostgreSQL and Redis in Docker, and set up the cache backend.

# Instructions
## 1. Create the Django Project:

* Initialize a Django project named alx-backend-caching_property_listings.
* Create a Django app named properties inside the project.
* Create a Property model in properties/models.py with fields:
* title (CharField, max_length=200)
* description (TextField)
* price (DecimalField, maxdigits=10, decimalplaces=2)
* location (CharField, max_length=100)
* created_at (DateTimeField, autonowadd=True)
* Run migrations to create the database schema.

## 2. Set Up Dockerized PostgreSQL and Redis:
* Create a docker-compose.yml file in the project root to define two services:
* PostgreSQL: Use the official postgres:latest image, expose port 5432, and set environment variables for database configuration.
* Redis: Use the official redis:latest image, expose port 6379.
* Ensure both services are accessible from the Django app (e.g., PostgreSQL via postgres:5432, Redis viaredis:6379).
## 3. Configure Django Settings:

* Install required Python packages: django, django-redis, psycopg2-binary.
* Add django-redis to INSTALLED_APPS in alx-backend-caching_property_listings/settings.py.
* Configure the database to use PostgreSQL in alx-backend-caching_property_listings/settings.py
* Configure Redis as the cache backend in alx-backend-caching_property_listings/settings.py
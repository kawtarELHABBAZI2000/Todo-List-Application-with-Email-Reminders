# Todo List Application with Email Reminders

## Overview

This project is a Todo List application with email reminder functionality, consisting of a Django backend, FastAPI service for email reminders, and a Vue.js frontend and Docker for containerization.

## Django Backend

## Set Up Django Project

```bash
# Install Django
python.exe -m pip install --upgrade pip
pip install Django
django-admin --version

# Create Django project and app
django-admin startproject django_backend
cd .\django_backend\
python manage.py startapp django_app


# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create Superuser
python manage.py createsuperuser

# Run Development Server
python manage.py runserver


# Visit http://localhost:8000/api/todos/ and use Postman to test API endpoints

```


# FastAPI Email Reminder Service


# Install FastAPI and Uvicorn:
python -m pip install fastapi uvicorn[standard]

### Run the FastAPI service:
uvicorn app.main:app --reload --port 8001

## Vue.js Frontend
Vue CLI Installation


# Install Vue CLI
npm install -g @vue/cli

# Create Vue project
vue create vue_frontend
cd vue_frontend

## Install Axios for HTTP Requests:
npm install axios

## Run the Vue.js app:
npm run serve

# Usage
### Access the Django backend API at http://localhost:8000/api/todos/.
### Run FastAPI service for email reminders at http://localhost:8001.
### Start the Vue.js app and interact with the Todo List application.



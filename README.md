# Django-Mysql-CRUD

## Table of Contents:
1. About The Project
2. Getting Started
   - Prerequisites
   - Installation
3. Steps
4. Run
5. Skills Covered
------------------

## 1. About The Project :

   Creating a Django Web-Application for CRUD(Create, Read, Update and Delete) operations on a MySQL Database and view the data in the localhost.

## 2. Getting Started :

-  ### PREREQUISITES :
   + Django
   + pymysql
   + bootstrap4
   + crispy-forms
   + MySQl Workbench
     
- ### INSTALLATION :
  
  create a python virtual enviroment on command prompt
  + Choose the folder to create python venv and write the following command by replacing envname with a environment name
  
        python -m venv myvenv
  + Changing Directory to activate venv
    
        cd myvenv\Scripts
  + Activating venv
 
        # To activate the virtual environment
        activate.bat
  + Go back to folder where you want to create django project using cd
    
  + Installing django library and create django project --> Replace the projname with project name 

        django-admin startproject projname

  + The Django project folder with projname added to the selected path

        # Replace MyApp with your app name to register a app
        django-admin startapp MyApp

  + Install the crispy forms library which we used

        pip install django-crispy-forms

## 4. STEPS :
   + In setting.py register these template and app that we will use in the project

           INSTALLED_APPS = [
          'django.contrib.admin',
          'django.contrib.auth',
          'django.contrib.contenttypes',
          'django.contrib.sessions',
          'django.contrib.messages',
          'django.contrib.staticfiles',
          'MySql_CRUD',
          'crispy_forms',   
          ]
      
          STATICFILES_DIRS=[
          BASE_DIR/'static',
          ]  
    
          CRISPY_TEMPLATE_PACK='bootstrap4'
  + Database Registration replace pass --> with your MySql password

          DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'django',
                'USER': 'root',
                'PASSWORD': 'pass',
                'HOST': '127.0.0.1',
                'PORT': '3306',
                }
            }
  + my model at models.py in app

          from django.db import models

          # Create your models here.
          class RegisterForm(models.Model):
              name = models.CharField(max_length=100)
              age = models.IntegerField()
              address = models.CharField(max_length=100)
              contact = models.CharField(max_length=100)
              email = models.EmailField()
          
              class Meta:
                  db_table = 'datas'  # creates a table named datas
  + Creating form in app named forms.py

            from django import forms
            from .models import RegisterForm
            
            class MyRegisterForm(forms.ModelForm):
                class Meta:
                    model = RegisterForm
                    fields = ['name', 'age', 'address', 'contact', 'email']
  + After creating the model and DB connection need to make migration to establish connection with DB

           python manage.py makemigration
  + Then migrate command to reflect in DB
    
           python manage.py migrate 
  + Creating functions to work on url request at views.py 
  + Creating HTML templates for web interface and registering path in URL's at urls.py
  + we have used bootstrap4 for this project designing so download the static folder in my project

## 5. RUN :
   > - I have attached the images of the website after completing project
   > - To Run this project we need to go to terminal with the project location
   > - Then run this code to execute,

           python manage.py runserver
   - The Output Images are attached in the Output section



  
 



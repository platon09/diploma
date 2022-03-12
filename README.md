# Diploma project

##  Instructions for use and launch app.

1. Configure virtual environment settings

    1.1 Create virtual environment and activate it
    
    ```bash
    virtualenv -p python3.8 .venv
   source .venv/bin/activate
    ```
    1.2 Install required libraries

    ```bash
    pip install -r requirements.txt
    ```

2. Migrate and seed the database and create super user

    ```bash
    ./manage.py makemigrations
    ./manage.py migrate
    ```
   
    ```bash
    ./manage.py createsuperuser
   
   username:admin
   email:
   password:admin
    ```

3. Run the server and check it by opening localhost:8000 in web browser

    ```bash
    ./manage.py runserver
    ```
    
4. Test API documentation

    ```
    http://127.0.0.1:8000/api/docs/
    ```

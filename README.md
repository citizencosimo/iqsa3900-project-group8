# iqsa3900-project-group8

Once you clone the project, you will have to complete further steps in order to set up the venv and environment variables.

1. Clone the repository using git clone https://github.com/citizencosimo/iqsa3900-project-group8.git
2. After you open the project in pycharm, you may have to select which version of Python you want to use by clicking in the bottom right corner.
3. Open a terminal line and enter the following: python -m venv venv
4. Activate the virtual environment: ./venv/Scripts/activate
5. Enter: pip install -r requirements.txt
6. Create a file in the top level directory (where manage.py is) called ".env"
7. Copy this line into .env: [Please contact Jason if you still need the salt]
8. Test that the server is running correctly using python manage.py runserver
9. If you see the basic Django screen it is set up correctly. If you see "a server error occured" check that you named .env correctly and copied the entire string.
10. Run the command: python manage.py makemigrations
11. Run the command: python manage.py migrate
12. Run the command: python manage.py createsuperuser and set up an account.

# iqsa3900-project-group8

This is the source code for a simple game review interface. It allows users to make accounts and write reviews for games in a database. Staff accounts have access to the entire database and the ability to edit it.

Once you clone the project, you will have to complete further steps in order to set up the venv and environment variables.

1. Clone the repository using git clone https://github.com/citizencosimo/iqsa3900-project-group8.git
2. After you open the project in pycharm, you may have to select which version of Python you want to use by clicking in the bottom right corner.
3. Open a terminal line and enter the following: python -m venv venv
4. Activate the virtual environment: ./venv/Scripts/activate
5. Enter: pip install -r requirements.txt
6. Create a file in the top level directory (where manage.py is) called ".env"
7. Set up environment variables for a secret key, default email, and email app password. Other configurations may be necessary if you are not using gmail.
8. Switch server to debug mode if you plan to make changes.
9. Run the command: python manage.py makemigrations
10. Run the command: python manage.py migrate
11. Run the command: python manage.py createsuperuser and set up an account.

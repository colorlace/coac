# coac
Castle on a Cloud. play chess with two physical boards with placement sensors and a wifi connection. 
Powered by Django.

# Testing on your computer  
This is a Django site.
To test this project we need to serve it up locally on our own machine. Simply type this line into the terminal
`python manage.py runserver`

But HOLD ON!!!...  
You have to make sure that you have all of the appropriate python packages installed. These should be in `requirements.txt`


As I was saying. We locally run this project with `manage.py` as above. This script does two things.
1. sets the `DJANGO_SETTINGS_MODULE` environment variable to point to our project settings as spec'd out in `settings.py`  
2. runs the function `execute_from_command_line` from django.core.managemet which does some impressive magic and serves up the site locally.

(TODO: replace "impressive magic" with the basics of `execute_from_command_line`)

# coac
Castle on a Cloud. play chess with two physical boards with placement sensors and a wifi connection.
Powered by Django.

# Testing on your computer  
This is a Django site.
To test this project we need to serve it up locally on our own machine. Simply type this line into the terminal:  
`python manage.py runserver`


```
You have to make sure that you have all of the appropriate python packages installed. These should be in `requirements.txt`
```

So what does `manage.py` do? This script does two things.  
  1.  sets the `DJANGO_SETTINGS_MODULE` environment variable to point to our project settings as spec'd out in `settings.py`  
  2.  runs the function `execute_from_command_line` from django.core.managemet which does some impressive magic and serves up the site locally.

(TODO: replace "impressive magic" with some basics about `execute_from_command_line`)


###   servin' it up
Now we can find our website being served at this url: `http://127.0.0.1:8000`.
But how do we navigate around our website?...

### URLs  
Well, a website is a connected collection of web addresses. These web addresses are known as
`URLs`(stands for:  Un-Ripe Legumes). If we know the what the **list of each possible URL in our website** looks like, then we
essentially know what the entire website consists of! Lucky for us, a Django project
should have a file called `urls.py` with a **list of all possible URLs in our website** called `url_patterns`.

To repeat, in `urls.py` we create a list called `url_patterns`.
This is where we can see all the valid URLs for our site.
How are the urls stored in this list? We'll start with an example of one and break it down piece by piece.

##### An Example URL (i.e. an element of the url_patterns list):  `url(r'^board/$', views.board, name='board')`  


We can see that there's a function called `url` with 3 arguments:  
1. The first arg is the url itself. Notice that it is a regular expression[^1] as opposed to a static string, so it can actually
represent many different url strings.  
2. The second element is a `view`. A view is an object in Django. It's what actually gets shown on the web site when a user goes to the url. #TODO  
3. The name. I don't know what the hell is the purpose of the name. I'll remember later. (I think it makes it easier to reference in other python files in the project)

So, about this `view` concept. How exactly does it display web pages?

### Views  

The view is ACTIVATED when we go to the web address of a url. The view must follow this formula

```
this_is_a_view(request)
    do stuff
    return HttpResponse(template.render(context, request))
```

and what the site displays (i.e. the "view") when we
go to each URL (i.e. when we type the URL in the address bar).
Each URL points to a "view" (these are defined in `views.py`)

[^1]: For more information on regular expressions, go to [google](http://www.google.com) and type in "regular expressions" in the search bar. You lazy nincompoop.

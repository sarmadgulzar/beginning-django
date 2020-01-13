# Creating websites with [Django](http://djangoproject.com)

## Introduction:

[Django](http://djangoproject.com) is a web framework written in Python. It is a high-level framework that saves you the hassle of low-level web development so that you can focus on what really matters instead of reinventing the wheel. On Django's website, they call it:
> *The web framework for perfectionists with deadlines.*

And that really is the case because Django makes it super easy to create the backend of your web application very quickly. Python has other frameworks like [Flask](https://www.palletsprojects.com/p/flask/), [Tornado](https://www.tornadoweb.org/en/stable/), etc. but Django has gained a huge amount of popularity. A few key features of Django are as follows:

- Quick prototyping
- Built-in [ORM](https://en.wikipedia.org/wiki/Object-relational_mapping) (Object Relational Mapper)
- A beautiful admin panel, out of the box
- Built-in authentication and authorization
- Powerful web forms

and many more!

Now its time to install Django on your computer.

## Installation:

I'll assume that you have [Python](https://www.python.org/) and [pip](https://pypi.org/project/pip/) installed on your system and they are added to your PATH variable. The latest version of Django is `3.0.2` at the time of writing this tutorial and that's the one we are going to use.

To install Django, write this command in your terminal/prompt:
```
$ pip install django
```

If everything goes well, you should be able to run the following commands to verify your Django installation.

```
$ python
```
```python
>>> import django
>>> django.__version__
'3.0.2'
```

Fantastic work installing Django on your computer. Now let's go ahead and create a website using ```django-admin```. It is basically a command-line utility used to create *django projects* and to do few other things. You don't have to worry too much about this as we'll come back to this later. For now, just run the following command in terminal/prompt:

```
$ django-admin startproject myproject .
```

The directory structure should look like this:
- myproject/
  - ```__init__.py```
  - ```asgi.py```
  - ```settings.py```
  - ```urls.py```
  - ```wsgi.py```
- ```manage.py```
  
If you feel confused after seeing so many files, please don't. I understand that starting with Django can feel somewhat tedious, but I promise it all will make sense later.

Fire up the terminal and run the following command:

```
$ python manage.py runserver
```

You'll see an output similar to this:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
January 14, 2020 - 01:45:59
Django version 3.0.2, using settings 'myproject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Now open your favorite browser and go to the following URL: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

You will see a page like this:

![Django Welcome Screen](https://github.com/sarmadgulzar/beginning-django/raw/master/images/01.png)

Great work so far. Now, let me briefly explain the files in ```myproject``` folder and ```manage.py``` file.

### ```manage.py```
Just like ```django-admin```, it is a command-line tool to do different things like, for example, starting a server we just did above using:

```
$ python manage.py runserver
```

Later on, we'll see many more things that we can do using ```manage.py```.

### ```myproject/__init__.py```
This empty file is just there to treat ```myproject``` folder as a *module*.

### ```myproject/settings.py```
This file contains settings for the Django project. A few important ones are ```DEBUG```, ```INSTALLED_APPS```, ```DATABASES``` etc. We'll discuss them in detail later.

### ```myproject/urls.py```
These are the routes for our web applications. Only URLs defined inside this file will be accessible.

### ```myproject/asgi.py``` and ```myproject/wsgi.py```
These files are used when we deploy our application to the web server on the cloud so no need to worry about them just yet.

## Creating  a Hello World page:
Now that you have a basic understanding of how Django works, let's create a simple application that prints ```"Hello World"``` on our home page.

Open the ```myproject/urls.py```, it should look similar to this:

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

Let's add a few things, so it looks like this:

```python
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse # new line

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: HttpResponse("Hello World")), # new line
]
```

Now when you go back to the browser, you'll see this page:

![Hello World Page](https://github.com/sarmadgulzar/beginning-django/raw/master/images/02.png)

That way easy, no?

Okay, that ```lambda``` expression looks weird. Let's create a separate file called ```views.py``` to contain our views.

Now our directory structure will look like this:
- myproject/
  - ```__init__.py```
  - ```asgi.py```
  - ```settings.py```
  - ```urls.py```
  - ```views.py```
  - ```wsgi.py```
- ```manage.py```

Now update the ```views.py``` file so it looks like this:

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")

```

and ```urls.py``` will look like this:

```python
from django.contrib import admin
from django.urls import path

from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]

```

Now go back to the browser and refresh the page. You'll see the same results. But now our code is much cleaner, isn't?

To give you about how *URLs* work in Django. Change ```views.py``` as follows:

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")

# new lines
def bye(request):
    return HttpResponse("Goodbye World")

```

and ```urls.py```:

```python
from django.contrib import admin
from django.urls import path

from .views import index, bye # updated line

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('bye/', bye), # new line
]

```

Now go back to the browser and type http://127.0.0.1:8000/bye/ in the URL box and hit enter.

You'll see something like this:

![Goodbye World Page](https://github.com/sarmadgulzar/beginning-django/raw/master/images/03.png)

Now you'll start to feel this pattern that how URLs defined in ```urls.py``` are mapped to the functions in ```views.py```.

Well, that concludes our introduction to Django. Stay tuned for the next part and until then, Happy Pythoning :heart:
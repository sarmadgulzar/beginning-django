# Creating websites with [Django](http://djangoproject.com)

## Introduction:

[Django](http://djangoproject.com) is a web framework written in Python. It is a high-level framework that saves you the hassle of low-level web development so that youu can focus on what really matters instead of reinventig the wheel. On Django's website, they call it:
> *The web framework for perfectionists with deadlines.*

And that really is the case becase Django makes it super easy to create backend of your web application quickly. Python has other frameworks like [Flask](https://www.palletsprojects.com/p/flask/), [Tornado](https://www.tornadoweb.org/en/stable/) etc. but Django has gained huge amount of popularity. A few key features of Django are as follows:

- Quick prototyping
- Builtin [ORM](https://en.wikipedia.org/wiki/Object-relational_mapping) (Object Relational Mapper)
- A beautiful admin panel, out of the box
- Builtin authentication and authorization
- Powerful web forms

and many more!

Now its time to install Django on your computer.

## Installation:

I'll assume that you have [Python](https://www.python.org/) and [pip](https://pypi.org/project/pip/) install on your system and they are add to your PATH variable. Latest version of Django is `3.0.2` at the time of writing this tutorial and that's the one we are going to use.

To install Django, write this command in your terminal/prompt:
```
$ pip install django
```

If everything goes fine, you should be able to run the following commands to verify your Django installation.

```
$ python
```
```python
>>> import django
>>> django.__version__
'3.0.2'
```

Fanstastic work installing Django on your computer. Now let's go ahead and create a website using ```django-admin```. It is basically a command-line utillity used to create *django projects* and few other things. You don't have to worry too much about this, as we'll come back to this later. For now, just run the following command in terminal/prompt:

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

Now open your favorite browser and go to the following url: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

You will see a page like this:

![Django Welcome Screen](https://github.com/sarmadgulzar/beginning-django/raw/master/images/01.png)

Great work so far. Now, let me briefly explain the files in ```myproject``` folder and ```manage.py``` file.

### ```manage.py```
Just like ```django-admin```, it is a command line tool to do different things like, for example, starting a server we just did above using:

```
$ python manage.py runserver
```

Later on, we'll see many more things that we can do using ```manage.py```.

### ```myproject/__init__.py```
This empty file is just there to treat ```myproject``` folder as a *module*.

### ```myproject/settings.py```

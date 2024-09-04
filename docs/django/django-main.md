# Django Notes

## Basic Cheatsheet

*Creating a new project* :
```bash
django-admin startproject projectname
```
*Add an app to a project* :
```bash
python3 manage.py startapp appname
```
*Starting the server*
```bash
python3 manage.py runserver
```
*Creating migrations*
```bash
python3 manage.py makemigrations
```
*Migrate the database*
```bash
python3 manage.py migrate
```
*Creating a Super User for the admin panel*
```bash
python3 manage.py createsuperuser
```
*Collecting static files into one folder*
```bash
python3 manage.py collectstatic
```

## My Notes

### to turn a simple request as response  on page:
```python
from django.http import HttpResponse
Usage: return HTTPResponse('some text')
```
### to get the response within a defined template
```python
from django.shortcuts import render
Usage: return render(request, 'template_file.html', {some_dictionary})
```
### Referencing to the URLs defined in  urls.py
```html
{%  url 'name_of_the_url' %}
```
### Add the new custom app to settings.py
```python
INSTALLED_APPS = [ '<Folder Name>.<Python File Name (apps.py)>.<Class Name> ' ]
```
### Add custom app to the admin page:
```python
# (add the lines to admin.py of custom app)
from .models import <Class Name>
admin.site.register(<Class Name>)
```
### How to add staatic media files into the settings file
1- Check if MEDIA_URL and MEDIA_ROOT defined.
2- Add required libraries (in urls.py):
```python
from django.conf import settings
from django.conf.urls.static import static
```
3- Add the second line to the urlpattern (in urls.py):
```python
urlpatterns = [ ... ]
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
### Get all the objects from the databse in view.py
<sample_object>.objects
SAMPLE: 
```python
def homepage(request):
	posts = Blog.objects
	return render(request, 'blog/home.html', {'posts': posts})
```

### Make a loop for the object instances in template HTML file
```html
{% for <gany_name_for_instance> in  <sample_objects_collection>.all %}
    {{  <any_name_for_instance>.<any_attribtue_or_method_of_object> }}
{% endfor %}
```
### Taking the ID number of any object as URL part in urls.py
SAMPLE: 
```python
path('<int:post_id>', views.detail, name='blog_detail')
```
### Specify the directory of the static files uploaded or created in the repository in settings.py
```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '<relative_path_of_uploaded_files>')
]
```

### load static file in HTML templates
In the header:  
```html
{% load staticfiles %}
```
as content link in anywhere in body: 
```html
{% static '<file_name_w_extension>' %}
```

### A sample for linking to objects with aspecific ID number:
urls.py : urlpatterns : 
```python
path('<int:blog_id>', views.detail, name='blog_detail') 
```
views.py : 
```python
def homepage(request):
	posts = Blog.objects
	return render(request, 'blog/home.html', {'posts': posts})
def detail(request, blog_id):
	post_detail = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'blog/detail.html', {'post_detail': post_detail})
```
template HTML:
```html
{% for post in posts.all %}
    <a href="{% url 'blog_detail' post.id %}"><h3>{{ post.title }}</h3></a>
{% endfor %}
```

## General python notes

### Sort lists with a specific element
gets the specified element from the list and use it to sorting the list
```python
sorted([('books', 43),('papers', 8),('citations', 126)], key=operator.itemgetter(1), reverse=True)
# RETURNS:  [('citations', 126), ('books', 43), ('papers', 8)]
```
or
```python
a.sort(key=lambda elem: elem[1])
```
### Format datetime data type appearance with strftime() 
```python
<any_datetime_object>.strftime('%b %e %Y') 
# RETURNS Feb 13 2024
```
For more detail check: [ Python strftime cheatsheet ](https://strftime.org/)

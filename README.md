### DaniHomeoClinic (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)
python -m pip install Django

### Requirement
1. python == 3.9.1
2. django == 3.2


### TODO List
1. Install Apache with mod_wsgi
2. Install mysql and configure 


### To create a virtual environment in python
https://docs.python.org/3/tutorial/venv.html


### Documentation
1. https://docs.djangoproject.com/en/3.2/topics/
2. https://docs.djangoproject.com/en/3.2/intro/reusable-apps/
3. https://www.geeksforgeeks.org/django-tutorial/


### To add admin to local templates
create a directory called admin inside templates, and copy the template admin/base_site.html from within the default 
Django admin template directory in the source code of Django itself (django/contrib/admin/templates) into that directory.

Then, edit the file and replace {{ site_header|default:_('Django administration') }} (including the curly braces) with your own site’s name

# Designing the main page
1. Fetch all the items from db and returning it through a view
    from .models import Item
    def index(request):
        all_items = Items.objects.all()
        return HttpResponse(all_items) 
2. This doesn't give the data in required format. Hence, we introduce a 'templates' folder which will have all the design related files in order to showcase the data in required format
3. Create the 'templates' folder inside the 'food' app, followed by that, create a 'food' folder again which will hold all the files. ie. food\templates\food\index.html
4. Import the templates in views.py as : (uses Django Template)
    from django.template import loader
    def index(request):
        all_items = Item.objects.all()
        template = loader.get_template('food/index.html')
        context = {'all_items':all_items}
        return HttpResponse(template.render(context, request))
    
    Basically, we are passing the data to be fed to html file in the 'context' and pass it as parameter to template.render() in order to utilize those elements

# DJANGO TEMPLATE LANGUAGE
5. The passed elements can be utilized in html as: (DJANGO TEMPLATE LANGUAGE)
    Example:
    {% for item in all_items %}
        <ul>
            <li>
                {{item.item_name}}
            </li>
        </ul>
    {% endfor %}
6. Instead of rendering template separately, it can be done alternately as:
    from django.shortcuts import render
    def index(request):
        all_items = Item.objects.all()
        context = {'all_items':all_items}
        return render(request, 'food/index.html', context)
7. Detailed view and respective URL pattern:
   Example:
   url pattern --> path("<int:item_id>", views.details, name='details')
   detailed view -->
   def details(request, item_id):
    return HttpResponse("This is item id: %s" % item_id)
8. DTL:
    To render the templates in Django app, we need something called as 'Templating Engine'. Eg. Django Templating Engine, Jinja2
    Default Django engine - DTL
    Variable -> {{ var1 }}
    Control flows/ tags -> {% for i in item %} ... {% endfor %}

# Removing the hardcoded url in HTML files:
9. Refer to the name of the url in urls.py file and replace it with hardcoded urls
    Eg. "/food/{{item.item_id}}" -----> "{% url 'details' item.id %}" in a href parameter
    Don't miss the quotes around the name and the parameter to pass

# Namespaces:
10. In a project, if many apps has same name in the urls, there can be confusion on which one to address while the name is called.
    To solve this, 
    In current app urls.py, add the line as 'app_name="food"'
    Then, whenever you refer the urls from this app, then give it as: "{% url 'food:details' item.id %}" in a href parameter

# Adding static files:
11. Adding the style sheet in the html file by adding the below line in head section:
    {% load static %} --> Django 3.0 or more
    <link rel="stylesheet" href="{% static 'food/images/style.css' %}">
    This points to the style.css file in food/static/food/images/style.css
12. If the style sheet is still not rendered, add the following lines in settings.py:
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    VENV_PATH = os.path.dirname(BASE_DIR)
    STATIC_ROOT = os.path.join(VENV_PATH, 'static_root')
13. Add the bootstrap ref as:
    Reference: https://getbootstrap.com/docs/5.3/getting-started/download/
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>

# Adding base template:
14. Create a base template file with navbar code in it so that it can be added to all pages
    This will contain {% block body %} and {% endblock %}

# Adding Forms:
15. Create a forms.py file
    from django import forms
    from .models import Item  --> the model for which the form is created

    class ItemForm(forms.ModelForm):
        class Meta:
            model - Item --> which model
            fields = ['item_name', 'item_desc', 'item_price', 'item_image']
16. Adding a respective view:
    def create_item(request):
        form = ItemForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('food:index')
        return render(request, 'food/create_item.html', {'form':form})
17. We always add {% csrf_token %} tag in html whenever we deal with forms
18. Basically, whenever there arises a need for forms, we create a template class for that form in forms.py with the help of any models if required, and then we import that form template into views.py to play with it and send it for rendering later  
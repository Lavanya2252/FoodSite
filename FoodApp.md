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
5. The passed elements can be utilized in html as:
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
# Dealing with Authentication
1. We always add {% csrf_token %} tag in html whenever we deal with forms
2. Basically, whenever there arises a need for forms, we create a template class for that form in forms.py with the help of any models if required, and then we import that form template into views.py to play with it and send it for rendering later
3. Django already has inbuilt forms which we can use for user registration
    Example:
    from django.contrib.auth.forms import UserCreationForm
    def register(request):
        form = UserCreationForm()
        return render(request, 'users/register.html', {'form':form})
4. Forms wont have default submit buttons
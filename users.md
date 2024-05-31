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
5. If we want to modify those inbuilt forms, like adding email field, we can import it in forms.py and modify it according to our requirements

# Handling inbuilt views for Login Functionality:
6. Whenever we try to access a classbased view, we mention it as 'views.method.as_view()'
    Eg. from django.contrib.auth import views as auth_views
    pattern = 'login/', auth_views.LoginView.as_view(), name='login'
7. In the above example, we are referring to a view which is inbuilt. To specify a template for that, we use a parameter called 'template_name'
    Eg. from django.contrib.auth import views as auth_views
    pattern = 'login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login' 
8. Once on entering the login credentials, we need to redirect it to specific page as we didn't define a custom view for it. This can be done it settings.py as:
    Eg. LOGIN_REDIRECT_URL = 'food:index'
9. Redirecting registered users to login page: the login url is defined under the default app. hence, we can give the url as usual: ie. return redirect('login') in views.py as current app
10. To check if the user is logged in or not: we can use the 'user' variable of django as follows:
    {% if user.is_authenticated %}
        Do something
    {% else %}
        Logout
    {% endif %}
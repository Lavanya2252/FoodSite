from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout


def register(request):
    # REFER CREATE ITEM IN FOOD APP FOR OTHER TYPE OF HANDLING IT 
    # ie. Form will take the parameter as 'request.POST or None' instead of if/else scenario
    if request.method == "POST":
        # form = UserCreationForm(request.POST) # takes the user data and processes it on clicking 'Submit'
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, Your account is created successfully!')
            form.save()
            # return redirect('food:index')
            return redirect('login')
    else:
        # form = UserCreationForm() # else returns empty form for user to fill details
        form = RegisterForm(request.POST)
    return render(request, 'users/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request,'users/loggedout.html' , {})
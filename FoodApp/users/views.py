from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    # REFER CREATE ITEM IN FOOD APP FOR OTHER TYPE OF HANDLING IT 
    # ie. Form will take the parameter as 'request.POST or None' instead of if/else scenario
    if request.method == "POST":
        form = UserCreationForm(request.POST) # takes the user data and processes it on clicking 'Submit'
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, Your account is created successfully!')
            form.save()
            return redirect('food:index')
    else:
        form = UserCreationForm() # else returns empty form for user to fill details
    return render(request, 'users/register.html', {'form': form})

def signin(request):
    form = {}
    return render(request, 'users/signin.html', {'form': form})
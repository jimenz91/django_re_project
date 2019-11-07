from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def register(request):
    """User register logic."""
    if request.method == 'POST':
        # Get form values and assign them to variables.
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if both passwords supplied match.
        if password == password2:
            # Check if username already exists in DB. If it does, return to the register page and inform the user.
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                # Check if email already exists in DB. If it does, return to the register page and inform the user.
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    # Creating the user in the DB with the information supplied.
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')
                    user.save()
                    messages.success(
                        request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            # Error for passwords that don't match.
            messages.error(request, "Passwords don't match")
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    """User login logic."""
    # Check the request for the post method with the login information.
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate user
        user = auth.authenticate(username=username, password=password)
        # If the user exists in the DB, perform log in.
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            # If not, indicate that the credentials are incorrect.
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    """User logout"""
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import myForm
from .models import myModel


# Handles user login authentication and redirects to home page on success
def log_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Incorrect username or password.")
            return redirect('log_in')
    else:
        return render(request, 'login.html', {})

# Logs out the current user and redirects to login page
def log_out(request):
    logout(request)
    messages.success(request, "You were logged out")
    return redirect('log_in')

# Creates a new user account with validation for matching passwords and unique username/email
def sign_up(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        
        if password != password_confirm:
            messages.error(request, "Passwords do not match")
            return redirect('signup')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('signup')
        
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('log_in')
    else:
        return render(request, 'signup.html', {})

# Displays the main dashboard with all requests if user is authenticated
def home(request):
    if request.user.is_authenticated:
        person_details = myModel.objects.all()
        return render(request, 'dashboard.html', {'person_details': person_details})
    else:
        return redirect('log_in')

# Displays form to submit a new request and saves it to the database
def request(request):
    success = False
    new_data = ''

    if request.method == "GET":
        form = myForm()
        
    else:
        form = myForm(request.POST)
        
        if form.is_valid():
            success = True
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            quote_text = form.cleaned_data['quote_text']
            category = form.cleaned_data['category']
            additional_details = form.cleaned_data['additional_details']
            success = True
            new_data = form.cleaned_data
            form.save()
            
        
    return render(request, 'request.html', {'form': form, 'success': success, 'new_data': new_data})

# Allows editing of an existing request by ID and saves changes to database
def edit(request, model_id):
    person_detail = myModel.objects.get(id=model_id)
    form = myForm(request.POST or None, instance=person_detail)
    success = False
    if form.is_valid():
        success = True
        form.save()
        messages.success(request, "Request updated successfully")
        return redirect('home')
    return render(request, 'edit.html', {'form': form, 'success': success, 'person_detail': person_detail})

# Deletes a request from the database by ID and redirects to home
def delete(request, model_id):
    person_detail = myModel.objects.get(id=model_id)
    person_detail.delete()
    messages.success(request, "Request deleted successfully")
    return redirect('home')

# Admin-only dashboard that displays all requests with statistics (requires superuser access)
def admin_dashboard(request):
    if not request.user.is_authenticated:
        messages.error(request, "Please log in to access this page")
        return redirect('log_in')
    
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission to access the admin page")
        return redirect('home')
    
    person_details = myModel.objects.all()
    total_requests = person_details.count()
    
    return render(request, 'admin-dashboard.html', {'person_details': person_details, 'total_requests': total_requests})
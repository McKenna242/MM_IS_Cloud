from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserForm, EmailForm

# Create your views here.

@login_required
def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('file')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })
    
#form to update user info uses auto_fill_form
@login_required   
def update(request):
    customer=User.objects.get(id=request.user.id)

    
    if request.method == 'POST':
        form = UserForm(request.POST, instance = request.user)
        if form.is_valid():
            update = form.save(commit = False)
            update.user = request.user
            update.save()
            return redirect('home')
    else:
        form = UserForm(data=request.POST, instance=customer)
    #return render(request, 'registration/user_update.html', {
    return auto_fill_form(request)
        #'form': form
    #})
#form to auto fill user info when changing in user dashboard
def auto_fill_form(request):
    
    form = UserForm(initial = dict(
        first_name = request.user.first_name, 
        last_name = request.user.last_name, 
        email = request.user.email))
    
    context = dict(form=form)
    return render(request, "registration/user_update.html", context) 


def update_email(request):
    
    customer=User.objects.get(id=request.user.id)

    if request.method == 'POST':
        form = EmailForm(request.POST, instance = request.user)
        if form.is_valid():
            update = form.save(commit = False)
            update.user = request.user
            update.save()
            return redirect('home')
    
    else:
        form = EmailForm(data=request.POST, instance=customer)
        
    return render(request, 'registration/user_update-email.html', {
    #return auto_fill_form(request)
        'form': form
    })


  
def secret_page(request):
    return render(request, 'secret_page.html')
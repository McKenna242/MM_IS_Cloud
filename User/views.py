from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserForm, EmailForm, GroupForm, InviteForm
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .models import Member, Group, ChangeEmail
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django_email_verification import send_email
from django.http import HttpResponse
from django.template.loader import get_template
from django.utils.html import strip_tags

# Create your views here.

@login_required
def home(request):
    count = User.objects.count()
    user = User.objects.all()
    groups = Group.objects.all()
    member = Member.objects.all()
    currentUser = request.user
    context = {'count':count, 'users':user, 'group':groups, 'member':member, 'currentUser':currentUser }
    return render(request, 'home.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            send_email(user)

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
    
    user=User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = EmailForm(request.POST, instance = request.user)
        if form.is_valid():
            email = form.cleaned_data['email']
            newEmail = ChangeEmail.objects.create(User = user, newEmail = email)
            context = {'user': user, 'newEmail': newEmail}
            html = render_to_string('registration/email_change_email.html', context)
            plain_message = strip_tags(html)
            send_mail(
                'Email Change Request',
                plain_message,
                'webmaster@olacloudstorage.com',
                [email],
                fail_silently=False,
                )
            
            return redirect('home')
    
    else:
        form = EmailForm(data=request.POST, instance=user)
        
    return render(request, 'registration/user_update-email.html', {
    #return auto_fill_form(request)
        'form': form
    })
def chage_email_page(request, pk):
    
    email=ChangeEmail.objects.get(id=pk)
    user = request.user

    context = {'user':user, 'email':email}
    #user=User.objects.get(id=request.user.id)
    if request.method == 'POST':
        user.email = email.newEmail
        user.save()
        ChangeEmail.objects.filter(User_id = user.id).delete()
        return redirect('home')
        
        
    return render(request, 'registration/change_email_page.html', context )
    
    
def invite(request, group_id):

    #group = Group.objects.get(id=request.group.id)
    group = Group.objects.get(id=group_id)
    members = Member.objects.all()
    
    if request.method == 'POST':
        form = InviteForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['users']
            print(user.id)
            newMember = Member.objects.create(member = user, groups = group, invited = True, accepted = False)
            newMember.save()   
            #update.user = request.user
            #return redirect('home')
    else:
        form = InviteForm(data=request.POST)
      
    context = {'form': form, 'group':group, 'members':members}
       
    return render(request, 'invite.html', context)
    #return render(request, 'registration/user_update.html', {

def create_group(request):
    
    customer=User.objects.get(id=request.user.id)
    user = request.user

    if request.method == 'POST':
        form = GroupForm(request.POST) 
        if form.is_valid():
            group = form.save(commit = False)
            group.groupCreator = request.user
            groupName = form.cleaned_data.get("groupName")
            group.save()
            newMember = Member.objects.create(member = user, groups = group, accepted = True, invited = True)
            newMember.save()   
            return redirect('home')
    
    else:
        form = GroupForm(data=request.POST, instance=customer)
        
    return render(request, 'create_group.html', {
    #return auto_fill_form(request)
        'form': form
    })

def group_dashboard(request, pk):
    
    group = Group.objects.get(id=pk)
    users = User.objects.all()
    user = request.user
    members = Member.objects.filter(groups=group)
    context = {'group':group,'users':users, 'members':members}
    
    if request.method == 'POST':
        newMember = Member.objects.create(member = user, groups = group)
        newMember.save()   

    
    
    return render(request, 'group_dashboard.html', context)
    
def accept_invite(request, group_id):
    
    #file = fileStorageSchema.objects.get(id=pk)
    group = Group.objects.get(id=group_id)
    user = request.user
    member = Member.objects.get(member=user.id, groups = group_id)
    if request.method == "POST":
        member.accepted = True
        member.save()
        return redirect('/dashboard/')
    
    context = {'group':group }
    return render(request, 'accept_invite.html', context)
    
    
def secret_page(request):
    return render(request, 'secret_page.html')
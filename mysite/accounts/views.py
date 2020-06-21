from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, LoginForm
from .decorators import authenticated_user
from django.contrib import messages
from django.contrib.auth.models import Group, User
# Create your views here.

def check_username(request, username):
    user_model = CreateUserForm(request.POST) # your way of getting the User
    try:
        user_model.objects.get(username__iexact=username)
    except user_model.DoesNotExist:
        return username
    raise forms.ValidationError(_("This username has already existed."))

@authenticated_user
def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            patient_group = Group.objects.get(name='patient')
            patient_group.user_set.add(user)
            login(request, user)
            return redirect('drview:homepage')

    form = CreateUserForm()
    return render(request=request,
                  template_name='registration/register.html',
                  context={'form': form, 'page_name':'Register'})

@authenticated_user
def userLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            groups = request.user.groups.all()
            if any(role.name == 'doctor' for role in groups):
                return redirect('drview:homepage')
            elif any(role.name == 'patient' for role in groups):
                return redirect('patientview:homepage')
            else:
                return redirect('testsite:test')
        else:
            messages.error(request, 'Login failed. Please try again.', extra_tags='alert-info')
            return redirect('accounts:login')

    form = LoginForm()
    return render(request=request,
                    template_name='registration/login.html',
                    context={'form': form, 'page_name': 'Login'})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.', extra_tags='alert-success')
    return redirect('accounts:login')
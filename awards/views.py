from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from .forms import *
from django.http import Http404

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', locals())

@login_required(login_url='/accounts/login')
def home(request):
    current_user = request.user
    all_projects = Projects.objects.all()
    return render(request, 'index.html', locals())


@login_required(login_url='/accounts/login')
def project(request, project_id):
    try:
        project = Projects.objects.get(id=project_id)
    except Projects.DoesNotExist:
        raise Http404()
    return render(request, "project.html", locals())


@login_required(login_url='/accounts/login')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UploadForm()
        my_projects = Projects.objects.filter(owner=current_user)
        my_profile = Profile.objects.get(user_id=current_user)
    return render(request, 'profile.html', locals())


@login_required(login_url='/accounts/login')
def upload_form(request):
    current_user = request.user
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.uploaded_by = current_user
            image.save()
            return redirect('home')
    else:
        form = UploadForm()
    return render(request, 'post.html', {'uploadform': form})

@login_required(login_url='/accounts/login')
def edit_prof(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            lol = form.save(commit=False)
            lol.uploaded_by = current_user
            lol.save()
            return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'profile_edit.html', {'profileform': form})



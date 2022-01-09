from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import (redirect, render, get_object_or_404, get_list_or_404, HttpResponseRedirect)
from .models import Project
from .forms import ProjectForm
# Create your views here.

@login_required
def project_home_view(request):
    return redirect("/projects/list")
    # return render(request, 'home.html', {})

@login_required
def project_list_view(request):
    user = request.user;
    if(user.is_authenticated):
        query_set = {}
        if(user.is_staff):
            query_set = Project.objects.all()
        else:
            query_set = get_list_or_404(Project, user_id=user.username) #Project.objects.all()

        context = {
            'project_list': query_set
        }
        return render(request, 'projects/project_list.html', context)
    else:
        messages.success(request, ("You are not authrized to access this page!!"))
        return redirect("/users/login")

@login_required
def project_edit_view(request, project_id):
    projectObj = get_object_or_404(Project, id=project_id);
    form = ProjectForm(request.POST or None, instance=projectObj);
    if form.is_valid():
        form.save();
        return HttpResponseRedirect("/projects/list")
    context = {
        'project_form': form
    }
    return render(request, 'projects/project_edit.html', context)

@login_required
def project_detail_view(request, project_id):
    projectObj = get_object_or_404(Project, id=project_id);
    context = {
        'projectObj': projectObj
    }
    return render(request, 'projects/project_detail.html', context)

@login_required
def project_add_view(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        uncommited_form = form.save(commit=False)
        uncommited_form.user_id = request.user.username
        uncommited_form.save()
        return HttpResponseRedirect("/projects/list")

    context = {
        'project_form': form
    }
    return render(request, 'projects/project_add.html', context)

@login_required
def project_delete_view(request, project_id):
    projectObj = get_object_or_404(Project, id=project_id);
    if request.method == "POST":
        projectObj.delete();
        return HttpResponseRedirect("/projects/list")
    context = {
        'project': projectObj
    }
    return render(request, 'projects/project_delete.html', context)
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Project
from django.contrib import messages

def projects_list(request):
    all_projects = Project.objects.all()
    return render(request, 'index.html', {'all_projects': all_projects})


def new(request):
    return render(request, 'add_project.html')


def add_project(request):
    if request.method == 'POST':
        title = request.POST['title']
        technology_used = request.POST['technology_used']
        deployed_link = request.POST['deployed_link']

        # Create a new Project instance
        project = Project.objects.create(
            title=title,
            technology_used=technology_used,
            deployed_link=deployed_link
        )
        project.save()

        messages.success(request, 'Project added successfully!')
        return redirect('projects_list')

    return render(request, 'add_project.html')



def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})

def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.title = request.POST['title']
        project.technology_used = request.POST['technology_used']
        project.deployed_link = request.POST['deployed_link']
        project.save()
        messages.success(request, 'Project updated successfully!')
        return redirect('projects_list')
    return render(request, 'edit_project.html', {'project': project})


def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully!')
        return redirect('projects_list')
    return HttpResponse(status=405)  # Method Not Allowed if not POST

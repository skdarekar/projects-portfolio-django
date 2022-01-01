from django.shortcuts import render

# Create your views here.
def project_home_view(request):
    return render(request, 'projects/project_list.html', {})
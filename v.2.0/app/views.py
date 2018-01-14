from django.shortcuts import render

# Create your views here.

def users_list(request):
    return render(request, 'app/users_list.html', {})
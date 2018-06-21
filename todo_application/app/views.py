from django.shortcuts import render
from .models import todo
# Create your views here.

def todo_view(request)  :

    data = todo.objects.all()

    return render(request,'todo_details.html',{'todo_data':data})


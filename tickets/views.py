from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request,'tickets/index.html')

def add_tickets(request):
    return render(request,'tickets/add_tickets.html')

import pdb
from django.shortcuts import render,redirect
from .models import Ticket , Intitulé
from django.contrib.auth.decorators import login_required
from django.contrib import  messages
from django.core.paginator import Paginator

 # Create your views here.

 
@login_required(login_url='/authentication/login')

def index(request):
    tickets=Ticket.objects.filter(owner=request.user)
    paginator = Paginator(tickets, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context = {
      'tickets' : tickets,
      'page_obj' : page_obj
    }
    return render(request, 'tickets/index.html' , context)

@login_required(login_url='/authentication/login')
def add_tickets(request):
   # intitulé = intitulé.objects.all()
    context = { 
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'tickets/add_tickets.html', context)
    if request.method == 'POST':
       # import pdb 
        # pdb.set_trace
        intitulé = request.POST['intitulé']
        

        if not intitulé:
          messages.error(request, 'Veuillez introduire intitulé de la tâche svp')
          return render(request, 'tickets/add_tickets.html',context ) 

        description = request.POST['description']
        info = request.POST['info']
        date = request.POST['ticket_date']
        
        if not description:
            messages.error(request, 'description is required')
            return render(request, 'tickets/add_tickets.html', context)

        if not date:
            messages.error(request, 'deadline is required')
            return render(request, 'tickets/add_tickets.html', context)    
        
        
        Ticket.objects.create(owner=request.user, intitulé=intitulé, info=info,date=date,
                                 description=description)
        messages.success(request, 'Ticket saved successfully')
    
        return redirect('tickets')




@login_required(login_url='/authentication/login')
def tickets_edit(request,id):
    tickets = Ticket.objects.get(pk=id)
    intitulé = Intitulé.objects.all()
    context = {
        'tickets': tickets,
        'values': tickets,
     }
    if request.method == 'GET':
        return render(request, 'tickets/edit-tickets.html', context)
    if request.method == 'POST':
        intitulé = request.POST['intitulé']

        if not intitulé:
            messages.error(request, 'intitulé is required')
            return render(request, 'tickets/edit-tickets.html', context)
        description = request.POST['description']
        date = request.POST['tickets_date']
        intitulé = request.POST['intitulé']
        info = request.POST['info']

        if not description:
            messages.error(request, 'description is required')
            return render(request, 'tickets/edit-tickets.html', context)

        tickets.owner = request.user
        tickets.intitulé = intitulé
        tickets. date = date
        tickets.info = info
        tickets.description = description

        tickets.save()
        messages.success(request, 'tickets updated  successfully')

        return redirect('tickets')



def delete_tickets(request, id):
    tickets = Ticket.objects.get(pk=id)
    tickets.delete()
    messages.success(request, 'Ticket removed')
    return redirect('tickets')

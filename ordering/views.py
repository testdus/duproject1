from django.shortcuts import render, redirect
from .models import OrderTable
from pizzas.models import Pizza, Topping
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    """The home page for Ordering
    with forms"""
    pizza = Pizza.objects.order_by('date_added')

    context = {'pizza': pizza, 'error':request.GET.get('error')}
    return render(request, 'ordering/index.html', context)

@csrf_exempt
def getToppings(request,pizza_id):
    topping = Topping.objects.filter(pizza_id=pizza_id).values('id', 'name')
    return HttpResponse(json.dumps(list(topping)))

@csrf_exempt
def saveView(request):
    if request.POST['qty'] !="":
        save_table = OrderTable().saveOrder(request.POST['qty'], request.POST['pizza_id'], request.POST['topping_id'])
        context = {'message': save_table}
        return render(request, 'ordering/confirmation.html', context)
    else:
        error = 'Some of the required fields are missing'
        return redirect('/ordering/?error=%s' % error)
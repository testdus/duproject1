from django.db import models
from pizzas.models import Pizza, Topping

# Create your models here.

class OrderTable(models.Model):
    """Order"""
    pizza = models.ForeignKey(Pizza)
    toppings = models.ForeignKey(Topping)
    quantity = models.IntegerField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(max_length=200)

    def saveOrder(self, qty, pizza_id, topping_id):
        price = (Pizza.objects.values('price').filter(id=pizza_id))[0]['price']
        total_amt = int(qty) * price
        order_table = OrderTable(quantity=qty, pizza_id=pizza_id, toppings=Topping(pk=topping_id), amount=total_amt)
        order_table.save()
        if self.pk == None:
            return {'price': total_amt, 'qty': qty, 'message': 'Success'}
        else:
            return {'price': total_amt, 'qty': qty, 'message': 'Failed'}
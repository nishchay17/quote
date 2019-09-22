from django.shortcuts import render
from .models import quotes
import random

def show(request):
    id = quotes.objects.count()
    rand_id = random.randint(1, id)
    quotes_data = quotes.objects.get(pk = rand_id) 
    content = { 'quotes' : quotes_data }
    return render(request, 'show.html' , content) 



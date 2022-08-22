from django.shortcuts import render
from .models import Mytodo

# Create your views here.
def alltodos(request):
    return render(request, 'alltodo.html', {})

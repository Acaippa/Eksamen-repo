from django.shortcuts import render
from .models import Laptop

# Create your views here.
def home_view(request):
    # Prosseser index.html med alle laptoppene som context.
    return render(request, "index.html", {"laptops" : Laptop.objects.all()}) # SELECT * FROM Laptop
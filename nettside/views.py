from django.shortcuts import render
from .models import Laptop
from .forms import LaptopForm

# Create your views here.
def home_view(request):
    form = LaptopForm()

    if request.method == "POST":
        form = LaptopForm(request.POST)

        if form.is_valid():
            form.save()
            form = LaptopForm()

    # Prosseser index.html med alle laptoppene som context.
    return render(request, "index.html", {"laptops" : Laptop.objects.all(), "form" : form}) # SELECT * FROM Laptop



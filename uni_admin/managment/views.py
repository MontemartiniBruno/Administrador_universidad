from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'managment/index.html')

def inicio(request):
    return render(request, 'managment/inicio.html')

def contact(request):
    return render(request, 'managment/form.html')
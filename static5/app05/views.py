from django.shortcuts import render

# Create your views here.
def home(request):
    info="my name is Gloria"
    return render(request,"index.html",{"info": info})
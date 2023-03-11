from django.shortcuts import render
def paginainicio (request):
     return render(request,"index.html")
def formcar(request):
    return render (request,"carap/basevehiculo.html")

def formpil(request):
    return render (request,"carap/datospiloto.html")

def formganador(request):
    return render(request,"carap/baseganadores.html")


     

 

from django.shortcuts import render, redirect
from .forms import Formulario
from django.core.mail import EmailMessage

# Create your views here.
def contacto(request):
    formulario_contacto=Formulario(request.POST)
    if request.method == "POST":
        formulario_contacto=Formulario(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            
            email=EmailMessage("Contaduria", 
                               "El usuario con nombre {} con la dirección {} te escribe lo siguiente: \n\n {}".format(nombre,email,contenido),"", ["comanuel7@gmail.com"],reply_to=[email])
            
            try:
                email.send()
                
                return redirect("/contacto/?valido")
            except:
                
                return redirect("/contacto/?fail")
                
                        

            
        
    
    
    return render(request, "contacto/contacto.html", {'miFormulario':formulario_contacto})


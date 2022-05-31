from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from familia.models import Persona
from django.template import loader
from familia.forms import PersonaForm, BuscarPersonaForm

def index(request):
    personas = Persona.objects.all()
    template = loader.get_template('familia/lista_familiares.html')
    context = {
        'personas': personas,
    }
    return HttpResponse(template.render(context, request))


def agregar(request):
  

    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            altura = form.cleaned_data['altura']
            
            Persona(nombre=nombre, email=email, fecha_nacimiento=fecha_nacimiento, altura=altura).save()

            return HttpResponseRedirect("/familia")
    
    elif request.method == "GET":
        form = PersonaForm()
    else:
        return HttpResponseBadRequest("Error no se reconoce el método.")

    
    return render(request, 'familia/form_carga.html', {'form': form})


def borrar(request, identificador):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue eliminada con éxito        
    '''
    if request.method == "GET":
        persona = Persona.objects.filter(id=int(identificador)).first()
        if persona:
            persona.delete()
        return HttpResponseRedirect("/familia/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")


def actualizar(request, identificador):
   
    pass


def buscar(request):
    if request.method == "GET":
        form_busqueda = BuscarPersonaForm()
        return render(request, 'familia/form_busqueda.html', {"form_busqueda": form_busqueda})

    elif request.method == "POST":
        form_busqueda = BuscarPersonaForm(request.POST)
        if form_busqueda.is_valid():
            palabra_a_buscar = form_busqueda.cleaned_data['palabra_a_buscar']
            personas = Persona.objects.filter(nombre__icontains=palabra_a_buscar)

        return  render(request, 'familia/lista_familiares.html', {"personas": personas})
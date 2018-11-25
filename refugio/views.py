from django.shortcuts import render
from django.http import HttpResponse
from refugio.models import Tipo, Mascota,Adoptante
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required

from django.views.generic.edit import UpdateView, CreateView, DeleteView 
from rest_framework import viewsets
from .serializer import TipoSerializer, MascotaSerializer, AdoptanteSerializer
from django.contrib.auth.models import User



def first_view(request):
    return render(request, 'base.html') 

#Tipo
@login_required()
def tipo( request):
    tipo_list = Tipo.objects.all()
    context = {'object_list': tipo_list}
    return render(request, 'refugio/tipo.html', context)

@login_required()
def tipo_detail(request, tipo_id):
    tipo = Tipo.objects.get(id=tipo_id)
    context = {'object': tipo}
    return render(request, 'refugio/tipo_detail.html', context)

#Mascota
@method_decorator(login_required, name='dispatch')
class MascotaListView(ListView):
    model = Mascota


@method_decorator(login_required, name='dispatch')
class MascotaDetailView(DetailView):
    model = Mascota
 
@method_decorator(login_required, name='dispatch')
class MascotaUpdate(UpdateView):
    model = Mascota
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class MascotaCreate(CreateView):
    model = Mascota
    fields = '__all__'
	
@method_decorator(login_required, name='dispatch')
class MascotaDelete(DeleteView):
    model = Mascota
    success_url = reverse_lazy('mascota-list')

#Adoptante
@method_decorator(login_required, name='dispatch')
class AdoptanteListView(ListView):
    model = Adoptante

@method_decorator(login_required, name='dispatch')
class AdoptanteDetailView(DetailView):
    model = Adoptante
 
@method_decorator(login_required, name='dispatch')
class AdoptanteUpdate(UpdateView):
    model = Adoptante
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class AdoptanteCreate(CreateView):
    model = Adoptante
    fields = '__all__'
	
@method_decorator(login_required, name='dispatch')
class AdoptanteDelete(DeleteView):
    model = Adoptante
    success_url = reverse_lazy('adoptante-list')

class TipoList(viewsets.ModelViewSet):
	queryset=Tipo.objects.all()
	serializer_class=TipoSerializer

class MascotaList(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

class AdoptanteList(viewsets.ModelViewSet):
    queryset = Adoptante.objects.all()
    serializer_class = AdoptanteSerializer

@login_required()
def base(request):
    return render(request, 'base.html')




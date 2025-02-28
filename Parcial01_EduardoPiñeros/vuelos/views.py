from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView
from django.views import View
from django import forms
from .models import Flight
from django.core.exceptions import ValidationError

# Create your views here.
class InitialView(TemplateView):
    template_name = 'vuelos/index.html'

class FlightForm(forms.ModelForm):
    class Meta:
        model=Flight
        fields =['name','tipo','price']
    def clean_price(self):
        data = self.cleaned_data.get('price')
        if data <= 0:
            raise ValidationError("Price can't be negative")
        return data
class RegistrarView(View):
    template_name = 'vuelos/registrar.html'

    def get(self,request):
        form = FlightForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)
    def post(self,request):
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('initial_view')
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)
class ListarView(ListView):
    template_name = 'vuelos/listar.html'
    model = Flight
    context_object_name = 'flights'
    ordering = ['price']
class EstadisticaView(View):
    template_name = 'vuelos/estadisticas.html'
    def get(self,request):
        vuelos_nacionales = Flight.objects.filter(tipo='Nacional')
        vuelos_internacionales = Flight.objects.filter(tipo='Internacional')
        vuelos_nacionales_count = vuelos_nacionales.count()
        vuelos_internacionales_count = vuelos_internacionales.count()
        sumNa = 0
        for vuelo in vuelos_nacionales:
            sumNa += vuelo.price
        promNa = sumNa/vuelos_nacionales.count()
        sumIn = 0
        for vuelo in vuelos_internacionales:
            sumIn += vuelo.price
        promIn = sumIn/vuelos_internacionales.count()
        viewData= {
            'Nacionales': vuelos_nacionales_count,
            'Internacionales': vuelos_internacionales_count,
            'promNa': promNa,
            'promIn':promIn
        }
        return render(request, self.template_name, viewData)
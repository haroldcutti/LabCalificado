from django.shortcuts import render, redirect
from django.views import View
from .models import Prestamo
from django.utils import timezone
from .forms import EditarPrestamoForm 

class ListaPrestamosView(View):
    def get(self, request):
        search_query = request.GET.get('search', '') 
        prestamos = Prestamo.objects.filter(fecdevolucion__isnull=True)

        if search_query:
            prestamos = prestamos.filter(libro__titulo__icontains=search_query)

        return render(request, 'lab08/lista_prestamos.html', {'prestamos': prestamos, 'search_query': search_query})

class FinalizarPrestamoView(View):
    def post(self, request, prestamo_id):
        prestamo = Prestamo.objects.get(pk=prestamo_id)
        prestamo.fecdevolucion = timezone.now()
        prestamo.save()
        return redirect('lista_prestamos')

class EditarPrestamoView(View):
    def get(self, request, prestamo_id):
        prestamo = Prestamo.objects.get(pk=prestamo_id)
        form = EditarPrestamoForm(instance=prestamo)
        return render(request, 'lab08/editar_prestamo.html', {'form': form, 'prestamo': prestamo})

    def post(self, request, prestamo_id):
        prestamo = Prestamo.objects.get(pk=prestamo_id)
        form = EditarPrestamoForm(request.POST, instance=prestamo)
        if form.is_valid():
            form.save()
            return redirect('lista_prestamos')
        return render(request, 'lab08/editar_prestamo.html', {'form': form, 'prestamo': prestamo})
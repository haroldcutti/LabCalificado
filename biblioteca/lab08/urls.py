from django.urls import path
from .views import EditarPrestamoView, ListaPrestamosView, FinalizarPrestamoView

urlpatterns = [
    path('prestamos/', ListaPrestamosView.as_view(), name='lista_prestamos'),
    path('prestamo/finalizar/<int:prestamo_id>/', FinalizarPrestamoView.as_view(), name='finalizar_prestamo'),
    path('prestamo/editar/<int:prestamo_id>/', EditarPrestamoView.as_view(), name='editar_prestamo'),

]

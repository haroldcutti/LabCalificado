from django.contrib import admin
from .models import Autor, Libro, Usuario, Prestamo

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'nacionalidad']

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'isbn', 'editorial', 'numpags']

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['numusuario', 'nif', 'nombre', 'direccion', 'telefono']

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ['libro', 'usuario', 'fecprestamo', 'fecdevolucion']


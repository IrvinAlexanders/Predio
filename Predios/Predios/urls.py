from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('Home.urls', 'inicio'), namespace='inicio')),    
    path('Cliente/', include(('Clients.urls', 'Cliente'), namespace='Persona')),
    path('Predio/', include(('Predio.urls', 'Predio'), namespace='Predio')),
    path('Propietario/', include(('Owner.urls', 'Propietario'), namespace='Propietario')),
    path('Busqueda/', include(('Query.urls', 'Consulta'), namespace='Consulta')),
   
    
]
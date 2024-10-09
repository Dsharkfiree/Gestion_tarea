from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tareas/', include('tareas.urls')),
    path('', lambda request: HttpResponseRedirect('/tareas/')),  # Redirige la raíz a /tareas/
]

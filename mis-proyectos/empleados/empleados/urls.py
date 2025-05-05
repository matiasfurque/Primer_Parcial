
from django.contrib import admin
from django.urls import path
from aplications.empleado.views import IndexView, PruebaListView, ModeloPruebaListView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', IndexView.as_view()),
    path('lista/', PruebaListView.as_view()),
    path('lista-prueba/', ModeloPruebaListView.as_view()),
]

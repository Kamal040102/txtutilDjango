from django.contrib import admin
from django.urls import path
from polls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('utility', views.utility, name='utility'),
    path('solution', views.solution, name='solution')
]

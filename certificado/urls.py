from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(template_name='login.html') ,name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('generar', views.generar, name='generar'),
    path('historial', views.historial, name='historial'),
    path('pdf', views.pdf, name='pdf' ),
    path('ver/', views.ver, name='ver'),
]
    
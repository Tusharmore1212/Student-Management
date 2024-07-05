from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('add/', views.add_std, name='add_std'),
    path('add_image/',views.add_image),
    path('delete_std/<int:roll>/', views.delete, name='delete_std'),
    path('update_std/<int:roll>/', views.update, name='update_std'),
    path('do_update_std/<int:roll>/', views.do_update, name='do_update_std'),
]

from django.urls import path
from main import views
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact_page, name='contact'),
    path('about/', views.about_page, name='about'),
    path('appointment/', views.appointment_page, name='appointment'),
    path('price/', views.price_page, name='price'),
    path('service/', views.service_page, name='service'),
    path('team/', views.team_page, name='team'),
    path('testimonial/', views.testimonial_page, name='testimonial'),

]

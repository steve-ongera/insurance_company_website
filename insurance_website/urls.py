from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('blog/', views.blog_view, name='blog'),
    path('contact/', views.contact_view, name='contact'),
    path('faq/', views.faq_view, name='faq'),
    path('features/', views.feature_view, name='features'),
     path('services/', views.service_view, name='services'),
    path('team/', views.team_view, name='team'),
    path('testimonials/', views.testimonial_view, name='testimonials'),
    
]


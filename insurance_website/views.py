from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def blog_view(request):
    return render(request, 'blog.html')

def contact_view(request):
    return render(request, 'contact.html')

def faq_view(request):
    return render(request, 'FAQ.html')

def feature_view(request):
    return render(request, 'feature.html')

def service_view(request):
    return render(request, 'service.html')

def team_view(request):
    return render(request, 'team.html')

def testimonial_view(request):
    return render(request, 'testimonial.html')

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

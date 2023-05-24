from django.shortcuts import render, get_object_or_404
from .models import Template

def home(request):
    templates = Template.objects.all()
    return render(request, 'home.html', {'templates': templates})

def template(request, template_id):
    template = get_object_or_404(Template, pk=template_id)
    return render(request, 'template.html', {'template': template})
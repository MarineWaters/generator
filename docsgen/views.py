from django.shortcuts import render, get_object_or_404
from .models import Template
from django_tex.core import compile_template_to_pdf
from django.http import HttpResponse

def save_and_convert(request):
    if request.method == 'POST':
        latex_text = request.POST.get('latex_text')
        template_name = 'template.tex'
        context = {'latex_text': latex_text}
        pdf = compile_template_to_pdf(template_name, context)
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="converted.pdf"'
        return response

def home(request):
    templates = Template.objects.all()
    return render(request, 'home.html', {'templates': templates})

def template(request, template_id):
    template = get_object_or_404(Template, pk=template_id)
    return render(request, 'template.html', {'template': template})
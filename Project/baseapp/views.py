from django.views.generic import TemplateView
# Create your views here.

class Home(TemplateView):
	template_name = 'baseapp/home.html'


class Syllabus(TemplateView):
	template_name = 'baseapp/syllabus.html'

class Eresources(TemplateView):
	template_name = 'baseapp/eresources.html'

class Qpaper(TemplateView):
	template_name = 'baseapp/qpaper.html'


class Contributors(TemplateView):
	template_name = 'baseapp/contributor.html'

class Faq(TemplateView):
	template_name = 'baseapp/faq.html'
from django.views.generic import TemplateView,CreateView
from .forms import Contact_form
from .models import Contactform


class Introview(TemplateView):
    template_name = 'customer/intro.html'

class Indexview(TemplateView):
    template_name = 'customer/index.html'

class Aboutview(TemplateView):
    template_name = 'customer/about_us.html'

class Serviceview(TemplateView):
    template_name = 'customer/services.html'

class Contactview(CreateView):

    model = Contactform
    form_class = Contact_form
    template_name = 'customer/contact_us.html'

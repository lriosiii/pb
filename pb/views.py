from django.views.generic.base import TemplateView


class MainHome(TemplateView):
    template_name = 'core/base.html'
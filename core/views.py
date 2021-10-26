from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class BaseView(TemplateView):
    template_name = 'core/base.html'


class IndexView(TemplateView):
    template_name = 'core/index.html'


class PlaylistView(TemplateView):
    template_name = 'core/playlist.html'


class EquipmentView(TemplateView):
    template_name = 'core/equipment.html'

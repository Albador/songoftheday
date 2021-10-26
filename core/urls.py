from django.urls import path, include
from core.views import IndexView, BaseView, PlaylistView, EquipmentView

urlpatterns = [
    path('', BaseView.as_view()),
    path('index', IndexView.as_view(), name='index'),
    path('playlist', PlaylistView.as_view(), name='playlist'),
    path('equipment', EquipmentView.as_view(), name='equipment'),
]

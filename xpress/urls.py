from django.urls import path
from django.views.generic import TemplateView

app_name = 'xpress'

urlpatterns = [
    path('',TemplateView.as_view(template_name='xpress/index.html'))
]

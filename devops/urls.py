# from django.conf.urls import re_path
# from re import template
from django.urls.conf import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('api/workflow/', include('workflow.urls')),
]
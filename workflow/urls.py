from django.urls.conf import path
from workflow import views

urlpatterns = [
    path('init', views.init),
]

from django.urls.conf import path
from workflow import views

urlpatterns = [
    path('test', views.test),
    path('init', views.init),
    path('env/add', views.add_env),
    path('demand/add', views.add_demand),
    path('demand/delete', views.delete_demand),
    path('integration/add', views.add_integration),
    path('integration/exit', views.exit_integration),
]

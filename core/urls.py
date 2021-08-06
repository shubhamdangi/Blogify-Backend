
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('xpress.urls',namespace='xpress')),
    path('api/',include('xpress_api.urls',namespace='xpress_api')),
    path('api-login', include('rest_framework.urls', namespace='rest_framework'))
]


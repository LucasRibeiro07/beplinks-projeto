from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('beplinks.urls_api')),
    path('', include('beplinks.urls')),
]
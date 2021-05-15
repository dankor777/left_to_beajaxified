from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('projekt_as.urls')),
    path('uzytkownicy/', include('django.contrib.auth.urls')),
    path('uzytkownicy/', include('uzytkownicy.urls'))
]

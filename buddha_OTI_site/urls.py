from django.contrib import admin
from django.urls import path, include

#for include media folder
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #Text Editor
    path('tinymce/', include('tinymce.urls')),
    path('', include('main.urls')),
    path('quiz/', include('quiz.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

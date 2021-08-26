from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path , include
from Simple_Portfolio import views

app_name = 'Simple_Portfolio'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index , name="index"),
    path('contact/', include('Contact_me.urls')),
]
handler404 = 'Simple_Portfolio.views.handler404'
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
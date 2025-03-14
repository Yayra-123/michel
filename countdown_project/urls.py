from django.contrib import admin
from django.urls import path
from countdown import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    
]
# urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


# <img src="{% static 'images/mon_image.jpg' %}" alt="Mon Image" width="300">

# <img src="{% static 'countdown/img/LOGO_ROND.png' %}" alt="Logo" width="300">
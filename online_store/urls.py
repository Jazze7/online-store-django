from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("web.urls", namespace="web")),
    path('users/', include("users.urls", namespace="users")),
    path('products/', include("products.urls", namespace="products")),

    
    
]
if settings.DEBUG:
    urlpatterns += (
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
        static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)


    )

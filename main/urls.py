from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from main import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('market.urls', namespace='market')),
    path('shop/', include('goods.urls', namespace='shop')),
    path('user/', include('users.urls', namespace='user')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('market.urls', namespace='market')),
    path('shop/', include('goods.urls', namespace='shop')),
]

from django.contrib import admin
from django.urls import path, include
from core.views import BuildViewSet, get_self
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'builds', BuildViewSet, base_name='build')
# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('self/', get_self),
    path('rest-auth/', include('rest_auth.urls')),
]

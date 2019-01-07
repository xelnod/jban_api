from django.contrib import admin
from django.urls import path, include
from core.views import BuildViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'build', BuildViewSet, base_name='build')
# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
]

from django.contrib import admin
from django.urls import path
from .views import main, get_self

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('<int:pk>', main),
    path('self/', get_self)
]

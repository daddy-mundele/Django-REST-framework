from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
api_patterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', views.user_view, name='user'),
    # ... outras definições de URL podem estar presentes ...
] + api_patterns


from rest_framework.routers import DefaultRouter
from .views import SchoolviewSet

router = DefaultRouter()

router .register(prefix='api/v1/schools', viewset=SchoolviewSet, basename='school')

urlpatterns = router.urls
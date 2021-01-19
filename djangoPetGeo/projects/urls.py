from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import ProjectView

router = SimpleRouter()
router.register('api/projects', ProjectView)

urlpatterns = router.urls
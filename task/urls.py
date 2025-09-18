from rest_framework.routers import DefaultRouter
from .views import TaskViewSet,RegisterViewSet

router = DefaultRouter()
router.register(r'task',TaskViewSet,basename='task')
router.register(r'register',RegisterViewSet,basename='register')


urlpatterns = router.urls
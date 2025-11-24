from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, PostViewSet

router = DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("posts", PostViewSet)

# URLConf

urlpatterns = router.urls

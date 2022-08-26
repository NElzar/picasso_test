from rest_framework import routers
from accident.views import CallViewSet


router = routers.SimpleRouter()
router.register(r'accidents', CallViewSet)
urlpatterns = router.urls

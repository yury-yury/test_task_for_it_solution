from rest_framework import routers

from my_app.views import UserViewSet, StudentViewSet, CourseViewSet

router = routers.SimpleRouter()
router.register('user', UserViewSet)
router.register('student', StudentViewSet)
router.register('course', CourseViewSet)

urlpatterns = [

]

urlpatterns += router.urls

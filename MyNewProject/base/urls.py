from django.urls import path, include
from rest_framework.routers import DefaultRouter
from base.views import CourseViewSet, TopicViewSet, BlockViewSet


router = DefaultRouter()
router.register('courses', CourseViewSet)
router.register('topics', TopicViewSet)
router.register('blocks', BlockViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
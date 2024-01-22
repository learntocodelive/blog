import time
from rest_framework import viewsets
from base.util_views import BaseViewSet
from base.serializers import CourseSerializer, TopicSerializer, BlockSerializer
from base.models import Course, Topic, Block, User


class CourseViewSet(BaseViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def create(self, request, *args, **kwargs):
        print(request.data["owner"])
        data = request.data
        if data.get("owner"):
            User.objects.get_or_create(email=data["owner"])
            print("Sleeping")
            time.sleep(0.5)
        return super().create(request, *args, **kwargs)


class TopicViewSet(BaseViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class BlockViewSet(BaseViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer
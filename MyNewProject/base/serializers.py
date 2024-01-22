from rest_framework import serializers
from base.models import Course, Topic, Block, User


class CourseSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        slug_field="email", queryset=User.objects.all()
    )

    class Meta:
        model = Course
        fields = "__all__"


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = "__all__"
from .models import Blog

from rest_framework import serializers, status


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            "id",
            "title",
            "description",
            "summery",
        )

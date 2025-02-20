from Blog.models import Post
from rest_framework import serializers


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "content", "author", "date_posted"]

        # fields = "__all__"
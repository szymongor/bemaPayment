from rest_framework import serializers

from epaymentapp.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False)

    class Meta:
        model = Post
        fields = '__all__'
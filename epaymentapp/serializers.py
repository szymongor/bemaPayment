from rest_framework import serializers

from epaymentapp.models import Post, Bill


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False)

    class Meta:
        model = Post
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
    Creator = serializers.StringRelatedField(many=False)

    class Meta:
        model = Bill
        fields = ('title', 'type', 'creator', 'founder','obligors','payments','status')

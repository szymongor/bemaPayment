from rest_framework import serializers

from epaymentapp.models import Post, Bill, Payment, subPost

class subPostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False)

    class Meta:
        model = subPost
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False)
    subposts = subPostSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bill
        fields = ('title', 'type', 'founder','obligors','payments','status')

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '_all_'

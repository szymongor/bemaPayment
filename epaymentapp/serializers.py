from rest_framework import serializers

from epaymentapp.models import Post, Bill, Payment, subPost


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False)

    class Meta:
        model = Post
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bill
        fields = ('title', 'type', 'creator', 'founder','obligors','payments','status')

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '_all_'

class subPostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False)

    class Meta:
        model = subPost
        fields = '_all_'

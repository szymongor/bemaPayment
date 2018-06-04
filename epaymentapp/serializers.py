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

class PaymentSerializer(serializers.ModelSerializer):
    founder = serializers.StringRelatedField(many=False)
    
    class Meta:
        model = Payment
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
    founder = serializers.StringRelatedField(many=False)
    obligors = serializers.StringRelatedField(many=True)
    payments = PaymentSerializer(many=True)
    class Meta:
        model = Bill
        fields = '__all__'

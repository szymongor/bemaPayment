from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from epaymentapp.models import Post, SiteUser, Bill, Payment
from epaymentapp.serializers import PostSerializer, BillSerializer, PaymentSerializer


class PostsList(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        request_post = request.data['post']
        site_user = SiteUser.objects.get(user= request.user)
        new_post = Post.objects.create(
            author = site_user,
            title = request_post['title'],
            text = request_post['text']
        )
        new_post.save();
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class BillView(APIView):

    def get(self,request):
        Bills = Bill.objects.all()
        serializer = BillSerializer(Bills, many=True)
        return Response(serializer.data)

    def post(self, request):
        request_bill = request.data['bill']
        site_user = SiteUser.objects.get(user= request.user)
        new_bill = Bill.objects.create(
            title = request_bill['title'],
    	    type = request_bill['type'],
    	    amount = request_bill['amount'],
    	    founder = site_user,
            obligors = site_user,
            status = request_post['status']
        )
        new_bill.save();
        Bills = Bill.objects.all()
        serializer = BillSerializer(Bills, many=True)
        return Response(serializer.data)

class PaymentView(APIView):

    def post(self, request):
        request_payment = request.data['payment']
        request_founder = SiteUser.objects.get(user= request.user)
        request_bill = Bill.objects.get(id=request_payment['bill_id'])
        new_payment = Payment.objects.create(
            amount = request_payment['amount'],
            bill = request_bill,
            founder = request_founder
        )
        new_payment.save();
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

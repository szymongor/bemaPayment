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
        request_post = request.data['post']
        site_user = SiteUser.objects.get(user= request.user)
        new_bill = Bill.objects.create(
            title = request_post['title'],
    	    type = request_post['type'],
    	    amount = request_post['amount'],
    	    founder = site_user,
            obligors = site_user,
            status = request_post['status']
        )
        new_bill.save();
        Bills = Bill.objects.all()
        serializer = BillSerializer(Bills, many=True)
        return Response(serializer.data)

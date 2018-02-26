from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from epaymentapp.models import Post, SiteUser
from epaymentapp.serializers import PostSerializer


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
        return Response(request_post)
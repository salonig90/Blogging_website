from django.shortcuts import render
from rest_framework import viewsets
from .models import BlogPost, Comment
from .serializers import BlogPostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

# Create your views here.
# def index(request):
#     return render(request, 'index.html')

class DemoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request.user)
        return Response({"message": "Hello, this is a demo view!"})

class RegisterView(APIView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']

        user = User(username=username)
        user.set_password(password)
        user.save()
        refresh = RefreshToken.for_user(user)

        return Response(
        {
            "status": "success" ,
            "user_id": user.id,
            "refresh" : str(refresh),
            "access" : str(refresh.access_token),
        })

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


from django.shortcuts import render
from blog.models import Post
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PostSerializer
# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    """API endpoint that allows posts to be viewed or edited."""
    queryset = Post.objects.all().order_by('-published')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
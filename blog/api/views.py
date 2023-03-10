from rest_framework import generics

from blog.api.serializers import PostSerializer
from blog.models import Post

# See views.pdf file, slide (14,15,16) to understand what's happening behind the scenes.

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
from rest_framework import generics

from blog.api.serializers import PostSerializer
from blog.models import Post

# See views.pdf file, slide (14,15,16) to understand what's happening behind the scenes.
# from rest_framework.authentication import SessionAuthentication

class PostList(generics.ListCreateAPIView):
    # authentication_classes = [SessionAuthentication]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
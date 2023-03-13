from rest_framework import generics

from blango_auth.models import User
from blog.api.serializers import PostSerializer, UserSerializer, PostDetailSerializer
from blog.models import Post
from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject

# See Course2, Week2, views.pdf file, slide (14,15,16) to understand what's happening behind the scenes.
# from rest_framework.authentication import SessionAuthentication

class PostList(generics.ListCreateAPIView):
    # authentication_classes = [SessionAuthentication]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class UserDetail(generics.RetrieveAPIView):
    lookup_field = "email"
    queryset = User.objects.all()
    serializer_class = UserSerializer
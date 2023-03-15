from rest_framework import generics, viewsets

from blango_auth.models import User
from blog.api.serializers import PostSerializer, UserSerializer, PostDetailSerializer, TagSerializer
from blog.models import Post, Tag
from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject

# See Course2, Week2, views.pdf file, slide (14,15,16) to understand what's happening behind the scenes of ListCreateAPIView.

# class PostList(generics.ListCreateAPIView):
#    # from rest_framework.authentication import SessionAuthentication
#    # authentication_classes = [SessionAuthentication]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
#     queryset = Post.objects.all()
#     serializer_class = PostDetailSerializer


# This Class Replaced Both PostList and PostDetail Views.
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action in ("list", "create"):
            return PostSerializer
        return PostDetailSerializer
    

class UserDetail(generics.RetrieveAPIView):
    lookup_field = "email"
    queryset = User.objects.all()
    serializer_class = UserSerializer


from rest_framework.decorators import action
from rest_framework.response import Response
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    @action(methods=['get'], detail=True, name="Posts with specific Tag")
    def posts(self, request, pk=None):
        tag = self.get_object()
        post_serializer = PostSerializer(
            tag.posts, many=True, context={"request": request}
        )
        return Response(post_serializer.data)
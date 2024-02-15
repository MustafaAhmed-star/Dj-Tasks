from rest_framework.generics import GenericAPIView 
from rest_framework.response import Response
from rest_framework import status

from .serializers import PostSerializer ,CommentSerializer
from .models import Post,Comment
 
 
class PostDetailViewApi(GenericAPIView):
    serializer_class = CommentSerializer

    def get(self, request,pk ,*args, **kwargs):
        post = Post.objects.get(pk=pk)
        order = request.query_params.get('order', 'newest')

        if order == 'oldest':
            comments = Comment.objects.filter(post=post).order_by('create_at')
             

        elif order == 'newest':
            comments = Comment.objects.filter(post=post).order_by('-create_at')
             
        
        else:
            comments = Comment.objects.filter(post=post)
              

        serializers = CommentSerializer(comments,many = True).data
        serializers2 = PostSerializer(post).data
        return Response({'post':serializers2,'comments':serializers},status=status.HTTP_200_OK)
        
    def post(self, request,pk ,*args, **kwargs):
        post = Post.objects.get(pk=pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user,post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
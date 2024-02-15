from rest_framework import  serializers

from .models import Post ,Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = [ 'create_at']
        
        
class PostSerializer(serializers.ModelSerializer):
    # comment_post = CommentSerializer(many  =True)
    
    class Meta:
        model = Post
        fields = ['author','title','content','image']
    
    
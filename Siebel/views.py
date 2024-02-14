from django.shortcuts import render,redirect,get_object_or_404

from .forms import CommentForm
from .models import Post,Comment
 


    
def addComment(request,pk):
    post = get_object_or_404(Post, pk=pk)
    order = request.GET.get('order', 'newest')  
    if order == 'oldest':
        comments = Comment.objects.filter(post=post).order_by('create_at')
    elif order=='newest':
        comments = Comment.objects.filter(post=post).order_by('-create_at')
    else:
        comments = Comment.objects.filter(post=post)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post 
            comment.save()
            
            return redirect(f'/posts/{post.pk}' )
    
    else:
        form = CommentForm()
 
        
    return render(request, 'post_details.html', {'post':post,'form': form , 'comments':comments,})
        
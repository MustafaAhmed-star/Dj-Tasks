from django.shortcuts import render,redirect

from .forms import CommentForm
from .models import Post,Comment
 

# def show(request):
#     return render(request, 'post_details.html')
    
    
    
def addComment(request,pk):
    post = Post.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post 
            comment.save()
            
            return redirect(f'posts/{post.pk}')
    
    else:
        form = CommentForm()
        
    return render(request, 'post_details.html', {'post':post,'form': form})
        
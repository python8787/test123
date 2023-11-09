from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all().order_by('-pub_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


# class PostCreateView(LoginRequiredMixin):
#     model = Post
#     form_class = PostForm
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
#
#     def test_func(self):
#         return self.request.user.is_authenticated

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})

@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id, author=request.user)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form': form, 'post': post})
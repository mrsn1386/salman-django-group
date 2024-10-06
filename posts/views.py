from django.contrib.admin.templatetags.admin_list import pagination
from account.models import User
from django.contrib.staticfiles.views import serve
from django.http import HttpRequest, Http404
from django.shortcuts import render, reverse, redirect
from django.views import View
from django.views.generic import ListView, CreateView, FormView
from posts.forms import CreatePostForm
from posts.models import Post


# Create your views here.

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'posts/all_posts_page.html'


class CreatePostView(View):
    def get(self, request):
        create_post_form = CreatePostForm()
        context = {'create_post_form': create_post_form}
        return render(request, 'posts/create_post_page.html', context)

    def post(self, request: HttpRequest):
        create_post_form = CreatePostForm(request.POST, request.FILES)
        if create_post_form.is_valid():
            title = create_post_form.cleaned_data['title']
            image = request.FILES['image']
            content = create_post_form.cleaned_data['content']
            category = create_post_form.cleaned_data['category']
            user: User = User.objects.get(username=request.user)
            post = Post(title=title, content=content, category=category, author=user, image=image)
            post.save()
            return redirect(reverse('all_posts'))

        context = {'create_post_form': create_post_form}
        return render(request, 'posts/create_post_page.html', context)


class MyPostsListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'posts/myPosts_page.html'

    def get_queryset(self):
        post: Post = Post.objects.filter(author=self.request.user)
        return post




from django.shortcuts import render, get_object_or_404
from django.views.generic import View, CreateView, DetailView, FormView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Blog
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic.detail import SingleObjectMixin


def all_blogs(request):
    blog_count = Blog.objects.count()
    blogs = Blog.objects.all()
    return render(request, 'blog/all_blogs.html', {'blogs': blogs, 'blog_count': blog_count})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})


class CommentGet(DetailView):
    model = Blog
    template_name = 'post_single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class CommentPost(SingleObjectMixin, FormView):
    model = Blog
    form_class = CommentForm
    template_name = "post_single.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()
        return reverse("post_detail", kwargs={'pk': post.pk})

class PostDetailView(View):

    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


class PostNewView(CreateView):
    model = Blog
    template_name = 'post_new.html'
    form_class = PostForm
    success_url = reverse_lazy('home')
    # fields = ['title', 'excerpt', 'body', 'author', 'date', 'photo']


class PostUpdateView(UpdateView):
    model = Blog
    template_name = 'post_update.html'
    fields = ['title', 'excerpt', 'body', 'photo']


class PostDeleteView(DeleteView):
    model = Blog
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

# Create your views here.

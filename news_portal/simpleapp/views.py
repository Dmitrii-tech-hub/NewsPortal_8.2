from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

class NewsListView(ListView):
    model = Post
    template_name = 'news_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(type='NW')  # Filter for news posts
    paginate_by = 10  # Number of posts per page

class SearchView(ListView):
    model = Post
    template_name = 'news_search.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        author_name = self.request.GET.get('author')
        after_date = self.request.GET.get('date_after')

        if title:
            queryset = queryset.filter(title__icontains=title)
        if author_name:
            queryset = queryset.filter(author__user__username__icontains=author_name)
        if after_date:
            queryset = queryset.filter(created_at__date__gt=after_date)

        return queryset


class NewsDetailView(DetailView):
    model = Post
    template_name = 'news_detail.html'
    context_object_name = 'post'

class NewsCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'news_create.html'
    success_url = reverse_lazy('news_list')  # Redirect after successful creation

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'NW'  # Set type to News
        post.save()
        return super().form_valid(form)

class NewsUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'news_edit.html'
    success_url = reverse_lazy('news_list')  # Redirect after successful update

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'NW'  # Ensure the type remains News
        post.save()
        return super().form_valid(form)

class ArticleCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'article_create.html'
    success_url = reverse_lazy('news_list')  # Redirect after successful creation

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'AR'  # Set type to Article
        post.save()
        return super().form_valid(form)

class ArticleUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'article_edit.html'
    success_url = reverse_lazy('news_list')  # Redirect after successful update

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'AR'  # Ensure the type remains Article
        post.save()
        return super().form_valid(form)

@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})


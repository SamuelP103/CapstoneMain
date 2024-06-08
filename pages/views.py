from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.urls import reverse
from collections import Counter
from django.shortcuts import render
from .models import Post
from .forms import CreateForm
from django.db.models import Count, Q


class HomePageView(TemplateView):
    template_name = "pages/home.html"
    
class AboutPageView(TemplateView):
    template_name = "pages/about.html"
    
class Create(CreateView):
    model = Post
    template_name = "pages/create.html"
    form_class = CreateForm
    
    def get_success_url(self) -> str:
        return reverse('list')

class PostDetail(DetailView):
    model = Post
    template_name = "pages/detail.html"
    context_object_name = 'post'

class ListPosts(ListView):
    model = Post
    template_name = "pages/list.html"
    context_object_name = 'posts'
    
    def get_queryset(self):
        posts = super().get_queryset()
        
        all_words_count = Counter()
        for post in posts:
            all_words_count.update(post.content.lower().split())

        specific_words = ["leak", "espionage", "cyber", "lost", "breach", "security"]
        specific_words_in_posts = [word for word in specific_words if all_words_count.get(word, 0) >= 2]

        self.specific_words = specific_words_in_posts

        selected_word = self.request.GET.get('word', '')
        if selected_word:
            query = Q()
            for word in selected_word.split():
                query |= Q(content__icontains=word.lower())
            sorted_posts = posts.filter(query)
        else:
            sorted_posts = posts
        
        return sorted_posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['specific_words'] = self.specific_words
        return context
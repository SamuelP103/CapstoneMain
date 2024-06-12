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

from django.db.models import Count



class ListPosts(ListView):
    model = Post
    template_name = "pages/list.html"
    context_object_name = 'posts'

    def get_queryset(self):
        posts = super().get_queryset()

        all_words_count = Counter()
        for post in posts:
            all_words_count.update(post.content.lower().split())

        specific_words = [
            "APT", "IoT security", "Silk Road", "breach", "attack",
            "cybersecurity", "dark web", "exploit", "incident response", "leak",
            "lost", "malware", "patch", "phishing", "ransomware", "regulation compliance",
            "social engineering", "threat actor", "tor",
            "vulnerability", "zero-day"
        ]

        specific_words_in_posts = {word: all_words_count.get(word, 0) for word in specific_words}
        self.specific_words = specific_words_in_posts

        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        specific_word_counts = {}
        for word, count in self.specific_words.items():
            specific_word_counts[word] = self.get_queryset().filter(content__icontains=word.lower()).count()

        
        selected_word = self.request.GET.get('word', '')
        if selected_word and specific_word_counts[selected_word] == 1:
            specific_word_counts[selected_word] += 1

        context['specific_words'] = specific_word_counts

        
        sorted_posts = self.get_queryset()
        if selected_word:
            query = Q()
            for word in selected_word.split():
                query |= Q(content__icontains=word.lower())
            sorted_posts = sorted_posts.filter(query)

        context[self.context_object_name] = sorted_posts
        return context
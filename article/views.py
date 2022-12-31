from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Article
from django.utils.timezone import now
from django.urls import reverse, reverse_lazy
# Create your views here.



class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'content', 'img']
    template_name = 'create.html'

    def get_success_url(self):
        return reverse('detail', kwargs={'pk':self.object.pk})



class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'

    def get_context_date(self):
        context = super().get_context_data()
        context['update_date'] = now()
        return context

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'content', 'img']
    template_name = 'update.html'

    def get_success_url(self):
        return reverse('detail', kwargs={'pk':self.object.pk})

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'delete.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        return reverse('list')


class ArticleListView(ListView):
    model = Article
    paginate_by = 10
    template_name = 'list.html'

    context = model.objects.all().order_by('-pub_date')
    def get_context_data(self):
        context = super().get_context_data()
        return context


def index_view(request):
    return render(request, 'index.html')
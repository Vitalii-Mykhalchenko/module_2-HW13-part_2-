from django.shortcuts import render, redirect, get_object_or_404
from .forms import TagForm, Tag
from .utils import mongodb
from django.core.paginator import Paginator
from .models import Quote, Author
from .forms import TagForm, AuthorForm, QuoteForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def main(request, page = 1):
    quotes = Quote.objects.all()
    pre_page = 10
    paginator = Paginator(list(quotes),pre_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quoteapp/index.html', context={"quotes": quotes_on_page})




def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/tag.html', {'form': form})

    return render(request, 'quoteapp/tag.html', {'form': TagForm()})


@login_required
def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/author.html', {'form': form})

    return render(request, 'quoteapp/author.html', {'form': AuthorForm()})


@login_required
def quote(request):
    tags = Tag.objects.all()
    authors = Author.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()
            choice_tags = Tag.objects.filter(
                name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)
            choice_author_ids = request.POST.getlist('authors')
            for author_id in choice_author_ids:
                author = Author.objects.get(fullname=author_id)
                id = author.id
                new_quote.author_id = id
            new_quote = form.save()
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/quote.html', {"tags": tags, 'form': form, "authors": authors})

    return render(request, 'quoteapp/quote.html', {"tags": tags, "authors": authors, 'form': QuoteForm()})


def detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'quoteapp/detail.html', {"author": author})

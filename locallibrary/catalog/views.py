from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic
# Create your views here.

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    # Word to search for in book titles and genre names
    search_word = "magic"

    # Count of books containing the search word (case-insensitive)
    num_books_with_word = Book.objects.filter(title__icontains=search_word).count()

    # Count of genres containing the search word (case-insensitive)
    num_genres_with_word = Genre.objects.filter(name__icontains=search_word).count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_books_with_word': num_books_with_word,
        'num_genres_with_word': num_genres_with_word,
        'search_word': search_word,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10  # Optional, for paginated display

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'catalog/author_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(author=self.object)  # Retrieve books by the author
        return context
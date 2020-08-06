from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_filter_books=Book.objects.filter(title='테메레르').count()
    
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()
    
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_filter_book':num_filter_books,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

'''
generic views는 /application_name/the_model_name_list.html의 경로를 가짐
여기에서는 catalog/book_list.html.임
근데 여기에서는 TEMPLATES경로를 template로 했으니
경로가 /catalog/templates/catalog/book_list.html 이렇게됨
'''
class BookListView(generic.ListView):
    model = Book
    paginate_by = 2
    '''
    context_object_name = 'my_book_list'   # your own name for the list as a template variable  book_list.html에서 이걸로 이름 바꿈
    
    queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war 유저가 읽은순으로 5개의 책을 나열
    #template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location
    '''
    '''
    def get_queryset(self):
        return Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context
    '''

class BookDetailView(generic.DetailView):
    model = Book
    


'''위에꺼를 함수기반으로 만들경우
def book_detail_view(request, primary_key):
    try:
        book = Book.objects.get(pk=primary_key)
    except Book.DoesNotExist:#오류처리를 직접해줘야함
        raise Http404('Book does not exist')
    
    return render(request, 'catalog/book_detail.html', context={'book': book})
'''

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author

from django.urls import path
from catalog import views


urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.BookListView.as_view(), name='book'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='author'),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]
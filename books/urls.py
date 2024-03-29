from django.urls import path
from django.urls import path
from books import views


from . import views

# CBV (class based view)
# urlpatterns = [
#     path('', views.BookList.as_view(), name='book_list'),
#     path('view/<int:pk>', views.BookView.as_view(), name='book_view'),
#     path('new', views.BookCreate.as_view(), name='book_new'),
#     path('view/<int:pk>', views.BookView.as_view(), name='book_view'),
#     path('edit/<int:pk>', views.BookUpdate.as_view(), name='book_edit'),
#     path('delete/<int:pk>', views.BookDelete.as_view(), name='book_delete'),
# ]


# FBV (function based view)
urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('view/<int:pk>', views.book_view, name='book_view'),
    path('new', views.book_create, name='book_new'),
    path('edit/<int:pk>', views.book_update, name='book_edit'),
    path('delete/<int:pk>', views.book_delete, name='book_delete'),
]
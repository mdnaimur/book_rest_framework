
from django.urls import path
from book_api.views import BookCreate, BookDetails, BookList


urlpatterns = [
    path('', BookCreate.as_view()),
    path('<int:pk>', BookDetails.as_view()),
    path('list/', BookList.as_view()),
]

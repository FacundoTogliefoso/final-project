from django.urls import path
from .views import PageCreateView, PagesListView, PageDetailView

pages_patterns = ([
    path('', PagesListView.as_view(), name='pages'),
    path('<int:pk>/', PageDetailView.as_view(), name='page'),
    path('create/', PageCreateView.as_view(), name='create'),
], 'pages')

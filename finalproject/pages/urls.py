from django.urls import path
from .views import PageCreateView, PageUpdateView, PagesListView, PageDetailView

pages_patterns = ([
    path('', PagesListView.as_view(), name='pages'),
    path('<int:pk>/', PageDetailView.as_view(), name='page'),
    path('update/<int:pk>/', PageUpdateView.as_view(), name='update'),
    path('create/', PageCreateView.as_view(), name='create'),
], 'pages')

from django.urls import path
from .views import PagesListView, PageDetailView

pages_patterns = ([
    path('', PagesListView.as_view(), name='pages'),
    path('<int:pk>/', PageDetailView.as_view(), name='page'),
], 'pages')

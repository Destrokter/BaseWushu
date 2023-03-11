from django.urls import path
from . import views

urlpatterns = [
    path('', views.TradicView.as_view(), name='tradic'),
    path('tradiccreate', views.Tradiccreate.as_view(), name='tradiccreate'),
    path('<int:pk>', views.TradicDetailView.as_view(), name='tradicdetail'),
    path('<int:pk>/update>', views.TradicUpdateView.as_view(), name='tradicupdate'),
    path('<int:pk>/delete>', views.TradicDeleteView.as_view(), name='tradicdelete'),
    path('search', views.SearchResultsView.as_view(), name='search_results_tradic'),
]

handler404 = "tradic.views.page_not_found_view"
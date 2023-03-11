from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllbaseView.as_view(), name='allbase'),
    path('allbasecreate', views.Allbasecreate.as_view(), name='allbasecreate'),
    path('<int:pk>', views.AllbaseDetailView.as_view(), name='allbasedetail'),
    path('<int:pk>/update>', views.AllbaseUpdateView.as_view(), name='allbaseupdate'),
    path('<int:pk>/delete>', views.AllbaseDeleteView.as_view(), name='allbasedelete'),
    path('search', views.SearchResultsView.as_view(), name='search_results'),
]
handler404 = "allbase.views.page_not_found_view"
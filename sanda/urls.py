from django.urls import path
from . import views

urlpatterns = [
    path('', views.SandaView.as_view(), name='sanda'),
    path('sandacreate', views.Sandacreate.as_view(), name='sandacreate'),
    path('<int:pk>', views.SandaDetailView.as_view(), name='sandadetail'),
    path('<int:pk>/update>', views.SandaUpdateView.as_view(), name='sandaupdate'),
    path('<int:pk>/delete>', views.SandaDeleteView.as_view(), name='sandadelete'),
    path('search', views.SearchResultsView.as_view(), name='search_result_sanda'),
]
handler404 = "sanda.views.page_not_found_view"
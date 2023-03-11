from urllib import request
from django.shortcuts import render, redirect
from .models import Taolu
from .forms import TaoluForm
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

class TaoluView(LoginRequiredMixin, ListView):
    paginate_by = 3
    model = Taolu
    template_name ='taolu/taolu.html'
    context_object_name = 'taolu'

# def taolu(request):
#     taolu= Taolu.objects.order_by('name')
#     paginator = Paginator(taolu, 3)
#     page_number = request.GET.get('page')
#     taolu = paginator.get_page(page_number)
#     return render(request, 'taolu/taolu.html', {'taolu': taolu})
#     #taolu = Taolu.objects.order_by('name')
#     #return render(request, 'taolu/taolu.html', {'taolu':taolu})


class TaoluDetailView(LoginRequiredMixin, DetailView):
    model = Taolu
    template_name ='taolu/details_view.html'
    context_object_name = 'taolu'


class TaoluUpdateView(LoginRequiredMixin, UpdateView):
    model = Taolu
    template_name = 'taolu/create.html'

    form_class = TaoluForm
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs ['instance'].representative:
            return self.handle_no_permission()
        return kwargs


class TaoluDeleteView(LoginRequiredMixin, DeleteView):
    model = Taolu
    success_url = '/taolu/'
    template_name = 'taolu/taolu-delete.html'
    def delete(self):
        self.object = self.get_object()
        self.object.representative
        self.request.user
        if self.request.user != self.object.representative:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


class SearchResultsView(ListView):
    model = Taolu
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Taolu.objects.filter(
            Q(name__name__icontains=query)
        )
        return object_list


class Create(LoginRequiredMixin, CreateView):
   model = Taolu
   form_class = TaoluForm
   template_name = 'taolu/create.html'
   success_url = reverse_lazy('create')
   def form_valid(self, form):
       self.object = form.save(commit=False)
       self.object.representative = self.request.user
       self.object.save()
       return super().form_valid(form)
# @login_required
# def create(request):
#    form = TaoluForm()
#    error =' '
#    if request.method =='POST':
#        form = TaoluForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect ('create')

#        else:
#            error = 'Заповніть коректно поле'



#    #form = TaoluForm()
#    context = {
#        'form': form,
#        'error': error
#    }


#    return render(request, 'taolu/create.html', context)


from urllib import request
from django.shortcuts import render, redirect
from .models import Sanda
from .forms import SandaForm
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

class SandaView(LoginRequiredMixin, ListView):
    paginate_by = 3
    model = Sanda
    template_name ='sanda/sanda.html'
    context_object_name = 'sanda'


# def sanda(request):
#     sanda = Sanda.objects.order_by('name')
#     paginator = Paginator(sanda, 3)
#     page_number = request.GET.get('page')
#     sanda = paginator.get_page(page_number)
#     return render(request, 'sanda/sanda.html', {'sanda': sanda})
#   # sanda = Sanda.objects.order_by('name')
#   # return render(request, 'sanda/sanda.html', {'sanda':sanda})

class SandaDetailView(LoginRequiredMixin, DetailView):
    model = Sanda
    template_name ='sanda/sandadetails_view.html'
    context_object_name = 'sanda'


class SandaUpdateView(LoginRequiredMixin, UpdateView):
    model = Sanda
    template_name = 'sanda/sandacreate.html'

    form_class = SandaForm
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs ['instance'].representative:
            return self.handle_no_permission()
        return kwargs


class SandaDeleteView(LoginRequiredMixin, DeleteView):
    model = Sanda
    success_url = '/sanda/'
    template_name = 'sanda/sanda-delete.html'
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
    model = Sanda
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Sanda.objects.filter(
            Q(name__name__icontains=query)
        )
        return object_list

class Sandacreate(LoginRequiredMixin, CreateView):
   model = Sanda
   form_class = SandaForm
   template_name = 'sanda/sandacreate.html'
   success_url = reverse_lazy('sandacreate')
   def form_valid(self, form):
       self.object = form.save(commit=False)
       self.object.representative = self.request.user
       self.object.save()
       return super().form_valid(form)


# @login_required
# def sandacreate(request):
#    form = SandaForm()
#    error =' '
#    if request.method =='POST':
#        form = SandaForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect ('sandacreate')

#        else:
#            error = 'Заповніть коректно поле'



#    #form = TaoluForm()
#    context = {
#        'form': form,
#        'error': error
#    }


#    return render(request, 'sanda/sandacreate.html', context)


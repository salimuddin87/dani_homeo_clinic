from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import MedicineDetail


class IndexView(generic.ListView):
    template_name = 'app/index.html'
    context_object_name = 'latest_medicine_list'

    def get_queryset(self):
        return MedicineDetail.objects.order_by('date_of_exp')[:20]


class DetailView(generic.ListView):
    model = MedicineDetail
    template_name = 'app/detail.html'

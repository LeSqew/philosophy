from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Concept, HistoricalContext, Quote, Source

# Create your views here.

class ConceptListView(ListView):
    model = Concept
    template_name = 'kant_duty/concept_list.html'
    context_object_name = 'concepts'

class ConceptDetailView(DetailView):
    model = Concept
    template_name = 'kant_duty/concept_detail.html'
    context_object_name = 'concept'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        concept = self.get_object()
        context['historical_contexts'] = concept.historical_contexts.all()
        context['quotes'] = concept.quotes.all()
        context['sources'] = concept.sources.all()
        return context

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView

from webapp.forms import QuoteForm
from webapp.models import Quote


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'quotes'
    model = Quote


class QuoteCreateView(LoginRequiredMixin, CreateView):
    template_name = 'quote_create.html'
    form_class = QuoteForm
    model = Quote
    success_url = 'webapp:index'

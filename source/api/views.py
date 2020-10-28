from django.shortcuts import get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api.serializers import QuoteCreateSerializer, QuoteUpdateSerializer, QuoteSerializer
from webapp.models import Quote
from .permissions import QuotePermissions


class QuoteViewSet(ModelViewSet):
    permission_classes = [QuotePermissions]

    def get_queryset(self):
        if self.request.method == 'GET' and \
                not self.request.user.has_perm('webapp.quote_view'):
            return Quote.get_moderated()
        return Quote.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return QuoteCreateSerializer
        elif self.request.method == 'PUT':
            return QuoteUpdateSerializer
        return QuoteSerializer


class QuotePlusView(APIView):
    def get(self, request, *args, **kwargs):
        quote = get_object_or_404(Quote, pk=kwargs.get('pk'))
        if quote.pk not in self.get_ids():
            quote.rating += 1
            quote.save()
            self.save_to_session(quote)
        return redirect('/api/quote/')

    def get_ids(self):
        return self.request.session.get('ids', [])

    def save_to_session(self, quote):
        ids = self.request.session.get('ids', [])
        ids_minus = self.request.session.get('ids_minus', [])
        if quote.pk not in ids:
            if quote.pk in ids_minus:
                ids_minus.remove(quote.pk)
            ids.append(quote.pk)
        self.request.session['ids'] = ids

        # ids = self.request.session.get('ids', [])
        # if quote.pk not in ids:
        #     ids.append(quote.pk)
        # self.request.session['ids'] = ids


class QuoteMinusView(APIView):
    def get(self, request, *args, **kwargs):
        quote = get_object_or_404(Quote, pk=kwargs.get('pk'))
        print(kwargs['pk'])
        print(self.get_ids(), 'get_ids')
        if quote.pk not in self.get_ids():
            quote.rating -= 1
            quote.save()
            self.save_to_session(quote)
        return redirect('/api/quote/')

    def get_ids(self):
        return self.request.session.get('ids_minus', [])

    def save_to_session(self, quote):
        ids = self.request.session.get('ids', [])
        ids_minus = self.request.session.get('ids_minus', [])
        if quote.pk not in ids_minus:
            if quote.pk in ids:
                ids.remove(quote.pk)
            ids_minus.append(quote.pk)
        self.request.session['ids_minus'] = ids_minus

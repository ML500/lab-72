from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, CharField
from webapp.models import Quote


class QuoteSerializer(ModelSerializer):
    status_display = CharField(max_length=20, source='get_status_display',
                               read_only=True)
    plus = serializers.HyperlinkedIdentityField(read_only=True, view_name='api:quote_plus')
    minus = serializers.HyperlinkedIdentityField(read_only=True, view_name='api:quote_minus')

    class Meta:
        model = Quote
        fields = '__all__'
        read_only_fields = ['text', 'plus', 'minus', 'author', 'email', 'rating', 'status']


class QuoteCreateSerializer(QuoteSerializer):
    class Meta(QuoteSerializer.Meta):
        read_only_fields = ['rating', 'status']


class QuoteUpdateSerializer(QuoteSerializer):
    class Meta(QuoteSerializer.Meta):
        read_only_fields = ['author', 'email', 'rating']

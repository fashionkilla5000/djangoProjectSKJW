from zolnierze.models import *
from .serializers import *
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters  import rest_framework as filters
from rest_framework.permissions import IsAuthenticated

class ZolnierzeFilter(filters.FilterSet):
    imie = filters.CharFilter(lookup_expr='icontains')
    nazwisko = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Zolnierz
        fields = ('imie', 'nazwisko')


class KontraktyFilter(filters.FilterSet):
    poczatek_kontraktu = filters.DateFilter(lookup_expr='icontains')
    koniec_kontraktu = filters.DateFilter(lookup_expr='icontains')

    class Meta:
        model = Kontrakty
        fields = ('poczatek_kontraktu', 'koniec_kontraktu')


class PrzepustkiFilter(filters.FilterSet):
    poczatek_przepustki = filters.DateFilter(lookup_expr='icontains')
    koniec_przepustki = filters.DateFilter(lookup_expr='icontains')

    class Meta:
        model = Przepustki
        fields = ('poczatek_przepustki', 'koniec_przepustki')


class WnioskiFilter(filters.FilterSet):
    rodzaj_wniosku = filters.CharFilter
    status = filters.CharFilter

    class Meta:
        model = Wnioski
        fields = ('rodzaj_wniosku', 'status')


class ZolnierzViewSet(viewsets.ModelViewSet):
    queryset = Zolnierz.objects.all()
    serializer_class = ZolnierzSerializer
    filterset_class = ZolnierzeFilter
    permission_classes = [IsAuthenticated]

    @action(methods=['get'],detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('id_zolnierza').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)

class KontraktyViewSet(viewsets.ModelViewSet):
    queryset = Kontrakty.objects.all()
    serializer_class = KontraktySerializer
    filterset_class = KontraktyFilter
    permission_classes = [IsAuthenticated]

class PrzepustkiViewSet(viewsets.ModelViewSet):
    queryset = Przepustki.objects.all()
    serializer_class = PrzepustkiSerializer
    filterset_class = PrzepustkiFilter
    permission_classes = [IsAuthenticated]

class WnioskiViewSet(viewsets.ModelViewSet):
    queryset = Wnioski.objects.all()
    serializer_class = WnioskiSerializer
    filterset_class = WnioskiFilter
    permission_classes = [IsAuthenticated]
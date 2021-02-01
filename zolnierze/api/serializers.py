from rest_framework import serializers
from zolnierze.models import *
from django.contrib.auth.models import User

class ZolnierzSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Zolnierz
        fields = ('id_zolnierza', 'imie', 'nazwisko', 'data_urodzenia', 'telefon', 'specjalnosc', 'stanowisko_etatowe', 'zameldowanie')

        def __str__(self):
            return self.imie + " " + self.nazwisko

class KontraktySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Kontrakty
        fields = ('zolnierz', 'poczatek_kontraktu', 'koniec_kontraktu', 'wynagrodzenie')

        def __str__(self):
            return self.zolnierz

class PrzepustkiSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Przepustki
        fields = ('zolnierz', 'poczatek_przepustki', 'koniec_przepustki')

        def __str__(self):
            return self.zolnierz

class WnioskiSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Wnioski
        fields = ('zolnierz', 'rodzaj_wniosku', 'status', 'data_zlozenia')

        def __str__(self):
            return self.zolnierz

class UserZolnierzSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Zolnierz
        fields = ['id_zolnierza','imie','nazwisko']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    books = UserZolnierzSerializer(many=True,read_only=True)
    class Meta:
        model = User
        fields = ['id_zolnierza','imie','nazwisko']


from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from . import views
from .models import *
from rest_framework import status
from django.utils.http import urlencode
from django import urls

class ZolnierzTest(APITestCase):
    def post_zolnierz_nazwisko(self, name):
        url = reverse(views.ZolnierzListView.name)
        data = {'nazwisko':name}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_zolnierz_nazwisko(self):
        new_zolnierz_nazwisko = 'Test'
        response = self.post_zolnierz_nazwisko(new_zolnierz_nazwisko)
        print("PK {0}".format(Zolnierz.objects.get().pk))
        assert response.status_code == status.HTTP_201_CREATED
        assert Zolnierz.objects.count() == 1
        assert Zolnierz.objects.get().name == new_zolnierz_nazwisko

    def test_filter_zolnierz_by_nazwisko(self):
        zolnierz_by_nazwisko_one = 'franek'
        zolnierz_by_nazwisko_two = 'test'
        self.post_zolnierz_nazwisko(zolnierz_by_nazwisko_one)
        self.post_zolnierz_nazwisko(zolnierz_by_nazwisko_two)
        filter_by_name = {'name': zolnierz_by_nazwisko_one}
        url= '{0}?{1}'.format(reverse(views.ZolnierzListView.name), urlencode(filter_by_name))
        print(url)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['name'] == zolnierz_by_nazwisko_one

class WnioskiTest(APITestCase):

    def post_wnioski_status(self, name):
        url = reverse(views.WnioskiDetailView.name)
        data = {'nazwa': name}
        response = self.client.post(url, data, format='json')
        return response

    def test_update_Wnioski_status(self):
        wnioski_status_name = 'przyjęty'
        response = self.post_wnioski_status(wnioski_status_name)
        url = urls.reverse(views.WnioskiDetailView.name, None, {response.data['pk']})
        updated_wnioski_status_name = 'odrzucony'
        data = {'name': updated_wnioski_status_name}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['name'] == updated_wnioski_status_name

    def test_get_Wnioski_status(self):
        wnioski_status_name = 'przyjęty'
        response = self.post_wnioski_status(wnioski_status_name)
        url = urls.reverse(views.WnioskiDetailView.name, None, {response.data['pk']})
        get_response = self.client.patch(url, format='json')
        assert get_response.status_code == status.HTTP_200_OK
        assert get_response.data['status'] == wnioski_status_name
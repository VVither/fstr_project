import unittest
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import pereval_added, User, Coords
from .serializers import PerevalSerializer
import json


class SubmitDataViewTests(APITestCase):

    def setUp(self):
        self.test_user = User.objects.create(email="test@example.com")

        self.test_coords = Coords.objects.create(latitude=40.7128, longitude=-74.0060, height=1000)


    def test_create_pereval(self):
        pereval_data = {
            'beautyTitle': 'Test Pereval',
            'title': 'Test Pereval Title',
            'coords': {'latitude': 40.7128, 'longitude': -74.0060, 'height': 1000},
            'user': {'email': 'test@example.com'},
            'images': [{'image_url': 'http://example.com/image1.jpg'}, {'image_url': 'http://example.com/image2.jpg'}],
            'winter_level': 'easy',
            'summer_level': 'medium'
            }
        
        url = reverse('pereval-list')  

        response = self.client.post(url, data=pereval_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_get_pereval_by_id(self):
        pereval = pereval_added.objects.create(beautyTitle='Test Pereval', title='Test Title', coords_id=self.test_coords, user=self.test_user, status='new')

        url = reverse('pereval-detail', args=[pereval.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('beautyTitle', response.data)

    def test_get_perevals_by_email(self):
        for i in range(3):
            pereval_added.objects.create(beautyTitle=f'Test Pereval {i+1}', title=f'Test Title {i+1}', coords_id=self.test_coords, user=self.test_user, status='new')
        
        url = reverse('pereval-list') + "?user__email=test@example.com"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)


    def test_get_pereval_not_found(self):
        url = reverse('pereval-detail', args=[1000])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['state'], 0)

    def test_patch_pereval(self):
        pereval = pereval_added.objects.create(beautyTitle='Test Pereval', title='Test Title', coords_id=self.test_coords, user=self.test_user, status='new')
        url = reverse('pereval-detail', args=[pereval.pk])

        patch_data = {'beautyTitle': 'Updated Test Pereval'}

        response = self.client.patch(url, data=patch_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['state'], 1)
        self.assertEqual(pereval_added.objects.get(pk=pereval.pk).beautyTitle, 'Updated Test Pereval')

    def test_patch_pereval_not_new(self):
        pereval = pereval_added.objects.create(beautyTitle='Test Pereval', title='Test Title', coords_id=self.test_coords, user=self.test_user, status='accepted')
        url = reverse('pereval-detail', args=[pereval.pk])
        patch_data = {'beautyTitle': 'Updated Test Pereval'}
        response = self.client.patch(url, data=patch_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['state'], 0)
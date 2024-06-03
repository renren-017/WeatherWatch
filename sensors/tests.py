from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from sensors.models import Alert


class AlertViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.alert = Alert.objects.create(description='Initial alert', sensor_id=1)

    def test_get_alerts(self):
        """
        Ensure we can retrieve a list of alerts.
        """
        url = reverse('alert-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_alert(self):
        """
        Ensure we can create a new alert.
        """
        url = reverse('alert-list')
        data = {'description': 'New alert', 'sensor': 1}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Alert.objects.count(), 2)

    def test_update_alert(self):
        """
        Ensure we can update an existing alert.
        """
        url = reverse('alert-detail', kwargs={'pk': self.alert.pk})
        data = {'description': 'Updated alert', 'sensor': 1}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.alert.refresh_from_db()
        self.assertEqual(self.alert.description, 'Updated alert')

    def test_delete_alert(self):
        """
        Ensure we can delete an alert.
        """
        url = reverse('alert-detail', kwargs={'pk': self.alert.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Alert.objects.count(), 0)

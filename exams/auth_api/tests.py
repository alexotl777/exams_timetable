from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from auth_api.models import User


class RegisterUserAPITestCase(APITestCase):
    def setUp(self):
        self.endpoint = reverse("register")

    def test_register_success(self):
        """Успешная регистрация пользователя"""
        data = {"email": "test@example.com", "password": "StrongPass123"}
        response = self.client.post(self.endpoint, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["message"], "User registered successfully")
        self.assertTrue(User.objects.filter(email="test@example.com").exists())

    def test_register_weak_password(self):
        """Ошибка при слабом пароле"""
        data = {"email": "weak@example.com", "password": "12345"}
        response = self.client.post(self.endpoint, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("password", response.data)
        self.assertFalse(User.objects.filter(email="weak@example.com").exists())

    def test_register_duplicate_email(self):
        """Ошибка при регистрации с уже существующим email"""
        User.objects.create(email="duplicate@example.com", password="StrongPass123")

        data = {"email": "duplicate@example.com", "password": "NewPass123"}
        response = self.client.post(self.endpoint, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.data)

    def test_register_invalid_email(self):
        """Ошибка при некорректном email"""
        data = {"email": "invalid-email", "password": "ValidPass123"}
        response = self.client.post(self.endpoint, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.data)

    def test_register_missing_fields(self):
        """Ошибка при отсутствии полей"""
        data = {}
        response = self.client.post(self.endpoint, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.data)
        self.assertIn("password", response.data)

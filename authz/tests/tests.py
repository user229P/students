from django.test import TestCase
from django.urls import reverse
from authz.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.messages import get_messages

class UserRegisterTestCase(TestCase):
    def setUp(self):
        self.register_url = reverse('signupUser')

    def test_valid_registration(self):
        data = {
            'email': 'test@example.com',
            'username': 'testuser',
            'password': 'testpassword',
            'password2': 'testpassword'
        }
        response = self.client.post(self.register_url, data)
        
        self.assertRedirects(response, reverse('loginUser'))
        

    def test_email_already_exists(self):
        User.objects.create_user(email='existing@example.com', username='existinguser', password='existingpassword')
        data = {
            'email': 'existing@example.com',
            'username': 'newuser',
            'password': 'newpassword',
            'password2': 'newpassword'
        }
        response = self.client.post(self.register_url, data)
        messages = [str(message) for message in get_messages(response.wsgi_request)]
        self.assertIn('Email is already in use.', messages) 
        
        

    def test_username_already_exists(self):
        User.objects.create_user(email='demo@example.com', username='existinguser', password='existingpassword')
        data = {
            'email': 'new@example.com',
            'username': 'existinguser',
            'password': 'newpassword',
            'password2': 'newpassword'
        }
        response = self.client.post(self.register_url, data)
        messages = [str(message) for message in get_messages(response.wsgi_request)]
        self.assertIn('Username is already in use.', messages) 
        

    def test_passwords_do_not_match(self):
        data = {
            'email': 'test@example.com',
            'username': 'testuser',
            'password': 'password1',
            'password2': 'password2'
        }
        response = self.client.post(self.register_url, data)
        messages = [str(message) for message in get_messages(response.wsgi_request)]
        self.assertIn('Passwords do not match.', messages) 
        
class UserLoginTestCase(TestCase):
    def setUp(self):
        self.login_url = reverse('loginUser')
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_valid_login(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        response = self.client.post(self.login_url, data)
        

    def test_invalid_credentials(self):
        data = {
            'username': 'testuser',
            'password': 'wrongpassword',
        }
        response = self.client.post(self.login_url, data)


class UpdateProfileTestCase(TestCase):
    def setUp(self):
        self.update_profile_url = reverse('update_profile')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

    def test_authenticated_user_can_update_profile(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            'email': 'newemail@example.com',
            'username': 'newusername',
            'fname': 'New',
            'lname': 'User',
        }
        response = self.client.post(self.update_profile_url, data)
        
        self.assertRedirects(response, reverse('profile'))
        self.user.refresh_from_db()  
        self.assertEqual(self.user.email, 'newemail@example.com') 
        self.assertEqual(self.user.username, 'newusername')  
        self.assertEqual(self.user.first_name, 'New')  
        self.assertEqual(self.user.last_name, 'User')  
        messages = [str(message) for message in get_messages(response.wsgi_request)]
        self.assertIn('Profile updated successfully.', messages) 

    def test_email_already_exists(self):
        self.client.login(username='testuser', password='testpassword')
        User.objects.create_user(email='existing@example.com', username='existinguser', password='existingpassword')
        data = {
            'email': 'existing@example.com',
            'username': 'newusername',
            'fname': 'New',
            'lname': 'User',
        }
        response = self.client.post(self.update_profile_url, data)
        self.assertContains(response, 'Email is already in use.')

    def test_username_already_exists(self):
        self.client.login(username='testuser', password='testpassword')
        User.objects.create_user(email='newemail@example.com', username='existinguser', password='existingpassword')
        data = {
            'email': 'new@example.com',
            'username': 'existinguser',
            'fname': 'New',
            'lname': 'User',
        }
        response = self.client.post(self.update_profile_url, data)
        messages = [str(message) for message in get_messages(response.wsgi_request)]
        self.assertIn('Username is already in use.', messages)
        
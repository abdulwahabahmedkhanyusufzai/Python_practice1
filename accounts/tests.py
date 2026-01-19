from django.test import TestCase, Client
from django.urls import reverse
from .models import Account

class BankFullStackTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a test account
        self.account = Account.objects.create(
            account_no="TEST001",
            name="Test User",
            age=30,
            pin=1234,
            email="test@example.com",
            balance=1000
        )

    def test_dashboard_loads(self):
        """Test that the dashboard loads clearly (Frontend check)"""
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test User") # Check if data is passed to template

    def test_create_account_flow(self):
        """Test creating an account via the form (Frontend -> Backend check)"""
        response = self.client.post(reverse('create_account'), {
            'name': 'New User',
            'age': 25,
            'pin': 5678,
            'email': 'new@example.com',
            'balance': 500
        }, follow=True) # follow=True follows the redirect
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Account.objects.filter(name='New User').exists())
        self.assertContains(response, "Account created!")

    def test_deposit_flow(self):
        """Test depositing money via the web interface"""
        url = reverse('deposit', kwargs={'pk': self.account.pk})
        response = self.client.post(url, {
            'amount': 500,
            'pin': 1234
        }, follow=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Deposited 500 successfully")
        
        # Verify Database
        self.account.refresh_from_db()
        self.assertEqual(self.account.balance, 1500)

    def test_withdraw_flow_insufficient_funds(self):
        """Test withdrawal validation logic"""
        url = reverse('withdraw', kwargs={'pk': self.account.pk})
        response = self.client.post(url, {
            'amount': 2000, # More than balance (1000)
            'pin': 1234
        }, follow=True)
        
        self.assertContains(response, "Insufficient Funds")
        self.account.refresh_from_db()
        self.assertEqual(self.account.balance, 1000) # Balance should be unchanged

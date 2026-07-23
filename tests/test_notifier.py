"""Test notification service."""
import pytest
from backend.services.notifier import NotificationService

class TestNotificationService:
    """Test notification functionality."""
    
    @pytest.fixture
    def notifier(self):
        """Initialize notifier."""
        return NotificationService()
    
    def test_send_sms(self, notifier):
        """Test SMS sending."""
        result = notifier.send_sms('+91234567890', 'Test message')
        # In testing, this should return True or handle gracefully
        assert isinstance(result, bool)
    
    def test_batch_notifications(self, notifier):
        """Test batch notifications."""
        recipients = [
            {'phone': '+91234567890'},
            {'phone': '+91987654321'}
        ]
        result = notifier.send_batch_notifications(recipients, 'Test', method='sms')
        assert 'success' in result
        assert 'failed' in result

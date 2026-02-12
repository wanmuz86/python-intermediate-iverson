
from .notifcation import Notification
from .logged_notification import LoggedNotification

class SMSNotification(LoggedNotification):
    """
    SMS notification implementation.

    Attributes:
        sender_id (str): SMS sender identifier.
    """

    def __init__(self, recipient: str, sender_id: str = "APP123"):
        super().__init__(recipient)
        self.sender_id = sender_id

    def send(self, message: str) -> None:
        self._log("Sending SMS")
        
        """
        Send an SMS notification.

        Args:
            message (str): SMS message content.
        """
        #Mock code to send SMS
        print(
            f"[SMS] From: {self.sender_id} -> "
            f"{self.recipient} | Message: {message}"
        )

from .notifcation import Notification
from .logged_notification import LoggedNotification

# Relace Noticiation wit LoggedNotification
class EmailNotification(LoggedNotification):

    """
    Email notification implementation.

    Attributes:
        subject_prefix (str): Prefix added to email subject.
    """


    def __init__(self, recipient, subject_prefix:str = "[APP]"):
        super().__init__(recipient)
        self.subject_prefix = subject_prefix


    def send(self, message:str)-> None:
        
        # Write the action to log
        self._log("SENDING EMAIL")

        """
        Send an email notification.

        Args:
            message (str): Email message content.
        """


        #Mock code to send email
        print(
            f"[EMAIL] To: {self.recipient} |"
            f"Subject: {self.subject_prefix} Update "
            f"Message: {message}"
        )

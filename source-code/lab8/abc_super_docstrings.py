from models.email_notification import EmailNotification
from models.sms_notification import SMSNotification
from models.notifcation import Notification

#Abstract class cannot be instatiated
# It can only be extended by other class
# And that class needs to follow the given contract
# n = Notification("test@example.com")

email = EmailNotification("test@example.com")
sms = SMSNotification("+60123456789")

email.send("Hello")
sms.send("Hello World")

print("\n--- Documentation Preview ---\n")
help(SMSNotification)

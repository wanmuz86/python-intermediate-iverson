from .notifcation import Notification

class LoggedNotification(Notification):
    """
    Intermediate notification class with logging support.

    Attributes:
        log_enabled (bool): Enable or disable logging.
    """

    # Another example of specifying the type :boolean
    def __init__(self, recipient, log_enabled:bool=True):
        super().__init__(recipient)
        self.log_enabled = log_enabled

    def _log(self, action:str)->None:
        """
        Log an action if logging is enabled.

        Args:
            action (str): Action description.
        """
        if self.log_enabled:
            print(f"[LOG] {action} -> {self.recipient}")
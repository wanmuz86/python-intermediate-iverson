from abc import ABC, abstractmethod

# (ABC) -> Specify that this is an abstract class
# Abstract class - provide the contract/format to the implementor
class Notification(ABC):

    """
    Base abstract notification type.

    Attributes:
        recipient (str): Target user identifier (email or phone).

    Methods:
        send(message: str) -> None
            Send a message to the recipient.
    """

    def __init__(self, recipient:str):
        self.recipient = recipient

# ALl class that implements/extends this Class needs to implement send method
    @abstractmethod
    # :str means the message needs to be of type string (optional but best practice in Python)
    # -> None means the return type is None / void (no return)
    def send(self, message:str) ->None:

        """
        Send a message to the recipient.

        Args:
            message (str): Message content.
        """


# pass means do nothing - the end
        pass
#!/usr/bin/env python3
"""Observer pattern — news notification system."""


class NewsSubject:
    """A subject that notifies observers of news events."""

    def __init__(self):
        """Initialize with empty observers."""
        self._observers = []

    def subscribe(self, observer, topics=None):
        """Subscribe an observer to topics."""
        self._observers.append((observer, topics))

    def unsubscribe(self, observer):
        """Unsubscribe an observer."""
        self._observers = [
            (obs, topics) for obs, topics in self._observers
            if obs is not observer
        ]

    def notify(self, topic, data):
        """Notify all relevant observers."""
        for observer, topics in list(self._observers):
            if topics is None or topic in topics:
                observer.update(topic, data)


class LogObserver:
    """An observer that logs news."""

    def update(self, topic, data):
        """Print a log message."""
        print("log:{}={}".format(topic, data))


class EmailObserver:
    """An observer that sends emails."""

    def update(self, topic, data):
        """Print an email message."""
        print("email:{}={}".format(topic, data))


class SmsObserver:
    """An observer that sends SMS alerts."""

    def update(self, topic, data):
        """Print an SMS message."""
        print("sms:{}={}".format(topic, data))


def main():
    """Main function."""
    subject = NewsSubject()

    log_observer = LogObserver()
    email_observer = EmailObserver()
    sms_observer = SmsObserver()

    subject.subscribe(log_observer, topics={"sports", "breaking"})
    subject.subscribe(email_observer)
    subject.subscribe(sms_observer, topics={"breaking"})

    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")


if __name__ == "__main__":
    main()

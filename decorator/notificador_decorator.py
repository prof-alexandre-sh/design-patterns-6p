# Componente base
class Message:
    def __init__(self, content):
        self._content = content

    def send(self):
        return self._content

# Decorador base
class NotificationDecorator(Message):
    def __init__(self, message):
        self._message = message # Composição. Decorator TEM um componente base

    def send(self):
        return self._message.send()

# Decoradores concretos
class EmailNotification(NotificationDecorator):
    def send(self):
        email_content = f"{self._message.send()}" + "\nenviado por email"
        return email_content

class SMSNotification(NotificationDecorator):
    def send(self):
        sms_content = f"{self._message.send()}" + "\nenviado por SMS"
        return sms_content

class MsTeamsNotification(NotificationDecorator):
    def send(self):
        push_content = f"{self._message.send()}" + "\nenviado por Ms Teams"
        return push_content

# Uso
basic_message = Message("Hello, world!")

email_notification = EmailNotification(basic_message)
sms_notification = SMSNotification(email_notification)
teams_notification = MsTeamsNotification(sms_notification)

print(basic_message.send())
#print(email_notification.send())
#print(sms_notification.send())
#print(teams_notification.send())
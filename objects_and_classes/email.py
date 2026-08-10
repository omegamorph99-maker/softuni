class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


sentences = []
information = input()

while information != 'Stop':
    information = information.split()
    sender, receiver, content = information
    sentence = Email(sender, receiver, content)
    sentences.append(sentence)
    information = input()

indices = list(map(int, input().split(', ')))

for index in indices:
    sentences[index].send()

for email in sentences:
    print(email.get_info())
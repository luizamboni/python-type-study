from typing import List


class Message:
    # it will broke: use type between '' to forward bind Type when Queue already exist
    # queue: Queue
    queue: 'Queue'
    content: str

    def __init__(self, content: str) -> None:
        self.content = content

    # it will broke: use type between '' to forward bind Type when Queue already exist
    # def bind_queue(self, queue: Queue) -> None: 
    def bind_queue(self, queue: 'Queue') -> None:
        self.queue = queue

class Queue:
    messages: List[Message]
    
    def __init__(self, unbound_messages: List[Message]) -> None:
        self.messages = unbound_messages
        for message in self.messages:
            message.bind_queue(self)



messages = [
    Message('a'),
    Message('b'),
    Message('c'),
    Message('d'),
]

queue = Queue(messages)

print(queue.messages)
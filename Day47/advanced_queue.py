from basic_queue import Queue
import json


class QueueOutOfRangeException(Exception):
    pass


class AdvancedQueue(Queue):
    _queue_instances = {}

    def __init__(self, name, size):
        super().__init__()
        self.name = name
        self.size = size

        AdvancedQueue._queue_instances[name] = self

    def insert(self, value):
        if len(self.queue) >= self.size:
            raise QueueOutOfRangeException(
                f"Queue '{self.name}' is at its maximum size ({self.size}). Cannot insert more values.")
        self.queue.append(value)

    @classmethod
    def get_queue_by_name(cls, name):
        return cls._queue_instances.get(name)

    def to_dict(self):
        return {
            'name': self.name,
            'size': self.size,
            'queue_contents': self.queue
        }

    @classmethod
    def save(cls):
        queue_data = {name: queue.to_dict()
                      for name, queue in cls._queue_instances.items()}
        with open("queues.json", 'w') as file:
            json.dump(queue_data, file, indent=4)

    @classmethod
    def load(cls):
        with open("queues.json", 'r') as file:
            queue_data = json.load(file)

        return queue_data

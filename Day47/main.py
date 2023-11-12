from basic_queue import Queue
from advanced_queue import AdvancedQueue

my_queue = Queue()

my_queue.insert(1)
my_queue.insert(2)
print(my_queue)
print("Is the queue empty?", my_queue.is_empty())

print("Popped:", my_queue.pop())
print("Popped:", my_queue.pop())
print(my_queue)
print("Popped:", my_queue.pop())
print("Is the queue empty?", my_queue.is_empty())

# ======================================================

queue1 = AdvancedQueue("Queue1", 2)
queue2 = AdvancedQueue("Queue2", 2)


queue1.insert(1)
queue1.insert(2)
queue2.insert("hj")
queue2.insert(2)
print(queue1)
print(queue2)

# queue1.insert(3)

AdvancedQueue.save()
print(AdvancedQueue.load())

retrieved_queue = AdvancedQueue.get_queue_by_name("Queue2")
print(retrieved_queue)

print(len(AdvancedQueue._queue_instances))

print(queue1.pop())
AdvancedQueue.save()
print(AdvancedQueue.load())

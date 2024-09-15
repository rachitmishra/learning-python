"""
Queue

Hot Potato Game
"""
from ds_queue import Queue


def hot_potato(name_list, num):
    queue = Queue()
    for name in name_list:
        queue.enqueue(name)

    while queue.size() > 1:
        for i in range(num):
            queue.enqueue(queue.dequeue())

        queue.dequeue()

    return queue.dequeue()


if __name__ == '__main__':
    names = ["Bill", "David", "Susan", "Jane", "Kent", "Brad", "John", "Hercules"]
    print(hot_potato(names, 7))

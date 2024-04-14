from ting_file_management.abstract_queue import AbstractQueue

from collections import deque


class Queue(AbstractQueue):
    def __init__(self):
        self._queue = deque()

    def __len__(self):
        return len(self._queue)

    def enqueue(self, value):
        self._queue.append(value)

    def dequeue(self):
        if not len(self._queue):
            return None
        return self._queue.popleft()

    def search(self, index):
        try:
            assert index >= 0
            return self._queue[index]
        except (IndexError, AssertionError):
            raise IndexError("Índice Inválido ou Inexistente")

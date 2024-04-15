import pytest
from ting_file_management.priority_queue import PriorityQueue


def empty_priority_queue():
    return PriorityQueue()


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    priority_queue.enqueue(
        {"nome_do_arquivo": "arquivo1.txt", "qtd_linhas": 4}
    )
    priority_queue.enqueue(
        {"nome_do_arquivo": "arquivo2.txt", "qtd_linhas": 7}
    )
    priority_queue.enqueue(
        {"nome_do_arquivo": "arquivo3.txt", "qtd_linhas": 3}
    )
    priority_queue.enqueue(
        {"nome_do_arquivo": "arquivo4.txt", "qtd_linhas": 5}
    )

    # Validate the length of the priority queue
    assert len(priority_queue) == 4

    # Test search functionality
    assert priority_queue.search(2) == {
        "nome_do_arquivo": "arquivo2.txt",
        "qtd_linhas": 7,
    }

    # Trying to search with invalid index should raise IndexError
    with pytest.raises(IndexError):
        priority_queue.search(66)  # Invalid index should raise IndexError

    # Dequeue elements and validate the order based on priority
    first = priority_queue.dequeue()  # High priority
    second = priority_queue.dequeue()  # Regular priority
    third = priority_queue.dequeue()  # Regular priority
    fourth = priority_queue.dequeue()  # High priority

    # Test dequeued elements
    assert first == {"nome_do_arquivo": "arquivo1.txt", "qtd_linhas": 4}
    assert second == {"nome_do_arquivo": "arquivo3.txt", "qtd_linhas": 3}
    assert third == {"nome_do_arquivo": "arquivo2.txt", "qtd_linhas": 7}
    assert fourth == {"nome_do_arquivo": "arquivo4.txt", "qtd_linhas": 5}

    # Validate the length after dequeuing
    assert (
        len(priority_queue) == 0
    )  # Only one element left in the queue (previously 4, now 0)

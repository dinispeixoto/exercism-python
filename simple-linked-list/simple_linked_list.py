from typing import List


class Node:
    def __init__(self, value: int, next_node: 'Node'):
        self._value = value
        self.next_node = next_node

    def value(self) -> int:
        return self._value

    def next(self) -> 'Node':
        return self.next_node


class LinkedList:
    def __init__(self, values=[]):
        self.size = 0
        self.node = None

        for value in values:
            self.push(value)

    def __iter__(self) -> 'LinkedList':
        return self

    def __len__(self) -> int:
        return self.size

    def __next__(self) -> int:
        previous = self.node
        if previous:
            self.node = self.node.next()
            return previous.value()
        else:
            raise StopIteration

    def head(self) -> 'Node':
        if not self.node:
            raise EmptyListException("List shouldn't be empty.")
        return self.node

    def push(self, value: int) -> None:
        self.node = Node(value, self.node)
        self.size += 1

    def pop(self) -> int:
        if not self.node:
            raise EmptyListException("List shouldn't be empty.")

        previous = self.node
        self.node = previous.next()
        self.size -= 1

        return previous.value()

    def reversed(self) -> List[int]:
        return [node for node in self][::-1]


class EmptyListException(Exception):
    ...

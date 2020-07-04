class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.previous = previous
        self.succeeding = succeeding


class LinkedList:
    def __init__(self):
        self.front = None
        self.back = None

    def push(self, value):
        if not self.back:
            self.back = Node(value, None, None)
            self.front = self.back
        else:
            old_back = self.back
            new_back = Node(value, None, old_back)
            old_back.succeeding = new_back
            self.back = new_back

    def pop(self):
        if self.back.previous:
            previous = self.back
            self.back = self.back.previous
        else:
            previous = self.back
            self.back = None
            self.front = None
        return previous.value

    def unshift(self, value):
        if not self.front:
            self.back = Node(value, None, None)
            self.front = self.back
        else:
            old_front = self.front
            new_front = Node(value, old_front, None)
            old_front.previous = new_front
            self.front = new_front

    def shift(self):
        if self.front.succeeding:
            previous = self.front
            self.front = self.front.succeeding
        else:
            previous = self.front
            self.back = None
            self.front = None
        return previous.value

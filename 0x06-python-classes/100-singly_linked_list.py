#!/usr/bin/python3
"""Module contains a Node class and a SinglyLinkedList class"""


class SinglyLinkedList:
    """SinglyLinkedList class for a singly-linked list"""

    def __init__(self):
        self.__head = None

    def __str__(self):
        node = self.__head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        new = Node(value)

        if self.__head is None:
            self.__head = new
            return

        if value < self.__head.data:
            new.next_node = self.__head
            self.__head = new
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node
        new.next_node = current.next_node
        current.next_node = new


class Node:
    """Node class for a node in a singly-linked list"""

    def __init__(self, data, next_node=None):
        if not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")

        if not isinstance(data, int):
            raise TypeError("data must be an integer")

        self.__next_node = next_node
        self.__data = data

    @property
    def data(self):
        """Setter for the private instance attribute __data"""
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Add a pointer to the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Add a pointer to the next node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

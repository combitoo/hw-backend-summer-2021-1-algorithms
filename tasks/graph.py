from collections import deque
from typing import TypeVar, Generic

__all__ = ("Node", "Graph")

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value
        self.outbound: list[Node] = []
        self.inbound: list[Node] = []

    @property
    def value(self) -> T:
        return self._value

    def point_to(self, other: "Node") -> None:
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self) -> str:
        return f"Node({repr(self._value)})"

    __repr__ = __str__


class Graph:
    """Test"""
    def __init__(self, root: Node) -> None:
        self._root = root

    def dfs(self) -> list[Node]:
        visited = set()
        result = []

        def dfs_util(node):
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in node.outbound:
                    dfs_util(neighbor)

        dfs_util(self._root)
        return result

    def bfs(self) -> list[Node]:
        visited = set()
        result = []
        queue = deque()

        queue.append(self._root)
        visited.add(self._root)

        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbor in node.outbound:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result
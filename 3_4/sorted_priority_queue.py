from sorted_priority_queue_abstract import SortedPriorityQueueAbstract
from typing import Any, Tuple

class _Item:
    def __init__(self, k, v):
        self._key = k
        self._value = v
    def __ge__(self, other): #greater/equal
        return self._key >= other._key

class SortedPriorityQueue(SortedPriorityQueueAbstract):
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def add(self, k: Any, v: Any) -> None:
        item = _Item(k, v)
        i = 0
        while i < len(self._data) and item >= (self._data[i]):
            i += 1
        self._data.insert(i, item)

    def min(self) -> Tuple[Any]:
        if self.is_empty():
            raise Exception("Estructura vacía.")
        else:
            return (self._data[0]._key, self._data[0]._value)

    def remove_min(self) -> Tuple[Any]:
        if self.is_empty():
            raise Exception("Estructura vacía")
        else:
            e = self._data.pop(0)
            return (e._key, e._value)

    def __str__(self) -> str:
        return str(f"SortedPriorityQueue({[e._value for e in self._data]})")
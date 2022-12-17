from __future__ import annotations
from abc import abstractmethod
from typing import Any, Optional, Dict
from collections import Counter
from ..singleton import ABCMetaSingleton
from io import StringIO


__all__ = ('Ingredient',)


class Ingredient(metaclass=ABCMetaSingleton):
    __slots__ = ('name', 'counter', 'parent')

    def __init__(
            self,
            name: str,
            parent: Optional[Ingredient] = None,
            *args,
            **kwargs
    ):
        self.name = name
        self.counter = Counter()
        self.parent = parent

    @abstractmethod
    def contains(self) -> Any: ...

    def structure(self, output: Optional[StringIO] = None, indent: int = 0) -> None: ...

    @classmethod
    def linearize_content(cls, contains) -> Dict:
        linearize_list = Counter()
        if 'ingredients' not in contains:
            linearize_list.update({contains['name']: contains['quantity']})
        else:
            for el in contains['ingredients']:
                linearize_list.update(cls.linearize_content(el))
        return dict(linearize_list)

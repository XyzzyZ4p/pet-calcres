from __future__ import annotations
from typing import Dict, List
from ..composite import Ingredient, Composite


__all__ = ('ComposeFactory',)


class ComposeFactory:
    __slots__ = ('name', 'elements', '_quantity', 'parent')
    data = None

    def __init__(
            self,
            name: str,
            elements: List[Dict],
            parent: Ingredient = None
    ):
        self.name = name
        self.elements = elements
        self._quantity = 1
        self.parent = parent

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    def create(self) -> Ingredient:
        compose = None
        for _ in range(self.quantity):
            compose = Composite(self.name, parent=self.parent)
            for element in self.elements:
                name, quantity, klass = element.values()
                for _ in range(quantity):
                    if klass == self.__class__:
                        compose.add(klass(**self.data[name], parent=compose).create())
                    else:
                        compose.add(klass(name, parent=compose))
        return compose

    @classmethod
    def set_data(cls, data):
        cls.data = data

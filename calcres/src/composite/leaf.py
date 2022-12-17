from __future__ import annotations
from typing import Any
from .abstract import Ingredient


__all__ = ('Leaf',)


class Leaf(Ingredient):
    def contains(self) -> Any:
        return self.name

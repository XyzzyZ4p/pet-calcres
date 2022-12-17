from __future__ import annotations
from typing import List, Any, Optional
from .abstract import Ingredient
from io import StringIO


__all__ = ('Composite',)


class Composite(Ingredient):
    __slots__ = ('name', 'counter', 'parent', 'container')

    def __init__(
            self,
            name: str,
            parent: Optional[Ingredient] = None,
            *args,
            **kwargs
    ):
        super().__init__(name, parent, *args, **kwargs)
        self.container: List = []

    def add(self, ingredient: Ingredient) -> None:
        if ingredient not in self.container:
            self.container.append(ingredient)
        self.counter.update([ingredient.name])

    def contains(self) -> Any:
        data = dict(
            name=self.name,
            quantity=type(self).instances[f'{self.name}:{self.parent}']['quantity'],
            ingredients=[dict(name=name, quantity=quantity) for name, quantity in self.counter.items()]
        )

        for el in self.container:
            content = el.contains()
            if not isinstance(content, str):
                for idx, ingredient in enumerate(data['ingredients']):
                    if ingredient['name'] == content['name']:
                        data['ingredients'][idx]['ingredients'] = content['ingredients']
        return data

    def structure(self, output: Optional[StringIO] = None, indent: int = 0) -> None:
        quantity = type(self).instances[f'{self.name}:{self.parent}']['quantity']
        print(f'{"":>{indent}}{self.name} : {quantity} -> {dict(self.counter)}', file=output, flush=True)
        for el in self.container:
            el.structure(output=output, indent=indent + 4)

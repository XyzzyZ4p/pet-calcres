from __future__ import annotations
from abc import ABCMeta


__all__ = ('ABCMetaSingleton',)


class ABCMetaSingleton(ABCMeta):
    instances = {}

    def __call__(cls, name, parent, *args, **kwargs):
        if f'{name}:{parent}' not in cls.instances.keys():
            cls.instances[f'{name}:{parent}'] = dict(
                instance=super(ABCMetaSingleton, cls).__call__(name, parent, *args, **kwargs),
                quantity=0
            )

        instance = cls.instances[f'{name}:{parent}']['instance']
        cls.instances[f'{name}:{parent}']['quantity'] += 1
        return instance

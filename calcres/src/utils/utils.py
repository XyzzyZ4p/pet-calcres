from __future__ import annotations
from pathlib import Path
from typing import Dict
from json import load
from yaml import safe_load
from ..composite import Leaf
from ..factory import ComposeFactory


__all__ = ('read_settings', 'read_data', 'configurate_data')


def read_settings(path: Path) -> Dict:
    with open(path, 'r', encoding='utf-8') as fp:
        data = safe_load(fp)
    return data


def read_data(path: Path) -> Dict:
    with open(path, 'r', encoding='utf-8') as fp:
        data = load(fp)
    for k, v in data.items():
        for idx, el in enumerate(v['elements']):
            if el['name'] in data.keys():
                klass = ComposeFactory
            else:
                klass = Leaf
            data[k]['elements'][idx]['klass'] = klass
    return data


def configurate_data(data):
    ComposeFactory.set_data(data)

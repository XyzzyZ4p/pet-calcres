from typing import Dict, Tuple
from io import StringIO
from pathlib import Path
from ..utils import read_data, read_settings, configurate_data
from ..factory import ComposeFactory
from ..composite import Ingredient


__all__ = ('configure_app', 'calculate')


def configure_app(root: Path, conf: Path) -> Dict:
    settings = read_settings(conf)
    data = read_data(settings['data'].format(ROOT=root))
    configurate_data(data)
    return data


def calculate(name: str, quantity: int, data: Dict) -> Tuple[str, str, Dict]:
    element = data[name]
    factory = ComposeFactory(**element)
    factory.quantity = quantity
    component = factory.create()
    linearize = Ingredient.linearize_content(component.contains())
    output = StringIO()
    component.structure(output=output)
    structure = output.getvalue()
    output.close()
    return name, structure, linearize

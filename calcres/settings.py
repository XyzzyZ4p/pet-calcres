import sys
from pathlib import Path

ROOT = Path(__file__).parents[1]
sys.path.append(str(ROOT))
CONF_PATH = ROOT / 'conf.yaml'

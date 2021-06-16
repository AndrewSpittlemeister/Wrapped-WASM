import os
import sys
from pathlib import Path

sys.path.append(str(Path(os.path.dirname(os.path.realpath(__file__))).resolve()))

import wasmtime.loader

from mylib_rs import add_one

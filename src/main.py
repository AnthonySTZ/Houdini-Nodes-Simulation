import os
import sys

plugin_path = os.environ["HOUDINI_SPRING_NODES_PATH"]

sys.path.insert(0, plugin_path)

import load_plugin
from importlib import reload

reload(load_plugin)

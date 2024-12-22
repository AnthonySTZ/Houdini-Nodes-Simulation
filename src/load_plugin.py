import os
import sys

plugin_path = os.environ["HOUDINI_SPRING_NODES_PATH"]

sys.path.insert(0, plugin_path)

import spring.plugin as plugin
from importlib import reload

reload(plugin)

plugin.run()

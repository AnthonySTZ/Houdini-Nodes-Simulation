import os
import sys

plugin_path = os.environ["HOUDINI_SPRING_NODES_PATH"]

sys.path.insert(0, plugin_path)

import spring.simulation as simulation
import spring.interface as interface
import spring.plugin as plugin
from importlib import reload

reload(simulation)
reload(interface)
reload(plugin)

plugin.run()

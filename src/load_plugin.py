import os
import sys

plugin_path = os.environ["HOUDINI_SPRING_NODES_PATH"]

sys.path.insert(0, plugin_path)

import spring.nodes as nodes
import spring.math as math
import spring.particle as particle
import spring.spring as spring
import spring.world as world
import spring.simulation as simulation
import spring.interface as interface
import spring.plugin as plugin
from importlib import reload

reload(nodes)
reload(math)
reload(particle)
reload(spring)
reload(world)
reload(simulation)
reload(interface)
reload(plugin)

plugin.run()

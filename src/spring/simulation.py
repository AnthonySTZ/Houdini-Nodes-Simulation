import time
import threading
import spring.nodes as nodes
from spring.world import World

thread = False


def simulate() -> None:

    # Create world
    world: World = World()
    selected_nodes: list = nodes.get_selected_nodes()
    world.add_particles(selected_nodes)
    anchor_nodes: list = nodes.get_anchor_nodes(selected_nodes)
    world.add_anchors(anchor_nodes)

    i = 0
    global thread
    while thread and i < 10:
        print(f"{i} seconds")
        time.sleep(1)
        i += 1


def start_simulation() -> None:
    print("Simulating the process...")

    global thread
    thread = True
    threading.Thread(target=simulate, daemon=True).start()


def stop_simulation() -> None:
    global thread
    thread = False
    print("Simulation stopped.")

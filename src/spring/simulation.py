import time
import threading
import spring.nodes as nodes
from spring.world import World
from spring.spring import Spring

thread = False


def simulate() -> None:

    # Create world
    world: World = World()
    selected_nodes: list = nodes.get_selected_nodes()
    world.add_particles(selected_nodes)
    anchor_nodes: list = nodes.get_anchor_nodes(selected_nodes)
    world.add_anchors(anchor_nodes)
    spring: Spring = Spring(0.5, 5, world.particles[0], world.particles[1])
    world.add_springs([spring])

    start_time = time.time()
    previous_time = start_time
    duration = 50
    delta_time = 0
    global thread
    while thread:
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time > duration:
            thread = False
            break

        delta_time = current_time - previous_time
        world.update(delta_time)
        previous_time = current_time


def start_simulation() -> None:
    # print("Simulating the process...")

    global thread
    thread = True
    threading.Thread(target=simulate, daemon=True).start()


def stop_simulation() -> None:
    global thread
    thread = False
    # print("Simulation stopped.")

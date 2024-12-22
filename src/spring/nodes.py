import hou  # type: ignore
from spring.spring import Spring
from spring.particle import Particle


def get_selected_nodes() -> list[hou.Node]:
    selected_nodes: list[hou.Node] = hou.selectedNodes()
    if not selected_nodes:
        raise ValueError("No nodes selected")
    return selected_nodes


def get_anchor_nodes(selected_nodes: list[hou.Node]) -> list[hou.Node]:
    anchor_nodes = []
    for node in selected_nodes:
        for input_node in node.inputs():
            if not input_node:
                continue
            if input_node not in selected_nodes:
                anchor_nodes.append(input_node)
    return anchor_nodes


def get_springs(
    particles: dict[hou.Node, Particle], stiffness: float, restlength: float
) -> list[Spring]:
    springs = []
    for particle_node in particles:
        for input_node in particles[particle_node].node.inputs():
            if input_node in particles:
                particle_a = particles[input_node]
                particle_b = particles[particle_node]
                springs.append(
                    Spring(
                        stiffness,
                        restlength,
                        particle_a,
                        particle_b,
                    )
                )
    return springs

import hou  # type: ignore


def get_selected_nodes() -> list[hou.Node]:
    selected_nodes: list[hou.Node] = hou.selectedNodes()
    if not selected_nodes:
        raise ValueError("No nodes selected")
    return selected_nodes


def get_anchor_nodes(selected_nodes: list[hou.Node]) -> list[hou.Node]:
    anchor_nodes = []
    for node in selected_nodes:
        for input_node in node.inputs():
            if input_node not in selected_nodes:
                anchor_nodes.append(input_node)
    return anchor_nodes

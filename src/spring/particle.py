from spring.math import Vector2
import hou  # type: ignore


class Particle:
    def __init__(self, node) -> None:
        self.node = node
        self.position = Vector2(node.position().x(), node.position().y())
        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        self.is_anchor = False

    def apply_force(self, force: Vector2) -> None:
        self.acceleration += force

    def update(self, gravity: float, dt: float) -> None:
        if self.is_anchor:
            return
        self.velocity += (self.acceleration + gravity) * dt
        self.position += self.velocity * dt
        self.velocity *= 0.9997  # damping
        self.acceleration *= 0
        self.node.setPosition(hou.Vector2(self.position.x, self.position.y))

    def update_user_position(self) -> None:
        self.position = Vector2(self.node.position().x(), self.node.position().y())

from spring.math import Vector2


class Particle:
    def __init__(self, node) -> None:
        self.position = Vector2(node.position().x, node.position().y)
        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        self.is_anchor = False

    def apply_force(self, force: Vector2) -> None:
        self.acceleration += force

    def update(self, dt: float) -> None:
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt
        self.acceleration *= 0

from spring.math import Vector2


class Particles:
    def __init__(self, x: float, y: float) -> None:
        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
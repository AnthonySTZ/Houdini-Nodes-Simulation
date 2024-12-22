from spring.particle import Particle
from spring.math import Vector2


class Spring:
    def __init__(
        self,
        stiffness: float,
        restlength: float,
        particle_a: Particle,
        particle_b: Particle,
    ) -> None:
        self.stiffness = stiffness
        self.restlength = restlength
        self.particle_a = particle_a
        self.particle_b = particle_b

    def update(self) -> None:
        displacement: Vector2 = self.particle_b.position - self.particle_a.position
        distance: float = displacement.length() - self.restlength
        direction: Vector2 = displacement.normalize()
        force: Vector2 = direction * (-self.stiffness * distance)
        self.particle_a.apply_force(-force)
        self.particle_b.apply_force(force)

from spring.particle import Particle


class Spring:
    def __init__(
        self, stiffness: float, particle_a: Particle, particle_b: Particle
    ) -> None:
        self.stiffness = stiffness
        self.particle_a = particle_a
        self.particle_b = particle_b

    def update(self, dt: float) -> None:
        pass

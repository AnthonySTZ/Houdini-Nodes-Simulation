from spring.particle import Particle
from spring.spring import Spring


class World:
    def __init__(self) -> None:
        self.particles: list[Particle] = []
        self.springs: list[Spring] = []

    def add_particles(self, particles: list) -> None:
        for particle in particles:
            self.particles.append(Particle(particle))

    def add_anchors(self, anchors: list) -> None:
        for anchor in anchors:
            particle = Particle(anchor)
            particle.is_anchor = True
            self.particles.append(particle)

    def add_springs(self, springs: list) -> None:
        for spring in springs:
            self.springs.append(spring)

    def update(self, dt: float) -> None:
        if dt > 0:
            for spring in self.springs:
                spring.update()
            for particle in self.particles:
                particle.update(dt)

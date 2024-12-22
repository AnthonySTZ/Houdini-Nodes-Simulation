from spring.particle import Particle
from spring.spring import Spring
from spring.math import Vector2


class World:
    def __init__(self) -> None:
        self.particles: dict = {}
        self.springs: list[Spring] = []
        self.gravity = Vector2(0, -3)

    def add_particles(self, particles: list) -> None:
        for particle in particles:
            self.particles[particle] = Particle(particle)

    def add_anchors(self, anchors: list) -> None:
        for anchor in anchors:
            particle = Particle(anchor)
            particle.is_anchor = True
            self.particles[anchor] = particle

    def add_springs(self, springs: list) -> None:
        for spring in springs:
            self.springs.append(spring)

    def update(self, dt: float) -> None:
        if dt > 0:
            for particle in self.particles.values():
                particle.update_user_position()
            for spring in self.springs:
                spring.update()
            for particle in self.particles.values():
                particle.update(self.gravity, dt)

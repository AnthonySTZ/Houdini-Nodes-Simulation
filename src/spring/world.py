from spring.particle import Particle
from spring.spring import Spring
from spring.math import Vector2


class World:
    def __init__(self) -> None:
        self.particles: dict[any, Particle] = {}
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
            self.check_collision()
            for spring in self.springs:
                spring.update()
            for particle in self.particles.values():
                particle.update(self.gravity, dt)

    def check_collision(self) -> None:
        node_radius: float = 0.6
        for particle in self.particles.values():
            for particle_other in self.particles.values():
                if particle == particle_other:
                    continue
                distance = particle.node.position().distanceTo(
                    particle_other.node.position()
                )
                if distance < node_radius:
                    direction = (
                        particle_other.position - particle.position
                    ).normalize()
                    push_vector = direction * (node_radius - distance)
                    particle.position -= push_vector
                    particle_other.position += push_vector

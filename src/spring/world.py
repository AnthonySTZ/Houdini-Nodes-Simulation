from spring.particle import Particle


class World:
    def __init__(self) -> None:
        self.particles = []
        self.springs = []

    def add_particles(self, particles: list) -> None:
        for particle in particles:
            self.particles.append(Particle(particle))

    def add_anchors(self, anchors: list) -> None:
        for anchor in anchors:
            particle = Particle(anchor)
            particle.is_anchor = True
            self.particles.append(particle)

    def update(self, dt: float) -> None:
        if dt > 0:
            print(f"FPS : {1/dt}")

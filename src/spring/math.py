class Vector2:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def length(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def normalize(self) -> "Vector2":
        length = self.length()
        return (
            Vector2(self.x / length, self.y / length) if length > 0 else Vector2(0, 0)
        )

    def __add__(self, other: "Vector2") -> "Vector2":
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector2") -> "Vector2":
        return Vector2(self.x - other.x, self.y - other.y)

    def __neg__(self) -> "Vector2":
        return Vector2(-self.x, -self.y)

    def __mul__(self, scalar: float) -> "Vector2":
        return Vector2(self.x * scalar, self.y * scalar)

class Vector2:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    @property
    def length(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def __add__(self, other: "Vector2") -> "Vector2":
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector2") -> "Vector2":
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Vector2":
        return Vector2(self.x * scalar, self.y * scalar)

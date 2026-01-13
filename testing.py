class Circle:
    def __init__(self, radius=1):
        self._radius = radius

    def __eq__(self, other) -> bool:
        return self._radius == other._radius
    
c = Circle(5)
print(result = (c == 5)
# file: sc_13_07_read_only_property.py
class Circle:
    def __init__(self, radius):
        # Validering ved konstruksjon (read-only etterpå)
        if radius < 0 or radius > 99:
            raise ValueError(f"Invalid radius {radius}")
        self._radius = radius

    @property
    def radius(self):  # Getter for radius (read-only)
        return self._radius

# Prøv Circle (read-only property)
try:
    c1 = Circle(10)
    print(c1.radius)  # property-getter blir kalt
    # Forsøk på å sette ny radius feiler fordi property er read-only
    c1.radius = 20
except AttributeError as ex:
    print("AttributeError:", ex)

# Ugyldig konstruksjon (validering i __init__)
try:
    c2 = Circle(-2)
except ValueError as ex:
    print("ValueError:", ex)
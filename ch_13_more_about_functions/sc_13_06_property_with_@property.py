# file: sc_13_06_descriptor_with_@property.py
# Circle-klasse med @property-decorator
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self): # Getter for radius
        return self._radius

    @radius.setter # Setter for radius
    def radius(self, radius):
        if radius < 0 or radius > 99:
            raise ValueError(f"Invalid radius {radius}")
        self._radius = radius

# Try Circle
try:
    c1 = Circle(10)
    print(c1.radius) # property-getter blir kalt
    c1.radius = 20  # property-setter blir kalt
    c1.radius = -2  # property-setter blir kalt (kaster ValueError)
except ValueError as ex:
    print("Exception: ",ex)
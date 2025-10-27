# file: sc_13_05_property_basic.py
# Circle klasse med property, men ikke @property decorator
class Circle:
    def __init__(self, radius):
        self.radius = radius # setter called, creates _radius attribute
    
    def _set_radius(self, radius): # setter for radius
        if radius < 0 or radius > 99:
            raise ValueError(f'Invalid radius {radius}')
        self._radius = radius # create _radius attribute
    
    def _get_radius(self): # Getter for radius
        return self._radius

    radius = property(_get_radius, _set_radius) # Lag property radius

# Try Circle
try:
    c1 = Circle(10)
    print(c1.radius) # _get_radius() blir kalt
    c1.radius = 20 # _set_radius() blir kalt
    c1.radius = -2 # _set_radius() blir kalt
except ValueError as ex:
    print("Exception: ",ex)
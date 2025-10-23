# file sc_10_06_multilpe_inheritance2.py
class A:
    def __init__(self):
        self.value = "A's value"
        super().__init__()  # Kaller neste i MRO

class B:
    def __init__(self):
        self.value = "B's value"
        super().__init__()  # Kaller neste i MRO (object)

class C(A, B):
    def __init__(self):
        super().__init__()  # Følger MRO: C -> A -> B -> object
        # Gammel kode uten super():
        # A.__init__(self)
        # B.__init__(self)

    def show(self):
        print(self.value)

c = C()
c.show()  # Output: B's value
print(f"MRO: {C.__mro__}")  # Viser: C -> A -> B -> object

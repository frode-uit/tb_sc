# file: sc_08_10_overload_getitem1.py
class Ordre:
    def __init__(self, handlekurv, kunde):
        self.handlekurv = list(handlekurv)
        self.kunde = kunde

    def __getitem__(self, key):
        return self.handlekurv[key]

ordre = Ordre(['Zalo', 'Eple', 'Deodorant'], 'Hansen')

print(ordre[0])       # Zalo
print(ordre[-1])      # Deodorant
print(ordre[0:2])     # ['Zalo', 'Eple']
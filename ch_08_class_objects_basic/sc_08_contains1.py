class Ordre:
    def __init__(self, handlekurv, kunde):
        self.handlekurv = list(handlekurv)
        self.kunde = kunde

    def __getitem__(self, key):
        return self.handlekurv[key]

    def __contains__(self, key):
        return key in self.handlekurv

ordre = Ordre(['Zalo', 'Eple', 'Deodorant'], 'Hansen')

if 'Zalo' in ordre:
    print("Zalo er i handlekurven")
class Atom():
    def __init__(self, electrons, protons):
        self.electrons = electrons  
        self.protons = protons

    def get_electrons(self):
        return self.electrons
    
    def get_protons(self):
        return self.protons

carbon = Atom(electrons = 6, protons = 6)
print(carbon.get_electrons())

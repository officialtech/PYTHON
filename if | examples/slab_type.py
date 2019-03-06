
print(15 * "*", r"r for residence", 15 * "*")
print(15 * "*", r"c for commercial", 15 * "*")
print(15 * "*", r"i for industry", 15 * "*")


class Slab:
    industry, commercial, residence = 5.25, 4.00, 3.08 #you can comment this and give directly values
    def __init__(self,name, slabType, slab_unit):
        self.name = name
        self.slabType = slabType
        self.slab_unit = slab_unit

    def calc(self):
        self.total = 0
        if self.slabType == 'r':
            self.total += (Slab.residence * self.slab_unit)
        elif self.slabType == 'c':
            self.total += (Slab.commercial * self.slab_unit)
        else:
            self.total += (Slab.industry * self.slab_unit)

    def show(self):
        print("Total Bill: ", self.total, "per unit")
        return "THANK-YOU"



name = input("Your Good Name: \n")
slabType = input("Slab Type: \n")
slab_unit = int(input("Number of units consumed: \n"))

so = Slab(name, slabType,slab_unit)
so.calc()
so.show()
#syntax
#class fish(animal):
#    def __init__(self):
#            super().__init__()

# EXAMPLE :

class animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale, exale.")

class fish(animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water")

x = fish()
x.swim()
x.breathe()
print(x.num_eyes)
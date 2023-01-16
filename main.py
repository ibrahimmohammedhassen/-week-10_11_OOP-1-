class person: #super/parent class
  def __init__(self, n, a, w):
    self.name = n
    self.age = a
    self.weight = w

  def display(self):
    print(f"{self.name} is {self.age} years old and weight {self.weight}kg.")

#alexandra = person("Alexandra", 23, 88)
#alexandra.disply()
class Doctor (person): #child/subclass
  def hospital(self):
    print("the doctor goes hospital 6 days a week.")
  pass
d = Doctor("Dr jones", 56, 65)
print(d.age)
d.display()
d.hospital()


class lecturer(person):
    peciality = "computer science"
    years0Experience = 8
    university = "solent"

    def lecture(self):
      print("the lecturer delivers lectures.")

l = lecturer("james",42, 70)
l.lecture()
l.display()
print(l.university)


class GP(Doctor):
  numberofregisteredpatient = 500

  def colleague(self):
    print("10 people workunder GP.")
gp = GP("Ahmed", 50, 76)
print(gp. numberofregisteredpatient)
gp.colleague()
gp.hospital()
gp.display
print(gp.name)






















  
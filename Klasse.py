class RechnenMitZweiZahlen:
  def __init__(self, z1, z2):
    self.z1 = z1
    self.z2 = z2

  def multiplikation(self):
    print(self.z1 * self.z2)
  
  def addition(self):
    print(self.z1 + self.z2)

obj = RechnenMitZweiZahlen(10, 36)
obj.multiplikation()
obj.addition()

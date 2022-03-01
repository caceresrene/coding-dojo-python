class Alumno:
  def __init__(self, name, lastName, email ):
    self.name = name
    self.lastName = lastName
    self.email = email
    self.count = 0
  def increaseCount(self, number):
    self.count += number
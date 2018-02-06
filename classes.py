class Triangle(object):
  
  number_of_sides = 3
  
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
  
  def check_angles(self):
    return self.angle1 + self.angle2 + self.angle3 == 180
  
my_triangle = Triangle(90, 30, 60)
print (my_triangle.number_of_sides)
print (my_triangle.check_angles())

class Equilateral(Triangle):
  
  angle = 60
  
  def __init__(self):
    self.angle1 = self.angle
    self.angle2 = self.angle
    self.angle3 = self.angle

my_equilateral = Equilateral()
print (my_equilateral.number_of_sides)
print (my_equilateral.check_angles())

class Point3D(object):
  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z
 
  def __repr__(self):
    return "(%d, %d, %d)" % (self.x, self.y, self.z)
  
my_point = Point3D(1,2,3)
print (my_point)

class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

class PartTimeEmployee(Employee):
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00
  
  def full_time_wage(self, hours):
    self.hours = hours
    return super(PartTimeEmployee, self).calculate_wage(hours)
  
milton = PartTimeEmployee("Milton")
print (milton.full_time_wage(10))
class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return 'Rectangle(width=' + str(self.width) + ', height=' + str(
      self.height) + ')'

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return ((self.width**2 + self.height**2)**.5)

  def get_picture(self):
    if (self.width > 50 or self.height > 50):
      return 'Too big for picture.'

    s = ''

    for line in range(self.height):
      for column in range(self.width):
        s += '*'

      s += '\n'

    return s

  def get_amount_inside(self, shape):
    return Rectangle.get_area(self) // Rectangle.get_area(shape)


class Square(Rectangle):

  def __init__(self, side):
    self.side = side
    self.width = side
    self.height = side

  def __str__(self):
    return 'Square(side=' + str(self.side) + ')'

  def set_side(self, side):
    self.side = side
    self.height = side
    self.width = side

  def set_height(self, height):
    self.set_side(height)

  def set_width(self, width):

    self.set_side(width)


rect = Rectangle(3, 6)
sq = Square(5)
rect.set_width(7)
rect.set_height(8)
sq.set_side(2)
actual = str(rect)
expected = "Rectangle(width=7, height=8)"
actual = str(sq)
expected = "Square(side=2)"
sq.set_width(4)
actual = str(sq)
expected = "Square(side=4)"
print(actual)

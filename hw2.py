
class Figure:
    unit = 'cm'
    def init(self):
        pass
    def calculate_area(self):
        pass
    def info(self):
        pass
class Square(Figure):
    def __init__(self, __length):
        super().__init__()
        self.__length = __length
    def calculate_area(self):

        return self.__length ** 2
    def info(self):
        return f"Square radius: {self.__length}{self.unit}, area: {self.calculate_area()}{self.unit}"

class Rectangle(Figure):
   def __init__(self, length, width):
       super().__init__()
       self.__lenght = length
       self.__width = width

   def calculate_area(self):
       return self.__lenght * self.__width

   def info(self):
       area = self.calculate_area()
       return f'Square side length: {self.__lenght}, {Figure.unit}, aarea: {area}{Figure.unit}'

if __name__ == "__main__":
    square1 = Square(5)
    square2 = Square(7)

    rectangle1 = Rectangle(5, 8)
    rectangle2 = Rectangle(10, 4)
    rectangle3 = Rectangle(6, 3)

    figures = [square1, square2, rectangle1, rectangle2, rectangle3]

    for figure in figures:
        print(figure.info())




print("Hello world!")

print("Updated from main")

# import math
#
# class Shape:
#     def calculate_area(self):
#         pass
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def calculate_area(self):
#         return self.width * self.height
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calculate_area(self):
#         return math.pi * self.radius ** 2
#
# class RightTriangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#
#     def calculate_area(self):
#         return 0.5 * self.base * self.height
#
# class Trapezoid(Shape):
#     def __init__(self, base1, base2, height):
#         self.base1 = base1
#         self.base2 = base2
#         self.height = height
#
#     def calculate_area(self):
#         return 0.5 * (self.base1 + self.base2) * self.height
#
#
# rectangle = Rectangle(5, 10)
# print("Площадь прямоугольника:", rectangle.calculate_area())
#
# circle = Circle(3)
# print("Площадь круга:", circle.calculate_area())
#
# triangle = RightTriangle(4, 6)
# print("Площадь прямоугольного треугольника:", triangle.calculate_area())
#
# trapezoid = Trapezoid(2, 4, 3)
# print("Площадь трапеции:", trapezoid.calculate_area())


# 2


# import math
#
# class Shape:
#     def calculate_area(self):
#         pass
#
#     def __int__(self):
#         return self.calculate_area()
#
#     def __str__(self):
#         return f"Это фигура"
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def calculate_area(self):
#         return self.width * self.height
#
#     def __str__(self):
#         return f"Прямоугольник: ширина={self.width}, высота={self.height}"
#
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calculate_area(self):
#         return math.pi * self.radius ** 2
#
#     def __str__(self):
#         return f"Круг: радиус={self.radius}"
#
# class RightTriangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#
#     def calculate_area(self):
#         return 0.5 * self.base * self.height
#
#     def __str__(self):
#         return f"Прямоугольный треугольник: основание={self.base}, высота={self.height}"
#
# class Trapezoid(Shape):
#     def __init__(self, base1, base2, height):
#         self.base1 = base1
#         self.base2 = base2
#         self.height = height
#
#     def calculate_area(self):
#         return 0.5 * (self.base1 + self.base2) * self.height
#
#
#     def __str__(self):
#         return f"Трапеция: основание1={self.base1}, основание2={self.base2}, высота={self.height}"
#
#
# rectangle = Rectangle(5, 10)
# print(int(rectangle))
# print(str(rectangle))
#
#
# circle = Circle(3)
# print(int(circle))
# print(str(circle))
#
# triangle = RightTriangle(4, 6)
# print(int(triangle))
# print(str(triangle))
#
# trapezoid = Trapezoid(2, 4, 3)
# print(int(trapezoid))
# print(str(trapezoid))



# 3


import pickle

# class Shape:
#     def __init__(self):
#         pass
#
#     def Show(self):
#         pass
#
#     def Save(self, filename):
#         with open(filename, 'wb') as file:
#             pickle.dump(self, file)
#
#     @classmethod
#     def Load(cls, filename):
#         with open(filename, 'rb') as file:
#             return pickle.load(file)
#
# class Square(Shape):
#     def __init__(self, x, y, side_length):
#         self.x = x
#         self.y = y
#         self.side_length = side_length
#
#     def Show(self):
#         print(f"Квадрат: левый верхний угол ({self.x}, {self.y}), длина стороны {self.side_length}")
#
#
# import pickle
#
# class Shape:
#     def __init__(self):
#         pass
#
#     def Show(self):
#         pass
#
#     def Save(self, filename):
#         with open(filename, 'wb') as file:
#             pickle.dump(self, file)
#
#     @classmethod
#     def Load(cls, filename):
#         with open(filename, 'rb') as file:
#             return pickle.load(file)
#
# class Square(Shape):
#     def __init__(self, x, y, side_length):
#         self.x = x
#         self.y = y
#         self.side_length = side_length
#
#     def Show(self):
#         print(f"Квадрат: левый верхний угол ({self.x}, {self.y}), длина стороны {self.side_length}")
#
# class Rectangle(Shape):
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#
#     def Show(self):
#         print(f"Прямоугольник: левый верхний угол ({self.x}, {self.y}), ширина {self.width}, высота {self.height}")
#
# class Circle(Shape):
#     def __init__(self, center_x, center_y, radius):
#         self.center_x = center_x
#         self.center_y = center_y
#         self.radius = radius
#
#     def Show(self):
#         print(f"Окружность: центр ({self.center_x}, {self.center_y}), радиус {self.radius}")
#
# class Ellipse(Shape):
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#
#     def Show(self):
#         print(f"Эллипс: верхний угол ({self.x}, {self.y}), ширина {self.width}, высота {self.height}")
#
# # Создание списка фигур
# shapes = [
#     Square(0, 0, 5),
#     Rectangle(2, 2, 6, 4),
#     Circle(1, 1, 3),
#     Ellipse(3, 3, 5, 2)
# ]
#
# # Сохранение фигур в файл
# with open('shapes_data.pkl', 'wb') as file:
#     pickle.dump(shapes, file)
#
# # Загрузка фигур из файла в другой список
# with open('shapes_data.pkl', 'rb') as file:
#     loaded_shapes = pickle.load(file)
#
# # Отображение информации о каждой из фигур
# for shape in loaded_shapes:
#     shape.Show()
def area(length, width=None):
    if width is None:
        width = length
        area = length * width
        return area
rectangular_area = area(60, 9)
square_area = area(9)
print("area of rectagle:",rectangular_area)
print("area of square:",square_area)

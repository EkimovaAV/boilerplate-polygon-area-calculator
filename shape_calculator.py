'''set_width
set_height
get_area: Returns area (width * height)
get_perimeter: Returns perimeter (2 * width + 2 * height)
get_diagonal: Returns diagonal ((width ** 2 + height ** 2) ** .5)
get_picture: Returns a string that represents the shape using lines of "*". The number of lines should be equal to the height and the number of "*" in each line should be equal to the width. There should be a new line (\n) at the end of each line. If the width or height is larger than 50, this should return the string: "Too big for picture.".
get_amount_inside: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
'''
class Rectangle:
    def __init__(self, width=5, height=10):
        self.height = height
        self.width = width
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def get_area(self):
        area=self.width*self.height
        return area
    def get_perimeter(self):
        perimeter = 2*self.width + 2 * self.height
        return perimeter
    def get_diagonal(self):
        dia=((self.width ** 2 + self.height ** 2) ** .5)
        return dia

    def get_picture(self):
        pict=''
        if self.width >50 or  self.height > 50:
            return "Too big for picture."
        for i in range(self.height):
            pict+= '*'* self.width+ '\n'
        return(pict)
    def get_amount_inside(self, shape):
        amount = round(self.height / shape.height) * round(self.width / shape.width)
        return amount
    def __str__(self):
        rect = F"Rectangle(width={self.width}, height={self.height})"
        return rect
class Square(Rectangle):
    def __init__(self, s):
        super().__init__(s, s)

    def set_side(self, s):
        self.width = s
        self.height = s

    def set_width(self, s):
        self.set_side(s)

    def set_height(self, s):
        self.set_side(s)

    def __str__(self):
        sq = F"Square(side={self.height})"
        return sq

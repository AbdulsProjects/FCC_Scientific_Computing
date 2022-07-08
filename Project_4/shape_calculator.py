class Rectangle:
    
    #Class constructor
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = 0.0
        self.perimeter = 0.0
        self.diagonal = 0.0
    
    #Redefines the object width
    def set_width(self, width):
        self.width = width
        
        #Changes height if object is square
        if isinstance(self, Square):
            self.height = width
            
        
    #Redefines the object height
    def set_height(self, height):
        self.height = height
    
        #Changes width if object is square
        if isinstance(self, Square):
            self.width = height
    
    
    #Returns object area
    def get_area(self):
        self.area = self.width * self.height
        return self.area
        
    
    #Returns object perimeter
    def get_perimeter(self):
        self.perimeter = self.width * 2 + self.height * 2
        return self.perimeter

    
    #Returns object diagonal
    def get_diagonal(self):
        self.diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return self.diagonal

    
    #Creates a visual representation of the object
    def get_picture(self):
        
        #Object too large
        if self.height > 50 or self.width > 50:
            return ("Too big for picture.")
        
        #Object correct size
        else:
            picture = ""
            #Sets number of rows equal to height
            for row in range(self.height):
                #Sets number of columns equal to width
                picture += ''.ljust(self.width, "*")
                #Adds new line
                picture += '\n'
            
            return picture
          
    
    #Changes the print representation of the object
    def __str__(self):
        
        #Square object
        if self.width == self.height:
            #Sets the value for the returned string
            output = f'Square(side={self.height})'
        
        #Rectangular object
        else:
            #sets the value for the returned string
            output = f'Rectangle(width={self.width}, height={self.height})'
        
        return output
      
    
    #Identifies how many times a second object could fit into the first
    def get_amount_inside(self, shape):
        #Calculates how many times the second object's width / height could fit into the first
        width_fit = int(self.width / shape.width) 
        height_fit = int(self.height / shape.height)
        #Calculates how many times object 2 can fit into object 1
        total_fit = width_fit * height_fit
        return total_fit
            
            
class Square(Rectangle):
    
    #Subclass constructor
    def __init__(self, side):
        self.width = side
        self.height = side
    
    
    #Changes both the width and height of the square
    def set_side(self, side):
        self.width = side
        self.height = side        

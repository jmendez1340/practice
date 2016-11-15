class Office_furniture(object):
    """
    This class defines a generic animal object

    Attributes: Material, Length, Width, Height, Price, Cuteness
    """

    def __init__(self, material, length, width, height, price, cute):
        self.material = material
        self.length = length
        self.width = width
        self.height = height
        self.price = price
        self.cute = cute

        # next we will use sets followed by gets afterwards

        def set_material(self,material):
            self.__material = material      # don't forget to make it hidden!

        def set_length(self, length):
            self.__length = length

        def set_width(self, width):
            self.__width = width

        def set_height(self, height):
            self.__height = height

        def set_price(self, price):
            self.__price = price

        def set_cute(self, cute):
            self.__cute = cute

        # Now we use get

        def get_material(self):
            return self.__material

        def get_length(self):
            return self.__length

        def get_width(self):
            return self.__width

        def get_height(self):
            return self.__height

        def get_price(self):
            return self.__price

        def get_cute(self):
            return self.__cute

        def __str__(self):
            if self.__price:
                return '{0}s are domestic {1}s.'.format\
                    (self.__material, self.__length,self.__width, self.__height, self.__cute)
            else:
                return '{0}s are wild {1}s.'.format\
                    (self.__material, self.__length,self.__width, self.__height, self.__cute)

class desk(Office_furniture):
    """
    attributes: name, breed
    inherited attribute: drawer_location, number_drawers
    """

    def __init__(self, drawer_location, number_drawers):
        Office_furniture.__init__(self,'wood','35in', '30in', '15in', '$40', 'Yes') # this statement inits parent attribute
        self.__drawer_location = drawer_location
        self.__number_drawers = number_drawers

    # this method overrides the parent class method
    def __str__(self):
        desc = 'On the {0} there are {1) drawers'.format(self.__drawer_location, self.__number_drawers)
        desc += Office_furniture.__str__(self)
        return desc

    def set_drawer_location(self, drawer_location):
        self.__drawer_location = drawer_location

    def get_drawer_location(self):
        self.__drawer_location

    def set_number_drawers(self, number_drawers):
        self.__number_drawers = number_drawers

    def get_number_drawers(self):
        self.__number_drawers
__author__ = 'admin'

# class Submarine(object):
#     my_attrs = ['color', 'year', 'name']
#
#     def __init__(self, color, year, name):
#         self.color = color
#         self.year = year
#         self.name = name
#
# class Tank(object):
#     my_attrs = ['weight', 'year', 'identifier']
#
#     def __init__(self, weight, year, identifier):
#         self.weight = weight
#         self.year = year
#         self.identifier = identifier

class AttributeInitType(type):
    def __call__(self, *args, **kwargs):

        obj = type.__call__(self, *args)

        for name, value in kwargs.items():
            setattr(obj, name, value)

        return obj

class Submarine(object, metaclass=AttributeInitType):
    my_attrs = ['color', 'year', 'name']

class Tank(object, metaclass=AttributeInitType):
    my_attrs = ['weight', 'year', 'identifier']

sub = Submarine(name="Narwal", year=2000, color="Black")
tank = Tank(weight=5000, year=1956, identifier="AXAXAX123")
print(tank.weight)
import types

class MyMathClass():
    def add(self, x, y):
        return x + y

    def monkey_path_adder(self):
        old_add = self.add

        def more_powerful_add(self, x, y):
            return old_add(x, y) + 1

        self.add = types.MethodType(more_powerful_add, self)

my_math = MyMathClass()
my_math.add(3, 3)

my_math.monkey_path_adder()
my_math.monkey_path_adder()
my_math.monkey_path_adder()
my_math.monkey_path_adder()

print(my_math.add(3,3))
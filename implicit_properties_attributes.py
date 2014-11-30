def test_method(): print("Just a test!")

class ExampleMetaClass(type):
    @classmethod
    def __prepare__(cls, name, baseClasses):
        print("In: __prepare__")
        return {'test_method': test_method}

    def __new__(cls, name, baseClasses, theDictionary):
        print("In: __new__")
        return type.__new__(cls, name, baseClasses, theDictionary)

class ExampleClass(metaclass=ExampleMetaClass):
    def __init__(self):
        print("In: __init__")
        pass
    exampleObject = "Just a test object"

example = ExampleClass()
print(example.exampleObject)
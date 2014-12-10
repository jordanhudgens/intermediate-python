import re

class FindMySkywalker:
    def __init__(self, arrayToSearch):
        self.i = 0
        self.n = len(arrayToSearch)
        self.arrayToSearch = arrayToSearch

    def __iter__(self):
        return self

    def next(self):
        if self.i <= self.n:
            i = self.i
            if re.search(r".*Skywalker.*", self.arrayToSearch[i]):
                print("Match Found at element", i, "with:", self.arrayToSearch[i])
            else:
                print("No match found at element", i, ".")
            self.i += 1
            return self.arrayToSearch[i]
        else:
            raise StopIteration()

stringArray = ['Han Solo', 'Luke Skywalker', 'Anakin Skywalker', 'R2D2']
s = FindMySkywalker(stringArray)

s.next()
s.next()
s.next()
s.next()
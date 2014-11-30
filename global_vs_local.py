spam = "test spam"

def do_local():
    spam = "local spam"
    print(spam)

def do_global():
    global spam
    spam = "global spam"

print(spam)

do_local()
print("After local assignment: ", spam)

do_global()
print("After global assignment: ", spam)
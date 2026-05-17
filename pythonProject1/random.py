import random
import inspect
import sys

def first_func():
    pass

class Human:
    pass

r = random
first_f = first_func
nick = Human


print(random.__name__)
print(r.__name__)
print(first_func.__name__)
print(first_f.__name__)
print(Human.__name__)
print(nick.__name__)

print(inspect.ismodule(random))
print(inspect.isclass(random))
print(inspect.isfunction(random))



print(inspect.getmodule(list))



for module_name, module_path in sys.modules.items():
    print(module_name, module_path)
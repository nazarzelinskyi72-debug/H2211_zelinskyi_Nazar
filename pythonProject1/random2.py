import random

import inspect

print(inspect.ismodule(random))
print(inspect.isclass(random))
print(inspect.isfunction(random))



print(inspect.getmodule(list))
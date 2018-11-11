## Classes and OOP

- What is a class?
a class is a constructor for objects (=the building blocks of python)

- How do you define a new class called `MyFirstClass`?
```py
class MyFirstClass():
    pass
```

- How do you create an object of the class `MyFirstClass`?
```py
class MyFirstClass():
    pass

mfc = MyFirstClass()
```

- What is instantiation?
The process of creating an object (=instance) of a class

- What are attributes?
Attributes are named elements that are part of a class

- What does it mean when an object is embedded?
It means that it is an attribute of another object. Example:
```py
class Rectangle():
    self.corner = Point()
```
An object that contains another object is called a **compound object**

- What is the difference between `copy.copy` and `copy.deepcopy`?
What do they each do?
Source: https://docs.python.org/3/library/copy.html
    * `copy.copy`: A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
    * `copy.deepcopy`: A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.

- What is the difference between a pure function and a modifier?
A modifier has "side effects" - it takes mutable arguments and changes them
during execution. A pure function does NOT do that. It uses only what
parameters you input, and does not change anything outside of the function
body.

- What is object-oriented programming?



## Methods

- What is a method?

- How is a method different than a function?

- What is invocation?

- What is the `__init__` method and what is it used for?

- Give an example `__init__` method for a `Car` class with attributes:
`make`, `model` and `year`.

- How do `__init__` methods handle variable arguments?

- What is the `__str__` method used for?

- How do you use a `__str__` method?

- What is operator overloading?

- What is an example of operator overloading?


## TYPE-BASED DISPATCH?

- What is polymorphism?

- Why is polymorphism beneficial?

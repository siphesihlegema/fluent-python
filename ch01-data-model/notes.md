# Python data Model

## Special Methods
- Special methods(dunder methods) are called by the python interpreter. 
- They are implemented in the class decleration and we invoke them in defferent ways.
- On safe simple way to invoke them is using built-in functions, wich are fast and do some other magic.
- The are also invoked through the python syntex and operarions e.g (for i in x:)

- Over all Special methods are realy cool and usefull, for example in things like
object reprentation, the method(__repr__) is called, if we implemented it in our class, it helps
us get a better formeted representation of the object.

- The python interpreter has its deteministic way of chossing with Special method to invoke
for example for boolean valuse. bool(x) calls x.__bool__(), if we did not
implement __bool__ python tries to call x.__len__(), wich return False for 0 else True.
- if all fails, all instances of user-defined classes are considerd True unless any of the
methods above a implemented.

## why len is not method

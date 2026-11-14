# Arrays and Sequences

## Tuples
in simle tuples are just imutable lists.
but ofcource its more complex then that.

### why Tuples are Not just imutable lists
- just like most Sequences in python, tuples dont store the catual values it holds
a contigous buffer but it stors references, adreeses or pointers to the actual values

- this means depending on the object if its mutable we can modify its values using
the adress out tuple is holding.
- But most importently the adress out tuple is holding does not change it always referencing
one single didtinct object.

## List Comprehension
- List comprrehension provides us an easily readable way or instantiating list objects.
- variables used in our Comprehension only exist in the lists local scope. if needed 
we can extend scope of variable using "Walrus operator" := and assign it to our
global variable

###  map and filter
- map and filter fuctions can do the same job as list comprehension, but 
insted or returning a full list they return an iterator.

- so normaly one might ask themselve why would we use listcomp insted of map and filter
arent they faster?

well is a bit complex
- map and filter are a bite faster then listcomp at least when working with
C built-in types becuse everything will be done using the underlying C.
- but with lamba or python functions, listcomp is actually fater becauce they avoid
a of function calls per iteration.

- the difference is not that big, so might as well use listcomp becauce 
it has better syntex. 

- besides if you really cared about performence might as well just use, generator
expretions, NumPy...

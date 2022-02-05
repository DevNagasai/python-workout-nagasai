# are variables really variables? or references to objects
# the following line creates a integer object,viz is an immutable data type.

x = 1000

# change value of x to 500, since integer object is immutable; python will point to the new value 500 and the previous value is no longer available.

x = 500

# now the value of x is 500 and the 1000 integer object will be collected by python garbage collector in some point of computation.

y = x

x = 3000



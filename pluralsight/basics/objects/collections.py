#tuple
# str
# range
# list
# dict
# set

t = ("Norway", 4.954, 3)
t[0]
len(t)
for item in t:
    print(item)

t+(338136, 26539)

t*3 # to repeat like a strip 

a = ((220, 284), (1184, 1210), (2620, 2924), (5020, 5564))
a[2]
a[2][1]

# single element tuple
h = (391)
h 
type(h) # gives int type not tuple

k = (391, )
k 
type(k)


e = () # to delcare an empty tuple, don't know what the use case becuase tuples are immutable. 

#declaring without paranthesis, makes pythin interpret it as a tuple, like this: 

p = 1,1,1,4,6,19

p
type(p)

def minmax(items):
    return min(items), max(items)

minmax([83,33,84,32,85,31,86])
# returns a tuple because the return statement in function definition has no data type but sperated by a comma. Hence it is defaultly considered as a tuple

# tuple unpacking
lower, upper = minmax([83,33,84,32,85,31,86])
lower # gets the first part of the min max output, tuple
upper # gets the second part of the min max output, tuple

# tuple unpacking with nested tuple unpacking

(a,(b,(c,d))) = (4,(3,(2,1)))
a # gets 4
b # gets 3
c # gets 2
d # gets 1

#swapping 
a = 'jelly'
b = 'bean'

a,b = b,a

#the default tuple function 

tuple([1,2,3,4,5])



####strings 
# homogeneous immutable sequence of characters

len("Length of a string")

# string concatenation
"New" + "found" + "land"


s = "New"
s+= "found"
s+="land"

# perform text join like in Sheets formulas
colors = ";".join(["#45ff23", "#2321fa", "#1298a3", "#a32312"])

# peform text split like in sheets formula
colors.split(";")

# text partitioning
"unforgetable".partition("forget") # yeilds ["un", "forget", "able"]

# using partition, strings can be unpacked individually 
departure, seperator, arrival = "London: Edinburgh".partition(":")

#string interpolation
"The age of {0} is {1}".format('Jim', 32)

"The age of {0} is {1}. {0}'s birthday is on {2}".format('Fred', 24, "October 31")

pos = (65.2, 23.1, 82.1)
"Galactic position x = {pos[0]} y = {pos[1]} z = {pos[2]}"

import math
"Math constants: pi = {m.pi}, e = {m.e}".format(m = math)

"Math constants: pi ={m.pi:.3f}, e = {m.e:.3f}".format( m= math)


# Range
#type of sequence representing arthmetic progression of integers

range(5) # this doesn't print 0 to 5, but this is an iterable

for i in range(5):
    print(i)

list(range(5,10))
list(range(0,10,step =1)) 

# providing one argument means stop 
# providing two argument means start,stop
# providing three arguments means start, stop and step

s = [0,1,3,6,13]
for i in range(len(s)): # unpythonic
    print(s[i])

for v in s: # use the iterator to iterate the iterable, do not include another iterable to get an iterable's values
    print(v)

t = [6,272,8862,14880, 2096886]
for p in enumerate(t): # enumerate introduces tuple in the loop by providing index along with the value in the iterable
     print(p) # prints index and value in a tuple

for index, p in enumerate(t): # gives the same result as above, but unpacks the tuple
    print(index, p) 

for i, v in enumerate(t): # elegance
    print("i = {1}, v = {}".format(i,v))

### List
# heterogeneous mutable sequence
s = "Show how to index into sequences".split()

s[3]# forward indexing
s[-4]# backward indexing
# backward indexing starts from -1 becuase there's no such thing as -0

s[1:4] # to slice list from element 2 uptil 4 but not the 4th element
s[3:] # slices values from 4th element to the last available element in the list

s[:3] # slices values upto 4th element but not the 4th element 

#copying lists copies shallow copies 
a = [[1,2],[3,4]]
b = a[:] # copies only the elements of 'a' 

a[0] = [8,9] # modifies a as a[[8,9],[3,4]] but doesn't change the values of b

# if compying is done like b =a, then modifying a will also modify b 

# list repetition 
c = [21,37]
d = c *4 # doing this won't change the values in c but only in d, when written directly with an '=' it makes a shallow copy 

# Repetition is shallow
s = [[-1, +1]]
t =  [[-1, +1]] * 5

s.append(1) # this appends a new value in s but not in t
t.append(1) # appends a new value in t but not in s

s[0].append(1) # appends 1 in all the elements as t as well


# list methods

w = "the quick brown fox jumps over the lazy dog".split()

w.index('fox') # givesa the index of fox
w.count('the') # counts the number of time 'the' is found in the list.
'the' in w # checks if the value is in the list and returns boolean answer
u = 'jackdaws love my big sphinx of squartz'.split()
# removing elements from the list
del u[3] # delete value based on index 
u.remove('jackdaws')  # remove is an built in function of list to remove elements from the list
u.remove[u.index('sphinx')] # remove using built-in index 
del u[u.index('quartz')] # delete using built-in index

# growing lists

m = [2,1,3]
n = [4,7,11]
k = m+n
k += [18, 29,47]
k.extend([76,])
# reverseing and sorting

g = [1,11,21,1211,112111]
g.reverse()
g.sort()
g.sort(reverse=True) # sorts in descending

h = 'not perplexing do handwriting family where I illegibly know doctors'.split()
h.sort(key= len) # sorts by length of the element in the list 
''.join(h)

x = [4,9,2,1]
y = sorted(x)
y = reversed(x) # gives an iterable to iterate over

# Dictionaries
urls ={'Google': 'https://google.com', 
        'Pluralsight': 'https://pluralsight.com',
        'Sixty North': 'http://sixty-north.com', 
        'Microsoft': 'http://microsoft.com'}

urls['Plural sight']

# keys are immubtale, values are mutable

names_and_ages = [('Alice', 32), ('Bob', 48), ('Charlie', 28), ('Daniel', 33)]
d = dict(names_and_ages) # converts list of tuples to dictionry with keys and values

phonetic = dict(a = 'alpha', b = 'bravo', c = 'charlie', d = 'delta', e = 'echo', f = 'foxtrot') # can be initialized by keyword arguments as well
d = dict(goldenrod = 0xDAA520, indigo = 0X4B0082, seashell = 0xFFF5EE)
e = d.copy() # shallow copies 

f = dict(e)
g = dict(wheat = 0xF5DEB3, khaki = 0xF0F68C, crimson = 0xDC143C)
f.update(g)

stocks = dict(goog = 891, aapl = 416, ibm = 194)

stocks.update(dict(goog = 123, yhoo = 245))

colors = dict(aquamarine = '#7FFFD4', burlywood = '#DEB887', chartreuse= '#7FFF00', cornflower = '#6495ED', firebrick = '#B03060', sienna = '#A0522D')

for key in colors: # iteration over a dictionary
    print("{key} => {value}".format (key = key, value = colors[key]))

for value in colors.values():
    print(value)

for key in colors.keys():
    print(key)

for key, value in colors.items(): # using tuple unpacking
    print("{key} => {value}".format(key = key, value = value))

symbols = dict(usd = '\u0024', gbp = '\u00a3', nzd = '\u0024', krw = '\u20a9', eur = '\u20ac', jpy = '\u00a5', nok ='kr', ils = '\u20aa', hhg = 'Pu')

'nzd' in symbols 
'mkd' in symbols






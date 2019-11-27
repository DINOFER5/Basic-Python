#!/usr/bin/env python
# coding: utf-8

# In[4]:


60*60*24*365.25


# In[5]:


l=[1,2,3,4,5,6,7,8,9,10]


# In[7]:


for i in range(len(l)):
    l[i]=l[i]*l[i]


# In[9]:


list=l[::-1]


# In[10]:


list


# In[75]:


l1=[1,2,3,4,5,6,7,8,9,10]


# In[76]:


pow=5

l1=[round((i**pow)-(i**(1/2))) for i in l1]

l1


# In[28]:


type(1/2)


# In[29]:


#number of minutes in a week
60*24*7


# In[31]:





# In[38]:


#getting reminder without modulus 2304811 divided by 47

def rem(a,b):
    return a-(a//b)*b

rem(2304811,47)


# In[45]:


#Task 3: Enter a Boolean expression to test whether the sum of 673 and 909 is divisible by 3.
def t3(a,b,c):
    if rem(a+b,c)==0:
        print("Divisible")
    else:
        print("Not divisible")
        


# In[55]:


#Task 4: Assign the value -9 to x and 1/2 to y. Predict the value of the following expression, then enter it
# to check your prediction:
# 2**(y+1/2) if x+10<0 else 2**(y-1/2)

def t4(a,b):
    n1=2**(b+1/2)
    n2=2**(b-1/2)
    if a+10<0:
        return n1
    else:
        return n2

t4(-9,1/2)


# In[57]:


#x3+y if x>y else y3+x
x=4
y=2
if x>y:
    print(x**3+y)
else:
    print(y**3+x)


# In[53]:


#Task 5: Write a comprehension over {1, 2, 3, 4, 5} whose value is the set consisting of the squares of the
# first five positive integers.
{i**2 for i in {1,2,3,4,5}}


# In[54]:


#Task 6: Write a comprehension over {0, 1, 2, 3, 4} whose value is the set consisting of the first five powers
# of two, starting with 2 power 0
{2**i for i in {0, 1, 2, 3, 4}}


# In[102]:


# Task 7: The value of the previous comprehension, {x*y for x in {1,2,3} for y in {2,3,4}}, is a
# seven-element set. Replace {1,2,3} and {2,3,4} with two other three-element sets so that the value
# becomes a nine-element set.

len({x*y for x in {2,4,7} for y in {2,3,9}})


# In[133]:


# Task 8: Replace {1,2,3} and {2,3,4} in the previous comprehension with 
# two disjoint (i.e. nonoverlapping) three-element sets so that the value becomes a five-element set.
set={x*y for x in {4,8,16} for y in {6,12,24}}
print(set)
len(set)


# In[156]:


[i for i in range(8)]


# In[203]:


# Task 9: Assign 10 to the variable base. Assign the set {0,1,2,3,4,5,6,7,8,9} to the variable digits.
# Now write an expression using a comprehension and base and digits whose value is the set of all at-mostthree-digit numbers.
# Your expression should work for any base. For example, if you instead assign 2 to base and assign {0,1}
# to digits, the value of your expression should be {0,1,2,3,4,5,6,7} because this is the set of numbers
# that, base two, have at most three digits.
base=8
{x*base**2+y*base**1+z*base**0 for x in range(base) for y in range(base) for z in range(base)}


# In[209]:


{i for i in range(base**3)}


# In[206]:


base**3


# In[211]:


# Task 10: Assume that S and T are assigned sets. Without using the intersection operator &, write a
# comprehension over S whose value is the intersection of S and T. Hint: Use a membership test in a filter at
# the end of the comprehension.
# Try out your comprehension with S = {1,2,3,4} and T = {3,4,5,6}.
S = {1,2,3,4}
T = {3,4,5,6}
{x for x in S if x in T}


# In[216]:


s=[20,10,15,75]


# In[217]:


# Task 11: Write an expression whose value is the average of the elements of the list [20, 10, 15, 75].

sum(s)/len(s)


# In[220]:


# Task 12: Assign to the variable LofL the list of lists [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
# Using a comprehension, write an expression involving LofL that returns the sum of all the numbers in all
# three lists. The expression has the form sum([sum(....
LofL =[[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
sum([sum(i) for i in LofL])


# In[221]:


# Task 13: Write a double list comprehension over the lists [’A’,’B’,’C’] and [1,2,3] whose value is the
# list of all possible two-element lists [letter, number]. That is, the value is
# [[’A’, 1], [’A’, 2], [’A’, 3], [’B’, 1], [’B’, 2],[’B’, 3],[’C’, 1], [’C’, 2], [’C’, 3]]
l1=['A','B','C']
l2=[1,2,3]
[[i,j] for i in l1 for j in l2 ]


# In[237]:


# Task 14: Suppose S is a set of integers, e.g. {−4, −2, 1, 2, 5, 0}. Write a triple comprehension whose value
# is a list of all three-element tuples (i, j, k) such that i, j, k are elements of S whose sum is zero.
sett={-4, -2, 1, 2, 5, 0}
[(x,y,z) for x in sett for y in sett for z in sett if x+y+z==0]


# In[240]:


# Task 15: Modify the comprehension of the previous task so that the resulting list does not include (0, 0, 0).
# Hint: add a filter.
[(x,y,z) for x in sett for y in sett for z in sett if x+y+z==0 and (x,y,z)!=(0,0,0)]


# In[241]:


# Task 16: Further modify the expression so that its value is not the list of all such tuples but is the first
# such tuple.

[(x,y,z) for x in sett for y in sett for z in sett if x+y+z==0 and (x,y,z)!=(0,0,0)][0]


# In[ ]:


# Task 17: Find an example of a list L such that len(L) and len(list(set(L))) are different. Then find
# a list L such that len(L) and len(list(set(L))) are the same but the order of elements differs between
# L and list(set(L)).


# In[242]:


L=[1,3,4,6,5,4]


# In[248]:


len(L) == len(list(set(L)))


# In[249]:


L1=[1,3,2,4,5]


# In[251]:


len(L1) == len(list(set(L1)))


# In[252]:


L1 in list(set(L1))


# In[255]:


# Task 18: Write a comprehension over a range of the form range(n) such that the 
# value of the comprehension is the set of odd numbers from 1 to 99.
[i for i in range(1,100,2)]


# In[256]:


List1,List2=[1,3,5],[2,4,6]


# In[260]:


[(List1[i],List2[i]) for i in range(len(List1))]


# In[262]:


# Task 19: Assign to L the list consisting of the first five letters [’A’,’B’,’C’,’D’,’E’]. Next, use L in an
# expression whose value is [(0, ’A’), (1, ’B’), (2, ’C’), (3, ’D’), (4, ’E’)]. Your expression
# should use a range and a zip, but should not use a comprehension.
lis=['A','B','C','D','E']
list(zip(lis,range(len(lis))))


# In[263]:


# Task 20: Starting from the lists [10, 25, 40] and [1, 15, 20], write a comprehension whose value is
# the three-element list in which the first element is the sum of 10 and 1, the second is the sum of 25 and 15,
# and the third is the sum of 40 and 20. Your expression should use zip but not list.
a=[10, 25, 40]
b=[1, 15, 20]
[x+y for x,y in zip(a,b)]


# In[271]:


# Task 21: Suppose dlist is a list of dictionaries and k is a key that appears in all the dictionaries in dlist.
# Write a comprehension whose value is the list whose i
# th element is the value corresponding to key k in the
# i
# th dictionary in dlist.
# Test your comprehension with some data. Here are some example data.
dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger',
'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
k = 'James'
[ v for i in dlist for ke,v in i.items() if ke==k]


# In[283]:


# Task 22: Modify the comprehension in Task 21 to handle the case in which k might not appear in all the
# dictionaries. The comprehension’s value is the list whose i
# th element is the value corresponding to key k in
# the i
# th dictionary in dlist if that dictionary contains that key, and ’NOT PRESENT’ otherwise.
# Test your comprehension with k = ’Bilbo’ and k = ’Frodo’ and with the following list of dictionaries:
dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},
{'Bilbo':'Martin','Thorin':'Richard'}]

[ i[k] if k in i else 'Not Present' for i in dlist]


# In[284]:


# Task 23: Using range, write a comprehension whose value is a dictionary. The keys should be the integers
# from 0 to 99 and the value corresponding to a key should be the square of the key.
{k:k*k for k in range(100)}


# In[290]:


# Task 24: Assign some set to the variable D, e.g. D ={’red’,’white’,’blue’}. 
# Now write a comprehension whose value is a dictionary that represents the identity function on D.
D={'red','white','blue'}
{i:i for i in D}


# In[295]:


from itertools import product


# In[332]:


# Task 25: Using the variables base=10 and digits=set(range(10)), write a dictionary comprehension
# that maps each integer from 0 through 999 to the list of three digits that represents that integer in base 10.
# That is, the value should be
# {0: [0, 0, 0], 1: [0, 0, 1], 2: [0, 0, 2], 3: [0, 0, 3], ...,
# 10: [0, 1, 0], 11: [0, 1, 1], 12: [0, 1, 2], ...,
# 999: [9, 9, 9]}
# Like Task 9, your expression should work for any base. For example, if you instead assign 2 to base and
# assign {0,1} to digits, the value should be
# {0: [0, 0, 0], 1: [0, 0, 1], 2: [0, 1, 0], 3: [0, 1, 1],
# ..., 7: [1, 1, 1]}
b=3
{(i[0]*b**2)+(i[1]*b)+i[2]:list(i) for i in product(range(b),range(b),range(b))}


# In[347]:


# Task 26: Suppose d is a dictionary that maps some employee IDs (a subset of the integers from 0 to n−1)
# to salaries. Suppose L is an n-element list whose i
# th element is the name of employee number i. Your goal is
# to write a comprehension whose value is a dictionary mapping employee names to salaries. You can assume
# that employee names are distinct. However, not every employee ID is represented in d.
d = {0:1000.0, 3:1200.50, 2:990}
L = ['Larry', 'Curly', 'Moe']
{L[i]:x[1] for x,i in zip(d.items(),range(len(L))) }


# In[351]:


# Task 27: Define a one-line procedure nextInts(L) specified as follows:
# • input: list L of integers
# • output: list of integers whose i th element is one more than the i th element of L
# • example: input [1, 5, 7], output [2, 6, 8].
def t27(l): return [i+1 for i in l]
t27([1, 5, 7])


# In[352]:


# Task 28: Define a one-line procedure cubes(L) specified as follows:
# • input: list L of numbers
# • output: list of numbers whose i th element is the cube of the i th element of L 
# • example: input [1, 2, 3], output [1, 8, 27].
def t28(l): return [i**3 for i in l]
t28([1, 2, 3])


# In[360]:


# Task 29: Define a one-line procedure dict2list(dct,keylist) with this spec:
# • input: dictionary dct, list keylist consisting of the keys of dct
# • output: list L such that L[i] = dct[keylist[i]] for i = 0, 1, 2, . . . , len(keylist) − 1
# • example: input dct={’a’:’A’, ’b’:’B’, ’c’:’C’} and keylist=[’b’,’c’,’a’], output [’B’, ’C’, ’A’]


# In[361]:


dct={'a':'A','b':'B', 'c':'C'} 
keylist=['b','c','a']
# output=['B','C','A']
def dict2list(dct,keylist): return [dct[keylist[i]] for i in range(len(keylist))]
dict2list(dct,keylist)


# In[ ]:


# Task 30: Define a one-line procedure list2dict(L, keylist) specified as follows:
# • input: list L, list keylist of immutable items
# • output: dictionary that maps keylist[i] to L[i] for i = 0, 1, 2, . . . , len(L) − 1
# • example: input L=[’A’,’B’,’C’] and keylist=[’a’,’b’,’c’], output
# {’a’:’A’, ’b’:’B’, ’c’:’C’}
# Hint: Use a comprehension that iterates over a zip or a range.


# In[363]:


L=['A','B','C'] 
keylist=['a','b','c']
def list2dict(L, keylist):return {keylist[i]:L[i] for i in range(len(L))}
list2dict(L,keylist)


# In[364]:


def list2dict0(L, keylist):return {k:v for v,k in zip(L,keylist)}
list2dict0(L,keylist)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





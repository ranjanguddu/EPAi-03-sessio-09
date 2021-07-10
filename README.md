# Session-09
---
## Tuple

A Tuple is immutable collection of Python objects separated by commas. In someways a tuple is similar to a list in terms of indexing, nested objects and repetition.

### Tuples are immutable
```python
tup = (1,2,3)
tup[0] = 2
print(tup)
```
```
Output:
Traceback (most recent call last):
  File "/Users/vikasran/Documents/EPAi-03/session-09/check.py", line 2, in <module>
    tup[0] = 2
TypeError: 'tuple' object does not support item assignment
```

Let's take another example:

```python
tup = (1,2,3, [4,6,9])
print(tup)

#now we change the element '6' of the list.
tup[3][1]=7
print(tup)
```
```
Output:
(1, 2, 3, [4, 6, 9])
(1, 2, 3, [4, 7, 9])
```
What we can conclude from the above 2 exmples. In case of tuple, we **can't change the reference of it's existing element**.

For tuple, comma is enough to declare it is tuple. No need to have small bracket pairs.
```python
tup1 = 2,3
tup2 = (2,3)
tup3 = 4, 
print(type(tup1))
print(type(tup2))
print(type(tup3))
```
```
Output:
<class 'tuple'>
<class 'tuple'>
<class 'tuple'>
```

## Namedtuple

Python supports a type of container like dictionaries called “namedtuple()” present in module, “collections“. Like dictionaries they contain keys that are hashed to a particular value. But on contrary, it supports both access from key value and iteration, the functionality that dictionaries lack.

### Basic example of Namedtuple
```python

from collections import namedtuple 
      
# Declaring namedtuple()  
Student = namedtuple('Student',['name','age','DOB'])  
      
# Adding values  
S = Student('Nandini','19','2541997')  
      
# Access using index  
print ("The Student age using index is : ",end ="")  
print (S[1])  
      
# Access using name   
print ("The Student name using keyname is : ",end ="")  
print (S.name)
```
```
Output:

The Student age using index is : 19
The Student name using keyname is : Nandini
```

For more detail on theis basic opeartion on Namedtuple refer this [link](https://www.geeksforgeeks.org/namedtuple-in-python/)


Let's see below example

```python
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y})'


p1 = Point2D(10,20)
print(p1)
```
```
Output:

Point2D(x=10, y=20)

```
What we have acheived above using so many code, we can get same thing using veryfew line with the help of Namedtuples
```python
from collections import namedtuple

Pt = namedtuple('Point2D', ('x', 'y'))
pt1 = Pt(10, 20)
print(pt1)
```
```
Output:

Point2D(x=10, y=20)

```
Let's say we are using class and finding dot product between two vectors (using end point, assuming initial point is origin)

```python
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return f"Point3D(x={self.x}, y={self.y}, z={self.z})"
    
    def __eq__(self, other):
        if isinstance(other, Point3D):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return False

Pt3 = Point3D
pt3 = Pt3(10, 20, 30)
pt4 = Pt3(10, 20, 30)
```
```python
def dot_product_3d(a, b):
    return a.x * b.x + a.y * b.y + a.z + b.z + a.a * b*a

dot_product_3d(pt3, pt4)
```
```
Output:

AttributeError                            Traceback (most recent call last)

<ipython-input-69-162476d7f603> in <module>()
----> 1 dot_product_3d(pt3, pt4)

<ipython-input-68-b090702c43a7> in dot_product_3d(a, b)
      1 def dot_product_3d(a, b):
----> 2     return a.x * b.x + a.y * b.y + a.z + b.z + a.a * b*a

AttributeError: 'Point3D' object has no attribute 'a'
```
Via class method, while we finding Dot Product we need to know about each attribute of that class. 

Whereas, if we use Namedtuple the issue is little simpler. We do not need to know about each attribute prior to implement dot product.


```python
def dot_product(a, b):
  return sum(e[0]*e[1] for e in zip(a, b))

Point4D = namedtuple('Point4D', ['i', 'j', 'k', 'l'])

pt4_1 = Point4D(1, 2, 3, 4)
pt4_2 = Point4D(1, 2, 3, 4)

dot_product(pt4_1, pt4_2)
```

We can use doc string for namedtuple:

```python
Stock = namedtuple('Stock', 'symbol year month day open high low close')
Stock.__doc__ = "Represent the stock values for a particalar day"
Stock.symbol.__doc__ = "Stock Market Name for NASDAC"
Stock.high.__doc__ = "highest value during the day"

```
Other important point about namedtuple:

```python
data_dict = dict(key1 = 100, key2 = 200, key3 = 300)
Data = namedtuple('Data', data_dict.keys())
d1 = Data(*data_dict.values())
print(d1)
```
```
Output:
Data(key1=100, key2=200, key3=300)
```

```python
dp2 = dict(key2= 100, key3 = 200, key1 = 300)
d2 = Data(*dp2.values())
print(d2)
```

```
Output:
Data(key1=100, key2=200, key3=300)
```
In the above example we can see that key, value is not in the same order. We can resolve this issue by **.

```python
d2 = Data(**dp2)
print(d2)
```
```
output
Data(key1=300, key2=100, key3=200)
```

```python
data_dict = dict(first_name='John', last_name='Cleese', age=42, complaint='dead parrot')
print(data_dict.keys())
print(sorted(data_dict.keys()))
Struct = namedtuple('Struct', sorted(data_dict.keys()))
print(Struct._fields)
d1 = Struct(**data_dict)
print(d1)
```
```
Output:
dict_keys(['first_name', 'last_name', 'age', 'complaint'])
['age', 'complaint', 'first_name', 'last_name']
('age', 'complaint', 'first_name', 'last_name')
Struct(age=42, complaint='dead parrot', first_name='John', last_name='Cleese')
```

## Assignemt Question Based on Namedtuple

### 1. Use the Faker (Links to an external site.)library to get 10000 random profiles. Using namedtuple, calculate the largest blood type, mean-current_location, oldest_person_age, and average age (add proper doc-strings). 

```python
from faker import Faker
from collections import namedtuple
from collections import defaultdict
from datetime import date, datetime, timezone
from time import perf_counter
from functools import wraps
import random
import pandas as pd


fake = Faker('en_IN')   
random_profile = namedtuple('Profile', ['name', 'age', 'sex', 'blood_group', 'location'])


# calculate the age of the person
find_age = lambda birthdate: int((date.today() - birthdate).days / 365)

# REPEAT DECORATOR
def repeat(n: int):
	"""
	This decorator is suppose to time the function. 
	"""
	def timed(fn):
		def inner(*args, **kwargs):
			total_elapsed = 0
			
			for _ in range(n):
				start = perf_counter()
				result = fn(*args, **kwargs)
				total_elapsed += (perf_counter() - start)

			avg_run_time = total_elapsed / n
			print(f'Average Run time of {fn.__name__} is : {avg_run_time} for {n} reps.')
			return result
		return inner
	return timed

profile_list = []

@repeat(10)
def generate_random_profile(n: int):
	"""
	This function suppose to generate n no of random profile using named Dictionary
	"""
	blood_type = defaultdict(lambda : 0)
	#print(f'blood type:{blood_type}')
	for _ in range(n):
		prof = fake.profile()
		#print(prof['name'], prof['blood_group'])
		profile = random_profile(prof['name'], find_age(prof['birthdate']), prof['sex'], prof['blood_group'], prof['current_location'])
		profile_list.append(profile)
		blood_type[profile.blood_group] +=1
		
	av_age = sum([i.age for i in profile_list])/len(profile_list)
	oldest = max([i.age for i in profile_list])
	mean_loaction = sum([i.location[0] for i in profile_list])/len(profile_list), sum([i.location[1] for i in profile_list])/len(profile_list)
	largest_blood_group = sorted(blood_type.items(), key=lambda x: x[1], reverse=True)[0]
	return f'average age:{av_age} years,oldest one is of {oldest} years, mean location:{mean_loaction}, largest_blood:{largest_blood_group}'

res = generate_random_profile(1000)
print(res)
```
```
Output:
Average Run time of generate_random_profile is : 0.36701088980000024 for 10 reps.
average age:57.6177 years,oldest one is of 116 years, mean location:(Decimal('-0.4788468498'), Decimal('-0.4567233898')), largest_blood:('O-', 140)
```

### 2. Do the same thing above using a dictionary. 

```python
profile_list_dict = []
blood_type = defaultdict(lambda: 0)


@repeat(10)
def generate_random_profile_dicts(n: int):
	"""
	This function suppose to generate n no of random profile using Dictionary
	"""
	for _ in range(n):
		profile_dict =  defaultdict(lambda :0)
		fake_prof = fake.profile()
		attribue = ['name', 'birthdate', 'sex', 'blood_group', 'current_location']
		for key in attribue:
			#print("hello")
			profile_dict[key] = fake_prof[key]
			
		age = find_age(fake_prof['birthdate'])
		profile_dict['age'] = age

		blood_type[profile_dict['blood_group']] += 1
		profile_list_dict.append(profile_dict)

	avg_age = sum([item['age']for item in profile_list_dict])/len(profile_list_dict)
	max_age = max([item['age']for item in profile_list_dict])
	mean_loc = sum([item['current_location'][0] for item in profile_list_dict])/len(profile_list_dict), sum([item['current_location'][1] for item in profile_list_dict])/len(profile_list_dict) 
	#print(type(mean_loc))
	return f'Average age:{avg_age} years.\n Oldest person: {max_age} years\nThe loaction:({mean_loc} Degrees.\
			 \nLargest Blood Category:{sorted(blood_type.items(), key=lambda x: x[1], reverse=True)[0]}'

	#print(profile_list_dict)
res = generate_random_profile_dicts(1000)
print(res)
```

```
Output:
Average Run time of generate_random_profile_dicts is : 0.34439868370000015 for 10 reps.
Average age:57.0932 years.
 Oldest person: 116 years
The loaction:((Decimal('0.6259542756'), Decimal('-2.1300260775')) Degrees.			 
Largest Blood Category:('A-', 1298)
```

### 3. Create fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies (name, symbol, open, high, close). Assign a random weight to all the companies. Calculate and show what value the stock market started at, what was the highest value during the day, and where did it end. Make sure your open, high, close are not totally random. You can only use namedtuple.

```python
symbol_generator =  lambda x:x[:3]+'_SYMB'.upper()
companies = namedtuple('StockMarket', ['name', 'symbol', 'open', 'low', 'high', 'close'])
weight = []
company_stock_profiles = []

def stock_exchange(n):
	""" This function suppose to generate n no of company's fake profile """
	
	for _ in range(n):
		name =  fake.company()
		symbol= symbol_generator(name)
		#print(f'{name}:{symbol}')
		open_value = random.randint(100, 4000)
		comp_weight = random.uniform(0, 0.8)

		weight.append(comp_weight)

		comp_contrib = round(open_value * comp_weight/sum(weight), 3)

		high_value = round(random.uniform(1.0, 1.2) * open_value * comp_weight/sum(weight), 3)
		close_value = round(random.uniform(0.6,0.8) * open_value * comp_weight/sum(weight), 3)
		low_value = round(random.uniform(0.2, 0.4) * open_value * comp_weight/sum(weight), 3)

		comp_profile = companies(name, symbol, open_value, low_value, high_value, close_value)
		#print(comp_profile)
		company_stock_profiles.append(comp_profile)
		Total = pd.DataFrame({
					'Open': ['= '+str(round(sum([i.open for i in company_stock_profiles]), 3))], 
					'Low': ['= '+str(round(sum([i.low for i in company_stock_profiles]), 3))],
					'High': ['= '+str(round(sum([i.high for i in company_stock_profiles]), 3))],
					'Close': ['= '+str(round(sum([i.close for i in company_stock_profiles]), 3))]
							})

		stock = pd.DataFrame({'Company Name': [i.name for i in company_stock_profiles],
								'Symbol': [i.symbol for i in company_stock_profiles],
								'Open': [i.open for i in company_stock_profiles], 
								'Low': [i.low for i in company_stock_profiles],
								'High': [i.high for i in company_stock_profiles],
								'Close': [i.close for i in company_stock_profiles]
								})
	return stock.append(Total)
		

res = stock_exchange(5)
print(res)
```
```
Output:

             Company Name    Symbol    Open        Low        High       Close
0              Moneta SPA  Mon_SYMB     302     65.097     360.836     214.135
1          Evans and Sons  Eva_SYMB    1546     59.812     299.412     172.335
2            Toso e figli  Tos_SYMB    3249    174.602     893.316     641.357
3  Lettiere-Piane e figli  Let_SYMB     512     18.858       94.31      51.505
4                Moss PLC  Mos_SYMB    3098    238.915     819.457     588.629
0                     NaN       NaN  = 8707  = 557.284  = 2467.331  = 1667.961


```
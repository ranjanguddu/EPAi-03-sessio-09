#  1. Use the Faker (Links to an external site.)library to get 
# 10000 random profiles. Using namedtuple, calculate the largest blood type,
# mean-current_location, oldest_person_age, and average age.

from faker import Faker
from collections import namedtuple
from collections import defaultdict
from datetime import date, datetime, timezone
from time import perf_counter
from functools import wraps
import random
import pandas as pd



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
			#print(f'Average Run time of {fn.__name__} is : {avg_run_time} for {n} reps.')
			return result, avg_run_time
		return inner
	return timed

profile_list = []

@repeat(10)
def generate_random_profile(n: int):
	"""
	This function suppose to generate n no of random profile using named Dictionary
	"""
	fake = Faker('en_IN')   
	random_profile = namedtuple('Profile', ['name', 'age', 'sex', 'blood_group', 'location'])
	# calculate the age of the person
	find_age = lambda birthdate: int((date.today() - birthdate).days / 365)

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

# res = generate_random_profile(1000)
# print(res[1])



# 2. Do the same thing above using a dictionary. Prove that namedtuple is faster.

profile_list_dict = []
blood_type = defaultdict(lambda: 0)


@repeat(10)
def generate_random_profile_dicts(n: int):
	"""
	This function suppose to generate n no of random profile using Dictionary
	"""
	fake = Faker('en_IN')   
	random_profile = namedtuple('Profile', ['name', 'age', 'sex', 'blood_group', 'location'])
	# calculate the age of the person
	find_age = lambda birthdate: int((date.today() - birthdate).days / 365)

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
# res = generate_random_profile_dicts(1000)
# print(res[1])

#3. Create fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies (name, symbol, open, high, close). Assign a random weight to all the companies. Calculate and show what value the stock market started at, what was the highest value during the day, and where did it end. Make sure your open, high, close are not totally random.

symbol_generator =  lambda x:x[:3]+'_SYMB'.upper()
companies = namedtuple('StockMarket', ['name', 'symbol', 'open', 'low', 'high', 'close'])
weight = []
company_stock_profiles = []

def stock_exchange(n):
	""" This function suppose to generate n no of company's fake profile """
	fake = Faker('en_IN')
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
		


#res = stock_exchange(100)
#print(res[1], res[2],res[3], res[4])


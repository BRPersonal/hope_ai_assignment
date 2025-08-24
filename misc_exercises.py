#get list of keys from a dictionary
dictionary = {"a": 1, "b": 2, "c": 3}
keys = list(dictionary.keys())
print(f"keys={keys}")

#filter numbers divisible by 3
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
div_by_3 = tuple(filter(lambda x: x % 3 == 0,numbers))
print(f"div_by_3={div_by_3}")

#find leap year
year = int(input("enter year:"))
is_leap = (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))
print(f"{year} { 'IS A' if is_leap else 'IS NOT A'} Leap Year")

#list,dictionary are mutable
#tuple,string are immutable

my_list = [1,2,3,4]
del my_list[2]
print(f"my_list={my_list}")


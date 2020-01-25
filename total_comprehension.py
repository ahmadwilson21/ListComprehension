# total_comprehension.py

my_numbers = [1, 2, 3, 4, 5, 6, 7]
print("--------------")
print("ORIGINAL LIST:", my_numbers)

print("--------------")
print("TOTAL COMPREHENSION...")
print("--------------")

mapped_numbers = [i*100 for i in my_numbers]

#mapped_numbers 
print("MAPPED LIST:", mapped_numbers)
print("--------------")

def greater_than_three(i):
    return i > 3

filtered_list = list(filter(greater_than_three,my_numbers))

print("FILTERED LIST W/MATCHES:", filtered_list)
print("--------------")

unfiltered_list = list(filter(lambda i: i>8, my_numbers))
print("FILTERED LIST W/O MATCHES:", unfiltered_list)
print("--------------")

last_list = [n*100 for n in my_numbers if n>3] # notation for making list equal to set a numbers
print("MAPPED AND FILTERED LIST :",last_list )
print("--------------")
# TODO: write python code here
#--------------
#ORIGINAL LIST: [1, 2, 3, 4, 5, 6, 7]
#--------------
#TOTAL COMPREHENSION...
#--------------
#MAPPED LIST: [100, 200, 300, 400, 500, 600, 700]
#--------------
#FILTERED LIST W/ MATCHES: [4, 5, 6, 7]
#--------------
#FILTERED LIST W/O MATCHES: []
#--------------
#MAPPED AND FILTERED LIST: [400, 500, 600, 700]
baby_names = ['zoey', 'charlotte', 'taylor', 'braydon', 'grace', 'ariel']
print(baby_names)


#Pay attention to line 6 closing ":" & line 7 must be in indented or the output will read an error. 
for baby_name in baby_names:
    print(baby_name)
    print(baby_name.title())
    print(baby_name.upper())
    print(baby_name.lower())
    print(baby_name.title() + " is a beautiful name & no my husband didn't help") 

#Practice using list with numbers 
for value in range(1, 13):
        print(value)
   
# the last value tells the list to add one. 
numbers = list(range(1, 14, 2))
print(numbers)
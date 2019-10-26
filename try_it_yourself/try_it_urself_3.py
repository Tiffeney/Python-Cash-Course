#3-1. Names: Store the names of a few of your friends in a list called names . Print each person’s name by accessing each element in the list, 
# one at a time.

# best_friends = ["whiteney", "asia", "betsy", "meshia", "kristi"]
# print(best_friends[0])
# print(best_friends[1])
# print(best_friends[2])
# print(best_friends[3])
# print(best_friends[4])

#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them . 
# The text of each message should be the same, but each message should be personalized with the person’s name.

# print(best_friends[0] + 'is my sister/bestfreind')




#3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, 
# and make a list that stores several examples . Use your list to print a series of statements about these items, such as 
# “I would like to own a Honda motorcycle.”


#3-8. Seeing the World: Think of at least five places in the world you’d like to visit .

#• Store the locations in a list . Make sure the list is not in alphabetical order .
# places_to_visit = ['london', 'africa', 'iceland', 'canada', 'atlanta']


# Print your list in its original order . Don’t worry about printing the list neatly, just print it as a raw Python list .
# print(places_to_visit)

# Use sorted() to print your list in alphabetical order without modifying the actual list .
# print(sorted(places_to_visit))

# Show that your list is still in its original order by printing it .
# print(places_to_visit)

# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list .
# print(places_to_visit)

# Show that your list is still in its original order by printing it again .
# print(places_to_visit)

# Use reverse() to change the order of your list . Print the list to show that its order has changed .
places_to_visit = ['london', 'africa', 'iceland', 'canada', 'atlanta']
# print(places_to_visit)
# places_to_visit.reverse()
# print(places_to_visit)
# print(places_to_visit.reverse())
print(places_to_visit)

# Use reverse() to change the order of your list again . Print the list to show it’s back to its original order .
places_to_visit.reverse()
print(places_to_visit)


# Use sort() to change your list so it’s stored in alphabetical order . Print the list to show that its order has been changed .
places_to_visit.sort()
print(places_to_visit)

# Use sort() to change your list so it’s stored in reverse alphabetical order . Print the list to show that its order has changed .
places_to_visit.sort(reverse=True)
print(places_to_visit)

#3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (page 46), use len() to print a message indicating the 
# number of people you are inviting to dinner .


#3-10. Every Function: Think of something you could store in a list . For example, you could make a list of mountains, rivers, countries, 
#cities, languages, or any- thing else you’d like . Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once .
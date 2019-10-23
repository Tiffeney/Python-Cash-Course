# 2-3 Personal Message: Store a person's name in a variable, and print a message to that person. 
# Your message should be simple, such as, "Hello Eric, would you like to learn some Python today?"

name = "tiffeney"
print(name + " you should've learn Python first! lol")

#2-4 Store a person's name in a variable, and then print that person's name in lowercare, uppercase, and titlecase
mentors_name = 'corey griffin'
print(mentors_name.title())
print(mentors_name.upper())
print(mentors_name.lower())

#2-5 Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something the following,
#include the quotations marks:
#Albert Einstein once said, "A person who never made a mistake never tired anything new."

print("One of James Baldwin famous quotes was, 'People are trapped in history and history is trapped in them.'")

#2-6 Repeat exercise 2-5, but this time store the famous person's name in a variable called message. Print your message

message = "james baldwin"
quote = "People are trapped in history and history is trapped in them."
print("One of " + message + " " + "famous quotes was " + quote)

#2-7 Store a person's name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character
#combination, "\t" and "\n", at least once. 
#Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip().

bros_name = ' christopher '
print(bros_name)

bros_full_name = ' christopher jordan rambo '
print(bros_full_name)
print(bros_full_name.rstrip())
print(bros_full_name.lstrip())
print(bros_full_name.strip())


bros_full_name = '\n\tchristopher\n\tjordan\n\trambo'
print(bros_full_name)


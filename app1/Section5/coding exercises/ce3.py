# This time you should create a program that:
#
# 1. Contains the above list.
#
# 2 Prompts the user to input the person's name.
#
# 3. Returns the rank that person has.
#
# For example:

# Enter a name: Sen
# 2

athletes = ['John', 'Sen', 'Lisa']
# athletes variable stores the names of the athletes in an index list

find_rank = input("What is the athlete's name: ")
# find rank variable collects user input of athlete's name
find_rank = find_rank.capitalize()
# find_rank input is capitalized in order to continue code execution even with lowercase submission
rank = athletes.index(find_rank) + 1
# rank is retrieved by indexing the user input of athlete name against the list and we add the index number with 1 to account for 0
print(rank)
# prints the retrieved rank number
# The ranking list given in the coding area represents the ranking of three athletes, John, Sen, and Lisa. John won 1st place, Sen got 2nd, and Lisa 3rd.
#
# Your task is to create a program that:
#
# 1. Contains the above list.
#
# 2. Prompts the user to input a rank number.
#
# 3. Returns the person who has the given rank.#
#
# For example:

# Enter rank number: 2
# Sen

athletes = ["John", "Sen", "Lisa"]
# athletes variable stores the athlete names in a list index
rank = int(input("Enter rank to retrieve the athlete name: "))
# rank variable stores the inputted rank as an integer
rank = rank - 1
# inputted rank is subtracted by 1 to account for 0
print(athletes[rank])
# print function calls the list index number from the index list of athletes
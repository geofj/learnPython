# Please code this exercise in your computer IDE. For this exercise,
# download the members.txt file attached to the resources.
# Then, create a program that:
#
# 1. prompts the user to enter a new member.
#
# 2. adds that member to members.txt at the end of the existing members.
# For example, the user here has entered the member Solomon Right.

new_member = input("Add a new member: ")
# user input for new member
members = open('members.txt', 'r')
# opens members.txt file
current_members = members.readlines()
members.close()
# reads members.txt
current_members.append(new_member.title() + "\n")
# appends members.txt file with the user input submission and creates a new line text for input
members = open('members.txt','w')
# opens members.txt file
current_members = members.writelines(current_members)
members.close()
# writes the new member onto existing data within members.txt
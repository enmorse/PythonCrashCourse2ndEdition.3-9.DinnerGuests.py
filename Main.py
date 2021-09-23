# Make a list that includes at least three people you
# would like to invite to dinner.

# Then use your list to print a message to each person,
# inviting them to dinner.

idol_guest_list = ["arnold schwarzenegger", "babe ruth",
                   "sean connery"]

invitation = f"Mr. {idol_guest_list[0].title()}, " \
             f"Mr. {idol_guest_list[1].title()}, and " \
             f"Mr. {idol_guest_list[2].title()}, I would like " \
             f"to invite you to dinner because " \
             f"\nyou are idols of mine and I have admired " \
             f"\nyou and looked up to you sense I was a " \
             f"little boy."

print(invitation)

# You just heard that one of your guests can't make the
# dinner, so you need to send out a new set of invitations.
# You will have to think of someone else to invite.

# Start with your program from Exercise 3 - 4.
# Add a print() call at the end of your program stating
# the name of the guest who can not make it.

message = f"I am sorry to inform you but " \
          f"{idol_guest_list[1].title()} will not be able to " \
          f"make it for dinner."

print(message)

# Modify your list, replacing the name of the guest who
# can't make it with the name of the new person you
# are inviting.

idol_guest_list[1] = "keanu reeves"

print(idol_guest_list)

# Print a second set of invitation messages,
# one for each person who is still in your list.

invitation1 = f"Mr. {idol_guest_list[0].title()}, I would " \
              f"like to invite you to dinner because " \
              f"\nyou have been an idol of mine and I have " \
              f"\nadmired you and looked up to you sense I " \
              f"was a little boy."
invitation2 = f"Mr. {idol_guest_list[1].title()}, I would " \
              f"like to invite you to dinner because " \
              f"\nyou have been an idol of mine and I have " \
              f"\nadmired you and looked up to you sense I " \
              f"was a little boy."
invitation3 = f"Mr. {idol_guest_list[2].title()}, I would " \
              f"like to invite you to dinner because " \
              f"\nyou have been an idol of mine and I have " \
              f"\nadmired you and looked up to you sense I " \
              f"was a little boy."

print(invitation1)
print(invitation2)
print(invitation3)

# You just found a bigger dinner table, so now more
# space is available. Think of three more guests to invite
# to dinner.

# Start with your program from Exercise 3 - 4 or 3 - 5.
# Add a print() call to the end of your program informing
# people that you found a bigger dinner table.

invitation4 = f"Mr. {idol_guest_list[0].title()}, " \
              f"Mr. {idol_guest_list[1].title()}," \
              f"\nand Mr. {idol_guest_list[2]}, I would like " \
              f"\nto inform you that I have found a bigger " \
              f"dinner table and can now seat three more " \
              f"guests for dinner."

print(invitation4)

# Use the insert() function to add one new guest to the
# beginning of your list.

idol_guest_list.insert(0, "Harrison Ford")

print(idol_guest_list)

# Use the insert() function to add one new guest to the
# middle of your list.

idol_guest_list.insert(2, "Sylvester Stallone")

print(idol_guest_list)

# Use append to add one new guest to the end of your
# list.

idol_guest_list.append("Jean-Claude Van Damme")

print(idol_guest_list)

# Print a new set of invitation messages,
# one for each person.

invitation5 = f"Mr. {idol_guest_list[0].title()}, I would " \
              f"like to invite you to dinner because " \
              f"\nyou have been an idol of mine and I have " \
              f"\nadmired you and looked up to you sense I " \
              f"was a little boy."
invitation6 = f"Mr. {idol_guest_list[1].title()}, I would " \
              f"like to invite you to dinner because " \
              f"\nyou have been an idol of mine and I have " \
              f"\nadmired you and looked up to you sense I " \
              f"was a little boy."
invitation7 = f"Mr. {idol_guest_list[2].title()}, I would " \
              f"like to invite you to dinner because " \
              f"\nyou have been an idol of mine and I have " \
              f"\nadmired you and looked up to you sense I " \
              f"was a little boy."
invitation8 = f"Mr. {idol_guest_list[3].title()}, I would " \
              f"like to invite you to dinner because " \
              f"\nyou have been an idol of mine and I have " \
              f"\nadmired you and looked up to you sense I " \
              f"was a little boy."
invitation9 = f"Mr. {idol_guest_list[4].title()}, I would " \
              f"like to invite you to dinner because " \
              f"\nyou have been an idol of mine and I have " \
              f"\nadmired you and looked up to you sense I " \
              f"was a little boy."
invitation10 = f"Mr. {idol_guest_list[5].title()}, I would " \
               f"like to invite you to dinner because " \
              f"\nyou have been an idol of mine and I have " \
               f"\nadmired you and looked up to you sense I " \
               f"was a little boy."

print(invitation5)
print(invitation6)
print(invitation7)
print(invitation8)
print(invitation9)
print(invitation10)

# You just found out that your new dinner table won't
# arrive in time for the dinner, and you have space for
# only two guests.

# Start with your program from Exercise 3 - 6.

# Add a new line that prints a message saying that you
# can invite only two people for dinner.

declined_invitations = f"Mr. {idol_guest_list[0].title()}, " \
                       f"Mr. {idol_guest_list[1].title()}," \
                       f"\nMr. {idol_guest_list[2].title()}, " \
                       f"Mr. {idol_guest_list[3].title()}," \
                       f"\nMr. {idol_guest_list[4].title()}, " \
                       f"Mr. {idol_guest_list[5].title()}," \
                       f"\nI am sorry to inform you but the " \
                       f"\ndinner table will not arrive in time " \
                       f"\nfor the dinner, and I will not be able " \
                       f"\nto accommodate all six of your for " \
                       f"dinner."

print(declined_invitations)

# Use pop() to remove guests from your list one at a
# time until only two names remain in your list. Each
# time you pop a name from your list, print a message
# to that person letting them know you can't invite them
# to dinner.

idol_guest_declined1 = idol_guest_list.pop(0)

print(idol_guest_list)

print(f"Mr. {idol_guest_declined1.title()}, I am sorry "
      f"\nto inform you but the dinner table will not "
      f"\narrive in time for dinner, and I will no be able "
      f"\nto accommodate you for dinner.")

idol_guest_declined2 = idol_guest_list.pop(1)

print(idol_guest_list)

print(f"Mr. {idol_guest_declined2.title()}, I am sorry "
      f"\nto inform you but the dinner table will not "
      f"\narrive in time for dinner, and I will no be able "
      f"\nto accommodate you for dinner.")

idol_guest_declined3 = idol_guest_list.pop(1)

print(idol_guest_list)

print(f"Mr. {idol_guest_declined3.title()}, I am sorry "
      f"\nto inform you but the dinner table will not "
      f"\narrive in time for dinner, and I will no be able "
      f"\nto accommodate you for dinner.")

idol_guest_declined4 = idol_guest_list.pop(2)

print(idol_guest_list)

print(f"Mr. {idol_guest_declined4.title()}, I am sorry "
      f"\nto inform you but the dinner table will not "
      f"\narrive in time for dinner, and I will no be "
      f"\nable to accommodate you for dinner.")

# Print a message to the two people still on your list,
# letting them know they're still invited

extinguished_guests = f"Mr. {idol_guest_list[0].title()} " \
                      f"and Mr. {idol_guest_list[1].title()}," \
                      f"\nI would like to inform you that you " \
                      f"\nare still invited to the dinner."

print(extinguished_guests)

# Use del to remove the last two items from your list,
# so that you have an empty list. Print your list to make
# sure you actually have an empty list at the end of
# your program.

del idol_guest_list[0]

print(idol_guest_list)

del idol_guest_list[0]

print(idol_guest_list)

# Working with one of the programs from Exercises 3 -
# 4 through 3 - 7 (page 42), use len() to print a message
# indicating the number of people you are inviting to
# dinner.

idol_guest_list.append("arnold schwarzenegger")

print(idol_guest_list)

idol_guest_list.append("sean connery")

print(idol_guest_list)

message = f"Mr. {idol_guest_list[0].title()} and Mr. " \
          f"{idol_guest_list[1].title()},I would like to " \
          f"\nextend a dinner invitation to you because you " \
          f"\nare idols of mine, and because I have " \
          f"\nadmired you and looked up to you sense I " \
          f"\nwas a little boy."

print(message)
print("The length of my idol guest list is ", len(idol_guest_list))

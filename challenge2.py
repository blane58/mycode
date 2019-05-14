#!/usr/bin/env python3
first_list=[]
first_dict={"first_name": "Monty", "Last_name": "Python", "actions": ["Scooter", 2, "Moscow"]}
# print out the following sentence:
# "In Monty Python, Eric Idle rode a Scooter 2 Moscow"
print(f'In {first_dict["first_name"]} {first_dict["Last_name"]}, Eric Idle rode a {first_dict["actions"][0]} {first_dict["actions"][1]} {first_dict["actions"][2]}')

# Use a method we discussed yesterday to add the following items to 'first_list': "horse", "to", "the Holy Grail".
# .append() OR .extend()
first_list.append(['horse', 'to', 'the Holy Grail'])
print(first_list)

# Use a method we discussed to update the "Actions" in first_dict with the values of first_list.
first_dict.update({"actions": first_list})
print(first_dict)

# Print out the following sentence:
# "In Monty Python, Eric Idle rode a horse to the Holy Grail".
print(f'In {first_dict["first_name"]} {first_dict["Last_name"]}, Eric Idle rode a {first_dict["actions"][0]} {first_dict["actions"][1]} {first_dict["actions"][2]}')

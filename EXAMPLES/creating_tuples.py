
person = ("Bill", "Gates", "Microsoft", "1955-10-28")  # parens not needed

person = "Bill", "Gates", "Microsoft", "1955-10-28"

print(person, "\n")

print(person[0], person[1], "\n")

# iterable unpacking
#  [0]         [1]       [2]    [3]
first_name, last_name, product, dob = person
print(first_name, last_name, "\n")

#  collections.namedtuple

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

f1 = []
for f in fruits:
    value = f.upper()
    f1.append(value)
print(f"{f1 = }\n")

# list comprehension
#    [VALUE for VAR in ITERABLE if CONDITION]
f2 = [f.upper() for f in fruits]
print(f"{f2 = }\n")

f3 = [f.title() for f in fruits if f.startswith('p')]
print(f"{f3 = }\n")

f4 = [f for f in fruits if f.endswith('berry')]
print(f"{f4 = }\n")

f5 = [f.upper() for f in fruits if f.startswith('p') if len(f) > 6]
print(f"{f5 = }\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

dobs = [p[-1] for p in people]
print(f"{dobs = }\n")

suits = 'Clubs Diamonds Hearts Spades'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
cards = [(rank, suit) for suit in suits for rank in ranks]
print(f"{cards = }\n")

# generator expression
#  (value for var in iterable if condition ...)
fruit_gen = (f.upper() for f in fruits)
print(f"{fruit_gen = }")
for fruit in fruit_gen:
    print(fruit)

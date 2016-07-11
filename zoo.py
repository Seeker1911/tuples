# tuple
zoo = ('Bear', 'Fox', 'HoneyBadger', 'Puma')
# Get index of Fox
print(zoo.index('Fox'))
# Iterate and compare if HoneyBadger exists
badger = [item for item in zoo if 'HoneyBadger' in item]

print(badger)
# Turn zoo tuple into list
zoo = list(zoo)

print(zoo)
# Add new animals
zoo.extend(['Lion', 'Tiger', 'Panda'])
print(zoo)
# turn list into tuple
zoo = tuple(zoo)
print(type(zoo))

# Create a variable for each value of zoo.
(Grizzly, foxicus, badger, cat, bigCat, otherCat, littleBear) = zoo
print(Grizzly)

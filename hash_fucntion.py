from string import printable

from hash_distribution import distribute, plot


def hash_function(key):
    return sum(
        index * ord(character)
        for index, character in enumerate(repr(key).lstrip("'"), start=1)
    )


print(type(printable))
print(len(printable))
print(printable)
plot(distribute(printable, 6, hash_function))

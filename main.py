def likes(names):
    count = len(names)

    if count == 0:
        return 'no one likes this'
    elif count == 1:
        return f'{names[0]} likes this'
    elif count == 2:
        return f'{names[0]} and {names[1]} like this'
    elif count == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        return f'{names[0]}, {names[1]} and {count - 2} others like this'

# Test cases
print(likes([]))
print(likes(["Peter"]))
print(likes(["Jacob", "Alex"]))
print(likes(["Max", "John", "Mark"]))
print(likes(["Alex", "Jacob", "Mark", "Max"]))


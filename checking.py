def checker(value):
    print(value)
    if value == 0:
        bum = 0
    else:
        value=value-1
        return checker(value)


values= 4

print(checker(values))


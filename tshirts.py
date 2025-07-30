
def size(cms):
    if cms < 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'

# Existing tests
assert(size(37) == 'S')
assert(size(40) == 'M')
assert(size(43) == 'L')

# New test that exposes the bug (will fail)
assert(size(38) == 'M')  

print("Tests ran (but some may fail, exposing bugs)")


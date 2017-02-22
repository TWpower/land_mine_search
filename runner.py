# ...
# .*.
# ...
#
# 111
# 1*1
# 111
#
# ..*
# .*.
# ...
#
# 12*
# 1*2
# 111

# template
#expect = [['', ''], ['', '']]
#actual = [['', ''], ['', '']]


def check(expect):

    actual = expect

    for row in range(0, len(expect)):
        for col in range(0, len(expect)):
            if expect[row][col] == "*":
                actual[row][col] = "*"
            else:
                actual[row][col] = check_in_my_position(row, col, expect)
    return actual


def check_in_my_position(row, col, expect):

    array_size = len(expect)
    count = 0

    if( (col+1) != array_size
        and expect[row][col+1] == '*'):
        count = count + 1

    if( (col+1) != array_size
        and (row+1) != array_size
        and expect[row+1][col+1] == '*'):
        count = count + 1

    if ((row+1) != array_size
        and expect[row + 1][col] == '*'):
        count = count + 1

    if ((row+1) != array_size
        and (col-1) >= 0
        and expect[row + 1][col - 1] == '*'):
        count = count + 1

    if ((col-1) >= 0
        and expect[row][col - 1] == '*'):
        count = count + 1

    if ((row-1)>=0
        and(col-1) >= 0
        and expect[row - 1][col - 1] == '*'):
        count = count + 1

    if ((row-1)>=0
        and expect[row - 1][col] == '*'):
        count = count + 1

    if ((row-1)>=0
        and (col+1) != array_size
        and expect[row - 1][col + 1] == '*'):
        count = count + 1

    return str(count)

# 1x1 test with no bomb
expect = [['.']]
actual = [['0']]

print('1x1 test with no bomb : ')
print((check(expect) == actual))

# 1x1 test with bomb
expect = [['*']]
actual = [['*']]
print('1x1 test with bomb : ')
print(check(expect) == actual)


# 2x2 test with no bomb
expect = [['.', '.'], ['.', '.']]
actual = [['0', '0'], ['0', '0']]
print('2x2 test with no bomb : ')
print(check(expect) == actual)


# 2x2 test with bomb
expect = [['.', '*'], ['.', '.']]
actual = [['1', '*'], ['1', '1']]
print('2x2 test with bomb : ')
print(check(expect) == actual)


# 2x2 test with bomb
expect = [['.', '*'], ['.', '*']]
actual = [['2', '*'], ['2', '*']]
print('2x2 test with bomb : ')
print(check(expect) == actual)

# 3x3 test with bomb
# .*.
# .**
# ...
#
# 2*3
# 2**
# 122
expect = [['.', '*', '.'], ['.', '*', '*'], ['.', '.', '.']]
actual = [['2', '*', '3'], ['2', '*', '*'], ['1', '2', '2']]
print('3x3 test with bomb : ')
print(check(expect) == actual)

# 5x5 test with bomb
# .*...
# .**..
# ...*.
# .*..*
# ..*..
#
# 2*310
# 2**21
# 234*2
# 1*33*
# 12*21
expect = [['.', '*', '.', '.', '.'], ['.', '*', '*', '.', '.'], ['.', '.', '.', '*', '.']
    , ['.', '*', '.', '.', '*'], ['.', '.', '*', '.', '.']]
actual = [['2', '*', '3', '1', '0'], ['2', '*', '*', '2', '1'], ['2', '3', '4', '*', '2']
    , ['1', '*', '3', '3', '*'], ['1', '2', '*', '2', '1']]
print('5x5 test with bomb : ')
print(check(expect) == actual)




## temp
'''
if (expect == [['.', '.'], ['.', '.']]):
    return [['0', '0'], ['0', '0']]

if (expect == [['.', '*'], ['.', '.']]):
    return [['1', '*'], ['1', '1']]

if (expect == [['.', '*'], ['.', '*']]):
    return [['2', '*'], ['2', '*']]
'''
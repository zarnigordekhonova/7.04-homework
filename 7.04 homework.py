from collections import Counter

# 1
def find_medium(l1, l2):
    l1.extend(l2)
    r = 0
    for i in l1:
        if l1.count(i) == 1:
            r += i
    print(r/4)
# find_medium([1, 1, 3, 4, 4, 5, 6, 7],
#          [0, 1, 2, 3, 4, 4, 5, 7, 8])


# 2
def text_number(l1, text):
    r = []
    for i in l1:
        i = str(i)
        r.append(text+i)
    print(r)
# text_number([1, 4, 3, 9],
#             'RM')


# 3
def max_sublist(l1):
    m = 0
    for i in l1:
        a = sum(i)
        if a > m:
            m = a
            s = i
    print(s)
# max_sublist([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])


# 4
def find_int(l1):
    r = 0
    for i in l1:
        if isinstance(i, int):
            r += 1
    print(r)

# find_int([1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22])


# 5
def most_frequent_number(l1):
    l1_count = Counter(l1)
    most_frequent, count = l1_count.most_common(1)[0]
    print(f'Eng kop takrorlangan raqam: {most_frequent}, {count} marta!')

# most_frequent_number([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2])


# 6
def change_last_value(l1):
    l1[-1] += 1
    print(l1)

# change_last_value([1, 2, 3])


# 7
def find_square(n):
    r = []
    for i in range(1, n+1):
        r.append(i**2)
    print(r)
# find_square(int(input('enter the n:  ')))


# 8
def pair_func(numbers, text):
    r = []
    for i in range(len(text)):
        r.append(text[i] + str(numbers[i]))
    print(r)
# pair_func([1, 4, 3, 9],
#           ['chelsea', 'real', 'barca', 'MU'])

# 9
def find_max(l1, l2):
    l1.extend(l2)
    r = []
    for i in l1:
        if l1.count(i) == 2:
            r.append(i)
    print(max(r))

# find_max([1, 1, 3, 4, 4, 5, 6, 7],
#          [0, 1, 2, 3, 4, 4, 5, 7, 8])


# 10
def find_fibonacci(n):
    n = int(input('enter a  number: '))
    l = [0, 1]
    for i in range(2, n+1):
        l.append(l[i-1] + l[i-2])
    print(l[-3:])

# find_fibonacci('n')



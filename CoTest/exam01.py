n = int(input())

array = []

for i in range(n):
    a, b = input().split()
    array.append((a, int(b)))


def setting(data):
    return data[1]


result = sorted(array, key=setting)

for i in result:
    print(i[0], end=' ')
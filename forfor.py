x = "1 2 3 4"
splited = x.split(" ")

n = [int(num) for num in splited]
print(n)
print(sum(n))
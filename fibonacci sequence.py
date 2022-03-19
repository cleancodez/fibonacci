fib = int(input("enter how many numbers you want in the series: "))
first = 0
second = 1
# FIBONACCI SEQUENCE (0,1,1,2,3,5,8,13,21...)
for i in range(fib):
    print(first)
    start = first
    first = second
    second = start+second
 
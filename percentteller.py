import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
print("Hello welcome to percentage program please enter your marks in 5 subjects")
a=input().split(",")
print(a)
a = [int(i) for i in a]
n = a[0]+a[1]+a[2]+a[3]+a[4]
print(n)
m = n/500 *100
print("here your percentage is below")
print(m)
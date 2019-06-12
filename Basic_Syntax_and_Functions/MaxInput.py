s=input().split(',')
print(max(s))

s='9e10'
print(type(s)==float)

s = "9e10"
if type(eval(s)) == type(12.0):
    print("True")
else:
    print("False")

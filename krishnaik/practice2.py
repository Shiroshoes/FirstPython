#1
check = list(map(int, input("Enter a number: ").split()))

new = all(x > 0 for x in check)

print(f"All numbers are positive?: {new}")


print("\n")


#2
evod = list(map(int, input("Enter a number: ").split()))

s = any(x % 2 == 0 for x in evod)

print(f"Any even number? {s}")


print("\n")


#3
sa = list(map(int, input("Enter numbers: ").split()))

same = len(set(sa)) == 1

print(f"All numbers are the same? {same}")


print("\n")


#4
lst = list(map(int, input("Enter List: ").split()))
n = int(input("Enter number to find: "))

find = any(lt == n for lt in lst)

print(f"Number exists? {find}")


print("\n")


#5
l = list(map(int, input("Enter numbers: ").split()))

if not l:
    none = False
    print(f"List is empty? {none}")
else:
    print("List is empty? True")
    

print("\n")


#6
en = list(map(int, input("Enter numbers: ").split()))

c = all(x > 10 for x in en)

print(f"All numbers greater than 10? {c}")
    

print("\n")



#7
ne = list(map(int, input("Enter numbers: ").split()))

a = any(x < 0 for x in ne)

print(f"Any negative number? {a}")


print("\n")


#8
bo = list(map(str, input("Enter boolean values (True/False): ").split()))

ol = any(x == True for x in bo)

print(f"At least one True? {ol}")


print("\n")


#9
bot = list(map(int, input("Enter a numbers: ").split()))

both = any(x > 0 for x in bot) and any(x < 0 for x in bot)

print(f"Contains both positive and negative? {both}")


print("\n")


#10
dup = list(map(int, input("Enter a number: ").split()))

se = set(dup)

como = len(dup) != len(se)

print(f"Contains duplicates? {como}")
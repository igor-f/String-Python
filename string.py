s=input("Please, enter your string: ")
while len(s)<5:		
	s=input("Length of your string must be >5: ")
print(s[2])
print(s[len(s)-2])
print(s[:5])
print(s[:len(s)-2])
print(s[1::2])
print(s[2::2])
print(s[::-1])
print(s[::-2])
print(len(s))
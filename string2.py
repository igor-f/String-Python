s=input("Please, enter your string: ")
while len(s)<5:		
	s=input("Length of your string must be >= 5: ")
print("Third symbol: ",s[2])
print("Penultimate symbol: ",s[len(s)-2])
print("First five symbols: ",s[:5])
print("Except for the last two symbols: ",s[:len(s)-2])
print("Symbols with even indexes: ",s[1::2])
print("Symbols with odd indexes: ",s[2::2])
print("String in reverse order: ",s[::-1])
print("The characters in reverse order through one: ",s[::-2])
print("Length of the string: ",len(s))
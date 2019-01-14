#Reading a text file
with open('name.txt') as f:
	full_text=f.read()

print("Hello, my name is " + full_text)

#writing a text file

with open('hello.txt', 'w') as f:
	f.write("Hello, my name is " + full_text)
	f.write('\n')
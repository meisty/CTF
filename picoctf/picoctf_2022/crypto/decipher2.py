file = open("message2.txt", "r")
lines = file.readline()

numbers = lines.split()

result = ""

alphanum = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
for number in numbers:
	mod = int(number) % 41
	inverse = pow(mod, 41-2, 41)
	result += alphanum[inverse - 1]

print(result)
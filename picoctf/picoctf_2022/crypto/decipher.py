
f = open("message.txt", "r")
lines = f.readline()

words = lines.split()

result = ""

alphanum = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
for word in words:
    result += (alphanum[int(word) % 37])


print(result)

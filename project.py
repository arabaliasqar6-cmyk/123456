names = ["John", "Oscar", "Jacob"]
file = open("names.txt", "w+")
file.write("john"+"\n")
file.write("Oscar"+"\n")
file.write("Jacob"+"\n")
file.close()
file= open("names.txt", "r")
print(file.read())
file.close()
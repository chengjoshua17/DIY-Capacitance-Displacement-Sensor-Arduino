openFile = open("data.txt", "r")
readFile = openFile.read()
checkemptyspace = readFile.partition("\n\n")
data1=checkemptyspace[0]
data2=checkemptyspace[2]
openFile.close()
text_file = open("data.txt", "w")
text_file.write(data1)
text_file.write("\n")
text_file.write(data2)
text_file.close()


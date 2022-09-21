#READING FILES
f = open('testfile.txt', 'r') #'r' means in read mode
#print(f) #print the file object, not the content of the file
#print(f.readline()) #print the first line of the file
#print(f.readlines()) #print all the lines of the file in a list of strings

for line in f.readlines():
    print(line.strip()) #strip for removing the \n character of the print function



#WRITING FILES
f = open('testfile_output.txt', 'w') #'w' means in write mode with overwrite.

f.write('Line 3\n')
f.write('Line 4\n')

f.close()

#APPENDING FILES
f = open('testfile_output.txt', 'a') #'a' means in append mode.

f.write('Line 22\n')
f.write('Line 55\n')

f.close()

#better way to have in mind the very important close() statement,
#is to use the block With, it closes automatically the file without specify it
with open('testfile_output.txt', 'a') as f:
    f.write('something\n')
    f.write('something else\n')




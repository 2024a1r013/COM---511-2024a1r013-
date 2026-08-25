import os
list = []
for items in os.listdir():
    list.append(items)
for i in list:
    print(i)    
print(os.getcwd()) # gives the current working directory .
#os.mkdir("myfolder") # create a  new folder 
if os.path.exists("myfolder"):
    print("Path Exists!!!")
else:
    print("Path doesnt exists")    
#os.rename("myfolder","firstfolder")    #changes the folder name
print(os.path.isfile("1.py"))
print(os.path.isdir("firstfolder"))
#os.remove("1.py")
# os.rmdir("firstfolder")
# os.rmdir("rough")
a = 30 
b = "harry" 
c = 71.22
print(a,b,c)
print(type(a))
print(str(31)) # converts integer into string
a = input("Enter name: ")
print(a)

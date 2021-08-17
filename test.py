'''
a = 10
b = 20
print (a,b)
print (a,b,sep=",")
print(a,b,sep="---")

print(5*' Hai')

print("Color")
print("Purple")
print("Color", end=' ')
print("Purple", end='')

x = 10.012345
y = 10
print('Value of x = %i' %x)
print('Value of x = %f' %x)
print('Value of x = %i' %y)
print('Value of x = %f' %x)
print('Value of x = %8.2f' %x)
name="Sri"
print('Hai %s' % name)
print('Hai %5s' %name)
print('index 0 is %c and 1 is %c' %(name[0], name[1]))
print('Hai %s' %(name[0:2]))

n1,n2,n3=1,2,3
print('Number1 is {0}'.format(n1))
print('Number1 is {0}, Number2 is {1}, Number3 is {2}' .format(n1,n2,n3))
'''

file1 = open("MyFile.txt","w+")

file1=open("myfile.txt","w")
L=["This is Delhi \n",  "This is Paris \n", "This is London \n"]
file1.write("Hello \n")
file1.writelines(L)
file1.close()
file1=open("myfile.txt","r+")
print("Output of Read function is ")
print(file1.read())
print()
file1.seek(0)
print("Output of Readline function is ")
print(file1.readline())
print()
file1.seek(0)
print("Output of Read(9) function is ")
print(file1.read(9))
print()
file1.seek(0)
print("Output of Readline(9) function is ")
print(file1.readline(9))
print()
file1.seek(0)
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close


file1=open("myfile.txt","w")
L=["This is Delhi \n",  "This is Paris \n", "This is London \n"]
s="Hello\n"

file1.write(s)

file1.writelines(L)
file1.close()
file1=open('myfile.txt','r')
print(file1.read())
file1.close()
'''
import shutil
source = "File1.txt"
destination= "D"

dest=shutil.move(source,destination)
'''
'''
import os

file="File1.txt"
location="D/"
path=os.path.join(location,file)
os.remove(path)
'''
'''
from datetime import datetime

log_file = "example2.log"

def read_log(log):
    with open(log,"r") as f:
        print(f.read())

def write_log(log,name):
    log_time=str(datetime.now())
    with open(log,"a") as f:
        f.writelines("Entry logged at: {} by {}\n".format(log_time,name))

if __name__=='__main__':
    name=input("What is your name? ")
    print("Adding new log entry")
    write_log(log_file,name)
    print("")

    print("Log File Contents")
    print("-----------------")
    read_log(log_file)
'''
author={"name":"Hank","color":"green","shape":"circle"}

colors=['blue','green','red']

favoruite_colors=[
    {
        "student":"Mary",
        "color":"red"
    },
    {
        "student": "John",
        "color": "blue"
    }
]
if __name__=='__main__':
    print("The author's name is {}.".format(author["name"]))
    print("His favorite color is {}.".format(author["color"]))
    print("")

    print("The current colors are:")
    for color in colors:
        print(color)
    print("")

    new_color=input("What is your favorite color? ")
    if new_color==author["color"]:
        print("You have the same favorite color as {}".format(author["name"]))
        print("")

    if new_color not in colors:
        print("That's a new color, adding it to the list!")
        colors.append(new_color)
        message=("There are now {} colors in the list. ".format(len(colors)))
        message += "The color you added was {}.".format(colors[3])
        print(message)
    else:
        pass
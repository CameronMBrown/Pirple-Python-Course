#Pirple Assignment 8 - file I/O
# a basic note taking/editing app

import os.path
from os import remove
from shutil import move

def writeToFile(fileName, format):
  file = open(fileName, format)
  note = str(input("Add your note here:"))
  file.write(note + "\n")
  file.close()

def editLine(fileName):
  count = 1
  file = open(fileName, "r")
  data = file.readlines() # insert file contents into array 
  file.close()
  if len(data) == 0: 
    #tried to edit an empty file
    print("file is empty, switching to append mode.")
    writeToFile(fileName, "a")
  for line in data: 
    #show the user the file first
    print(str(count) + " : " + str(line), end="")
    count += 1 
  lineNum = int(input("\n which line would you line to replace?")) # get line to be replaced
  replace = str(input("replace line " + str(lineNum) + " with:")) # get replacement text
  data[lineNum-1] = replace + "\n"
  file = open(fileName, "w")
  file.writelines(data)
  file.close()

def takeNote():
  makeNote = True
  while(makeNote): 
    # allow the user to keep taking notes without needing to run this script multiple times
    fileName = str(input("What file would you like to edit?"))
    if os.path.exists(fileName):
      print("I have found a file with that name, how would you like to continue?")
      action = str(input("type 'read' to see the file, \n'del' to delete and start over, \n'add' to append to the file\n'line' to replace part of the document.\n"))
      if(action == "read"):
        file = open(fileName, "r")
        print(file.read())
        file.close()
      elif (action == "del"):
        writeToFile(fileName, "w")
      elif (action == "line"):
        editLine(fileName)
      else:
        writeToFile(fileName, "a")
    else:
      writeToFile(fileName, "w")
    if(str(input("type 'close' to stop taking notes")) == "close"):
      makeNote = False
  
takeNote()


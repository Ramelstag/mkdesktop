#!/bin/python
import sys
import os
import shutil

#bullshit handling
if len(sys.argv) > 2:
    sys.exit("Too many arguments. please enter only a single file's name.")

if len(sys.argv) < 2:
    sys.exit("File not specified")

if not os.path.exists(sys.argv[1]):
    sys.exit("Error: file " + sys.argv[1] + " does not exit")

if os.path.isdir(sys.argv[1]):
    sys.exit("Error: " + sys.argv[1] + " is a directory")


file = open(sys.argv[1] + ".desktop", "w")
#header and name
file.write("[Desktop Entry]\n" + "Name=" + str.capitalize(sys.argv[1]) + "\nType=Application\n")
#exec
file.write("Exec=" + os.getcwd() + "/" + sys.argv[1] + "\n")
#path
file.write("Path=" + os.getcwd() + "\n")
#less important stuff (needlessly concatenated yes i know shut up it's more readable that way)
file.write("Icon=\n" + "Comment=\n" + "Category=\n")    #i don't know if there's an icon that would be
file.close                                              #available anywhere that i could use. i guess i could make one...

os.system("chmod +x " + sys.argv[1]) #making sure the target is executable

if os.path.exists("/home/" + os.environ["USER"] + "/.local/share/applications"): #sanity check

    option = input("Would you like to move the output .desktop to ~/.local/share/applications? [y/N]")
    
    if option.lower() in ["yes", "y"]:      #yes i know that python has a switch...case thing, i tried it
        print("Moving output to local applications folder...")  # but was having issues with it so i used elif
        shutil.move(sys.argv[1] + ".desktop", "/home/" + os.environ["USER"] + "/.local/share/applications/" + sys.argv[1] + ".desktop")
        print("Done. You may want to change the Name line, add a comment and an icon.")
    
    
    elif option.lower() in ["no", "n"]:
        print("Done.")
    else:
        print("Defaulted to no. Done.")

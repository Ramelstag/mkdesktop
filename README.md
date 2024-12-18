# mkdesktop

Simple Python script that makes basic .desktop entries for a target file

----

## Usage
  
Simply run `mkdesktop.py <file>`, and it will make a .desktop file targeting that file, and asks you if you want to add it to the applications folder in ~/.local/

## "Installation"

If you wish to use this script on your computer, all you need to do is to move the script to `/usr/bin` or somewhere else in your $PATH variable, but preferably in `/usr/bin`. Example: `sudo mv mkdesktop.py /usr/bin/mkdesktop` (you can remove the .py so you won't need to type it when calling the script). I have no idea if doing it like this is fine or not, considering it's a single tiny little script, it most likely can't hurt.
  
I will not be making a proper package for this (I don't even know how to do it), be aware that this script was made by someone not very familiar with python and just a novice programmer in general. If you want to make a package for it, feel free to do so (GPL enforces that), but I do not guarantee that it won't ever fail. Maybe in the future though.
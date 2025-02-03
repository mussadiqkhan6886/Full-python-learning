import sys # A library which relates with command line 

if len(sys.argv) < 2: # If length of sys.argv  is smaller than 2 than say too few argments and exit program
    sys.exit('Too few Arguments') # sys.exit() means exit entire program

for arg in sys.argv[1:]: # for every element in list of sys.argv[1:] slice it and execute
    print("My name is", arg)
    
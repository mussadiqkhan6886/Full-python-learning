# import hello and goodbye function fron saying
import sys
from saying import hello, goodbye

if len(sys.argv) == 2: # If len of command line is equal to 2 than execute 
    hello(sys.argv[1]) # hello(), arguement sys.argv[1] first index 
    

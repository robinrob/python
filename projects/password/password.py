import sys
from generator import Generator

DEFAULT_LENGTH = 10

length = DEFAULT_LENGTH
if len(sys.argv) >= 2:
    length = int(sys.argv[1])
    
print(Generator().generate(length))
    




# for-loop__loop_structure.py

# output: 0 1 2 3 4 5 6 7 8 9 10
# print command with no newline, newline is replaced by space character
for i in range(0,11,1):
    print i,

print # print newline

# output: 0 space 1
print '0',
print '1',

print # print newline

# output: 01 with no space in between the two characters
import sys
sys.stdout.write('0')
sys.stdout.write('1')
sys.stdout.flush()

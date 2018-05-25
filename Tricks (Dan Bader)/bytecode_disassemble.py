# use python's built-in 'dis' module to
# disassemble functions and inspect
# their CPython VM bytecode

import dis

def greet(name):
    return 'Hello, ' + name + '!'

print(greet('MC'))

dis.dis(greet)

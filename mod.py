import fn
'''Welcome to the module'''
s='Ravi Teja'
def display():
    '''this module displays print message'''
    print('hello')
    print(__name__)
    #print(dir(display))
display()
#print(dir())
#print(dir(fn))
print(display.__doc__)

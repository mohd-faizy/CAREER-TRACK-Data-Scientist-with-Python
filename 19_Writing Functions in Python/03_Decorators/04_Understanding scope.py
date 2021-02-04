# 04 - What four values does this script print?

x = 50

def one():
    x = 10

def two():
    global x
    x = 30

def three():
    x = 100
    print(x)

for func in [one, two, three]:
    func()
    print(x)

'''Output
50
30
100
30
------------------------------------------------------------------------------
- one() doesn't change the global x, so the first print() statement prints 50.

- two() does change the global x so the second print() statement prints 30.

- The print() statement inside the function three() is referencing the x value 
  that is local to three(), so it prints 100.

- But three() does not change the global x value so the last print() statement 
  prints 30 again.
------------------------------------------------------------------------------
'''


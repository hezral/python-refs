#!/usr/bin/env python3

global last
global new

last = 0
new = 1

print(last)
print(new)

def selected(lasts, news):
    global last
    global new
    new = lasts + 1
    last = news + 1

    #return new, last

   

print(selected(last, new))



print(last)
print(new)

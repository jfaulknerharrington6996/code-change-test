import time

bottles = 10
for x in range(bottles,0,-1):
    print("{0} green bottle hanging on the wall.".format(x))
    time.sleep(1)
    print("{0} green bottles hanging on the wall.".format(x))
    time.sleep(1)
    print("And if 1 green bottle should acidentally fall,")
    time.sleep(1)
    print("There'll be {0} green bottles hanging on the wall.\n".format(x-1))
    time.sleep(1)

ar = range(9)[::-1]
print (ar)

def loopda(*,a):
    for i in a:
        print (i)
        continue

loopda(a=ar)
loopda(a=range(9))

def openFile(path):
    try:
        f = open(path, "r")
        return f;
    except:
        print (path+" could not be opened")
        return f;


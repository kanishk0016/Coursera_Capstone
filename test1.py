def main ():
    print("before import")
    import math

    print("before functionA")
    def functionA():
        print("Function A")
    
    print("before functionB")
    def functionB():
        print("Function B {}".format(math.sqrt(100)))
    
    print("before __name__ guard")
    functionA()
    functionB()
    
if __name__ == '__main__':
    main()
else:
    print ("test1 file has been imported here")
    print("after __name__ guard")
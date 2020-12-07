print("my module attribute is", __name__)
def printX():
    print("executing printX() function ...")

def main():
    print("call printX function from command!")
    printX()
if __name__ == "__main__":
    main()
else:
    print("it is imported")
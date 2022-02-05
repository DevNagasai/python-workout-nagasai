class myclass():
    def method1(self):
        print("my class meethod1: \n")

    def method2(self,somestring):
        print("My class method2 " + somestring)

class anotherclass(myclass):
    def method1(self):
        myclass.method1(self)
        print("another class method1")
    def method2(self,somestring):
        print(somestring)


def main():
    c = myclass()
    c.method1()
    c.method2("this is a  string")
    c = anotherclass()
    c.method1()
    c.method2("This is also a string from another class")

if __name__ == "__main__":
    main()    
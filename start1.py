class Test:
    class_name = "class variable"

    def __init__(self):
        self.instance_name = "no name"

    def test1(self, name="instance name"):
        self.instance_name = name


if __name__ == "__main__":
    test_instance = Test()
    test_instance.test1()
    print(test_instance.instance_name)
    print(Test.instance_name)

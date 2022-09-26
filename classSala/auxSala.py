class Format:
    def formatation_title(self, msg: str):
        size = len(msg) + 30
        print("~" * size)
        print("{:^45}".format(msg))
        print("~" * size)
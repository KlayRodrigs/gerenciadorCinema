class Format:
    def formatation_title(self, msg: str):
        size = len(msg) + 55
        print("~" * size)
        print("{:^70}".format(msg))
        print("~" * size)
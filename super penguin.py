class bird:
    def __init__(self):
        print("bird is ready")

    def whoisThis(self):
        print("bird")

    def swim(self):
        print("swim faster")

class penguin(bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("run faster")

peggy = penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
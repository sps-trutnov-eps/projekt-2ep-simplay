import time

class TimeCount:

    def __init__(self):
        self.start_time = time.time()
        self.current_time = 0
        self.played_time = 0
        with open("data/time.txt", "r") as f:
            self.played_time = f.read()


    def end(self) -> None:
        self.current_time = time.time()
        self.played_time = int(self.current_time) - int(self.start_time) + int(self.played_time)
        print(self.played_time)

        with open("data/time.txt", "w") as f:
            f.write(str(self.played_time))

    @staticmethod
    def getPlayedTime() -> int:
        with open("data/time.txt", "r") as f:
            return round(int(f.read()) / 3600, 2)
import time


class Traffic_color:
    __color = [['\033[31m\r', 7], ['\033[33m\r', 3], ['\033[32m\r', 7],
               ['\033[33m\r', 3]]  # перенос каретки не работает

    def running(self):
        while True:
            for col in self.__color:
                print(f"{col[0]}o")
                time.sleep(col[1])


lightning1 = Traffic_color()
lightning1.running()

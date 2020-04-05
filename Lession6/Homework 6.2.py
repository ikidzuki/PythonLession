class Road:
    __depth = 8  # Толщина полотна
    __weight = 21  # Масса на кв. м.

    def __init__(self, length, width):
        self._length = length  # Длинна полотна
        self._width = width  # Ширина полотна

    def all_mass_asphalt(self):
        print(f"Масса полотна = {self._length * self._width * self.__depth * self.__weight / 1000} тонн")


asphalt_road1 = Road(25, 3550)
asphalt_road1.all_mass_asphalt()


material = ['Al', 'Ti', 'Fe', 'Carbon']
fork_type = ['air', 'spring', 'elastomer']


class Bicycle:
    def __init__(self, wheels_number: int, frame_material: str, wheel_size: float):
        """
        Создание базового образа велосипеда
        :param wheels_number: количество колес велосипеда
        :param frame_material: материал, из которой сделана рама велосипеда.
        :param wheel_size: размер колес
        Атрибут self._wheels инкапсулирован, потому что подразумеваются только двухколесные велосипеды.
        Увеличение колес возможно, но, тогда разработчик снимает с себя ответственность за дальнейшую
        работоспособность кода.
        """
        self._wheels = wheels_number
        self.check_material_of_frame(frame_material)
        self.wheel_size = wheel_size

    @property
    def wheels(self) -> int:
        return self._new_wheel_set

    @wheels.setter
    def wheels(self, value) -> None:
        if not isinstance(value, int):
            raise ValueError('Неправильный тип. Ожидается int')
        if value > 2 or value < 2:
            raise ValueError('Изменение количества колес может привести к нестабильной работоспособности программы. Ожидается 2')
        self._new_wheel_set = value

    def __str__(self) -> str:
        """
        :return: вывод основной информации о велосипеде
        """
        return f"Количество колес {self._wheels}. Тип рамы {self.type_of_frame}"

    def __repr__(self) -> str:
        """
        :return: вывод всей информации о велосипеде
        """
        return f"{self.__class__.__name__}(wheels_number={self._wheels!r}, frame_material={self.type_of_frame!r}, wheel_size={self.wheel_size!r})"

    def bike_configuration(self, wheels_number: int, frame_material: str, wheel_size: float) -> str:
        """
        Конфигурация велосипеда с учетом параметров
        :param wheels_number: количество колес велосипеда
        :param frame_material: материал, из которой сделана рама велосипеда.
        :param wheel_size: размер колес
        :return: модель велосипеда по сконфигурированным параметрам
        """
        ...

    def check_material_of_frame(frame: str) -> None:
        if frame not in material:
            raise ValueError('Отсутствует такой материал. Ожидается: Al, Ti, Fe, Carbon')


class CityBike(Bicycle):
    def __init__(self, wheels_number: int, frame_material: str, wheel_size: float, bicycle_trunk: str):
        """
        Создание городского велосипеда с багажником
        :param wheels_number: количество колес велосипеда
        :param frame_material: материал, из которой сделана рама велосипеда.
        :param wheel_size: размер колес
        :param bicycle_trunk: багажник велосипеда. Может быть составным или цельным(composite или full)
        Перегрузка нужна для установки багажника в стандартную модель велосипеда
        """
        super().__init__(wheels_number, frame_material, wheel_size)
        self.type_of_trunk = bicycle_trunk

    def __repr__(self) -> str:
        """
        :return: вывод всей информации о велосипеде
        """
        return f"{self.__class__.__name__}(wheels_number={self._wheels!r}, frame_material={self.type_of_frame!r}, wheel_size={self.wheel_size!r}, trunk={self.type_of_trunk!r})"

    def bike_configuration(self, wheels_number: int, frame_material: str, wheel_size: float) -> str:
        """
        Конфигурация велосипеда с учетом параметров
        :param wheels_number: количество колес велосипеда
        :param frame_material: материал, из которой сделана рама велосипеда.
        :param wheel_size: размер колес
        :return: модель велосипеда по сконфигурированным параметрам
        Перегрузка нужна, чтобы учесть наличие багажника и пересчитать основные параметры рамы
        """
        super().bike_configuration(wheels_number, frame_material, wheel_size)
        ...

class MountainBike(Bicycle):
    def __init__(self, wheels_number: int, frame_material: str, wheel_size: float, fork: str):
        """
        Создание городского велосипеда с багажником
        :param wheels_number: количество колес велосипеда
        :param frame_material: материал, из которой сделана рама велосипеда.
        :param wheel_size: размер колес
        :param fork: передний амортизатор. может быть air, spring, elastomer
        Перегрузка нужна для установки переднего амортизатора в стандартную модель велосипеда
        """
        super().__init__(wheels_number, frame_material, wheel_size)
        self.check_fork(fork)
        self.fork = fork

    def __repr__(self):
        """
        :return: вывод всей информации о велосипеде
        """
        return f"{self.__class__.__name__}(wheels_number={self._wheels!r}, frame_material={self.type_of_frame!r}, wheel_size={self.wheel_size!r}, fork={self.fork!r})"

    def bike_configuration(self, wheels_number: int, frame_material: str, wheel_size: float) -> str:
        """
        Конфигурация велосипеда с учетом параметров
        :param wheels_number: количество колес велосипеда
        :param frame_material: материал, из которой сделана рама велосипеда.
        :param wheel_size: размер колес
        :return: модель велосипеда по сконфигурированным параметрам
        Перегрузка нужна, чтобы учесть наличие вилки и пересчитать основные параметры рамы
        """
        super().bike_configuration(wheels_number, frame_material, wheel_size)
        ...

    def check_fork(fork: str) -> None:
        if fork not in fork_type:
            raise ValueError('Отсутствует такая вилка. Ожидается: air, spring, elastomer')


if __name__ == "__main__":
    pass

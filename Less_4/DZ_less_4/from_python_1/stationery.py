# 6-5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title=""):
        self.title = title

    def draw(self):
        # print("Запуск отрисовки")
        return "Запуск отрисовки"

    def declination(self, title):
        if type(title) == str and not title.isdigit():
            if title == "":
                return ""
            elif title[-1] == "а":
                title = title.replace(title[-1], "ой")
                return title
            elif title[-1] == "я":
                title = title.replace(title[-1], "ей")
                return title
            else:
                title = title + "ом"
                return title
        else:
            return ""


class Pen(Stationery):
    def draw(self):
        # print(f"Запуск отрисовки {super().declination(self.title)}")
        return f"Запуск отрисовки {super().declination(self.title)}"


class Pencil(Stationery):
    def draw(self):
        # print(f"Запуск отрисовки {super().declination(self.title)}")
        return f"Запуск отрисовки {super().declination(self.title)}"


class Handle(Stationery):
    def draw(self):
        # print(f"Запуск отрисовки {super().declination(self.title)}")
        return f"Запуск отрисовки {super().declination(self.title)}"


if __name__ == '__main__':
    stationery = Stationery()
    pen = Pen("ручка")
    pencil = Pencil("карандаш")
    handle = Handle("маркер")

    # stationery.draw()
    # pen.draw()
    # pencil.draw()
    # handle.draw()
    print(stationery.draw())
    print(pen.draw())
    print(pencil.draw())
    print(handle.draw())
"""Задача "Range - это просто":
Создайте пользовательский класс исключения StepValueError, который наследуется от ValueError.
Наследования достаточно, класс оставьте пустым при помощи оператора pass.

Создайте класс Iterator, который обладает следующими свойствами:
Атрибуты объекта:
start - целое число с которого начинается итерация.
stop - целое число на котором заканчивается итерация.
step - шаг с которой совершается итерация.
pointer - указывает на текущее число в итерации (изначально start)
Методы:
__init__(self, start, stop, step=1) - принимающий значения старта и конца итерации, а также шага. В этом методе в первую очередь проверяется step на равенство 0. Если равно, то выбрасывается исключение StepValueError('шаг не может быть равен 0')
__iter__ - метод сбрасывающий значение pointer на start и возвращающий сам объект итератора.
__next__ - метод увеличивающий атрибут pointer на step. В зависимости от знака атрибута step итерация завершиться либо когда pointer станет больше stop, либо меньше stop. Учтите это при описании метода.

Пункты задачи:
Создайте класс исключения StepValueError.
Создайте класс Iterator и опишите его атрибуты и методы.
Создайте несколько объектов класса Iterator и совершите итерации с ними при помощи цикла for.
class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if self.step > 0:
            if self.pointer >= self.stop:
                raise StopIteration
        elif self.step < 0:
            if self.pointer <= self.stop:
                raise StopIteration

        result = self.pointer
        self.pointer += self.step
        return result

# Пример использования
try:
    my_iterator = Iterator(1, 10, 2)
    for num in my_iterator:
        print(num)
except StepValueError as e:
    print(e)"""
# Определяем пользовательский класс исключения, наследуемый от ValueError
class StepValueError(ValueError):
    pass  # Класс пустой, используется только для выбрасывания исключений

# Определяем класс Iterator
class Iterator:
    # Метод инициализации, принимающий значения начала, конца и шага
    def __init__(self, start, stop, step=1):
        # Проверяем, равен ли шаг нулю
        if step == 0:
            # Если шаг равен 0, выбрасываем исключение StepValueError
            raise StepValueError('шаг не может быть равен 0')
        # Инициализируем атрибуты объекта
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start  # Устанавливаем указатель на начало итерации

    # Метод, возвращающий итератор
    def __iter__(self):
        self.pointer = self.start  # Сбрасываем указатель на начальное значение
        return self  # Возвращаем сам объект итератора

    # Метод для получения следующего значения итерации
    def __next__(self):
        # Проверяем, достигнут ли предел итерации
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            # Если предел достигнут, выбрасываем StopIteration
            raise StopIteration
        current = self.pointer  # Сохраняем текущее значение указателя
        self.pointer += self.step  # Увеличиваем указатель на шаг
        return current  # Возвращаем текущее значение

# Пример использования
try:
    # Создаем итератор с шагом 0 (это вызовет исключение)
    iter1 = Iterator(100, 200, 0)
    # Пытаемся итерироваться по итератору
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    # Обрабатываем исключение и выводим сообщение об ошибке
    print('Шаг указан неверно')

# Создаем несколько итераторов с различными параметрами
iter2 = Iterator(-5, 1)  # Итератор от -5 до 1
iter3 = Iterator(6, 15, 2)  # Итератор от 6 до 15 с шагом 2
iter4 = Iterator(5, 1, -1)  # Итератор от 5 до 1 с шагом -1
iter5 = Iterator(10, 1)  # Итератор от 10 до 1 с шагом по умолчанию (1)

# Итерируемся по итератору iter2 и выводим значения
for i in iter2:
    print(i, end=' ')
print()  # Печатаем новую строку

# Итерируемся по итератору iter3 и выводим значения
for i in iter3:
    print(i, end=' ')
print()  # Печатаем новую строку

# Итерируемся по итератору iter4 и выводим значения
for i in iter4:
    print(i, end=' ')
print()  # Печатаем новую строку

# Итерируемся по итератору iter5 и выводим значения
for i in iter5:
    print(i, end=' ')
print()  # Печатаем новую строку




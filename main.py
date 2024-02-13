#if __name__ == "__main__":
    # Write your solution here
class Phone:
    """" Базовый  класс телефоны """""
    def __init__(self, model: str, mem: int, age: int):
        ''''''' model - количество встроенной памяти' \
        ' diag - диагональ экрана' \
        ' age - время владения телефоном(полных лет) '''''''

        self.model = model
        self.mem = mem
        self.age = age


    def __str__(self):
        return f"Телефон {self.model}. Диагональ {self.mem}. Возраст {self.age}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.model!r}, author={self.mem!r}), age={self.age}"



    def sell_count(self, model: str, mem: int, age: int):
        """" Метод, расчитывающий стоимость продажи телефона """

    def mob_net_oper(self,  model: str):
        """" Метод, подбирающий самого выгодного мобильного оператора на основе модели телефона """


class Touchscreen(Phone):
    def __init__(self, model: str, mem: int, age: int, diag: float):
        """" diag - диагональ экрана в дюймах """
        super().__init__(model, mem, age)
        self.diag = diag

    @property
    def diag(self) -> float:
        return self._diag
    @diag.setter
    def diag(self, new_diag: int) -> None:
        if not isinstance(new_diag, float):
            raise TypeError("Диагональ экрана быть типа float")
        if new_diag <= 0:
            raise ValueError("Диагональ экрана должна быть положительным числом")
        self._diag = new_diag

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._model!r}, author={self._mem!r}), age={self._age!r}, diagonal={self._diag!r}"

    def sell_count(self, model: str, mem: int, age: int, diag: float):
        """" Метод, расчитывающий стоимость продажи телефона.
         Метод был перегружен, так как добавилась новая переменная, которая в значительной степени влияет на стоимость телефона"""

tp = Touchscreen

# pass

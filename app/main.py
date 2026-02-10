from abc import ABC, abstractmethod


class Validator(ABC):
    def __set_name__(
        self,
        owner,
        name
    ) -> None:
        self.protected_name = "_" + name

    def __get__(
        self,
        obj,
        objtype=None
    ):
        return getattr(obj, self.protected_name)

    def __set__(
        self,
        obj,
        value
    ):
        self.validate(value)
        setattr(obj, self.protected_name, value)

    @abstractmethod
    def validate(
        self,
        value
    ):
        pass


class Number(Validator):
    def __init__(
        self,
        min_value: int,
        max_value: int
    ):
        self.min_value = min_value
        self.max_value = max_value

    def validate(
        self,
        value: int
    ):
        if not isinstance(value, int):
            raise TypeError("Quantity should be integer")
        elif value < self.min_value and value > self.max_value:
            raise ValueError(
                f"Quantity should not be less than {self.min_value}",
                f" and greater than {self.max_value}."
            )


class OneOf:
    pass


class BurgerRecipe:
    def __init__(
        self,
        buns: int,
        cheese: int,
        tomatoes: int,
        cutlets: int,
        eggs: int,
        sauce: str
    ) -> None:
        self.buns = buns
        self. cheese = cheese
        self.tomatoes = tomatoes
        self.cutlets = cutlets
        self.eggs = eggs
        self.sauce = sauce

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


class Number:
    pass


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

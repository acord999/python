from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def consumption(self):
        "Must be rewritten"
        pass


class Coat(Clothes):
    @property
    def consumption(self):
        return self.param / 6.5 + 0.5


class Suit(Clothes):
    @property
    def consumption(self):
        return 2 * self.param + 0.3


coat_obj = Coat(10)
suit_obj = Suit(1.80)
print(coat_obj.consumption)
print(suit_obj.consumption)

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, expenditure):
        self.expenditure = expenditure

    @abstractmethod
    def expend(self):
        pass


class Coat(Clothes):
    @property
    def expend(self):
        V = self.expenditure
        print(f'Расход ткани для плаща, при {V} размере = {V / 6.5 + 0.5}')


class Suit(Clothes):
    @property
    def expend(self):
        H = self.expenditure
        print(f'Расход ткани для костюма, при {H} росте = {2 * H + 0.3}')


suit1 = Suit(176)
suit1.expend

coat1 = Coat(320)
coat1.expend

from abc import ABC, abstractmethod

class AbstracFactory(ABC):
    @abstractmethod
    def createButton(self):
        pass

    @abstractmethod
    def createCheckbox(self):
        pass
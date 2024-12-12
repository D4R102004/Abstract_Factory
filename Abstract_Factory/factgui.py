from abc import ABC, abstractmethod

class AbstractMaker(ABC):
    # Constructor ==============================================================================================================================================
    @abstractmethod
    def __init__(self, catalogue: list):
        self._catalogue = catalogue
    
    # Properties ===========================================================================================================================
    @property
    def catalogue(self):
        return self._catalogue
    
    # Methods ===========================================================================================================
    # Abstract
    @abstractmethod
    def createButton(self):
        pass

    @abstractmethod
    def createCheckbox(self):
        pass

    # Concrete
    def get_catalogue(self):
        return self.catalogue
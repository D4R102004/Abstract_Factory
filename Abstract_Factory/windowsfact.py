from abc import ABC, abstractmethod
from factgui import AbstractMaker as GUI

class WindowsMaker(GUI):
    def __init__(self, catalogue):
        super().__init__(catalogue)

    def createButton(self):
        pass
    
    def createCheckbox(self):
        pass
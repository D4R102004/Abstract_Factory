from abc import ABC, abstractmethod
from Abstract_Factory.factgui import AbstracFactory as GUI

class LinuxFactory(GUI):
    def createButton(self):
        return super().createButton()
    
    def createCheckbox(self):
        return super().createCheckbox()
class AbstractFactory:
    def __init__(self):
        self._p = 3
    @property
    def p(self):
        return self._p

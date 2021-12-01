from abc import ABCMeta, abstractmethod

class GamePainter:

    __metaclass__ = ABCMeta

    @classmethod

    @abstractmethod
    
    def paint(self,image): raise NotImplementedError

    def getWidth(self): return NotImplementedError

    def getHeight(self): return NotImplementedError




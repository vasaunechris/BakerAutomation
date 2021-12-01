
from abc import ABCMeta, abstractmethod
from pygame import event

class GameController(event):

    __metaclass__ = ABCMeta

    @abstractmethod
    def getCommand(cls): raise NotImplementedError

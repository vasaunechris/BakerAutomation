from abc import ABCMeta, abstractmethod

class Game:

    __metaclass__ = ABCMeta

    @abstractmethod
    def etatGame(cls): raise NotImplementedError

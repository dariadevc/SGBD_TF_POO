from abc import ABC, abstractmethod


class Pdf(ABC):
    @abstractmethod
    def inicializa_pdf(self):
        pass

    @abstractmethod
    def guarda_pdf(self, pdf):
        pass

    @abstractmethod
    def genera_pdf(self):
        pass

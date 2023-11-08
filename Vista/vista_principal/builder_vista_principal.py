from abc import ABC, abstractmethod


class BuilderVistaPrincipal(ABC):
    @property
    @abstractmethod
    def vista_principal(self) -> None:
        pass

    @vista_principal.setter
    @abstractmethod
    def vista_principal(self) -> None:
        pass

    @abstractmethod
    def produce_encabezado(self) -> None:
        pass

    # @abstractmethod
    # def produce_botones(self) -> None:
    #     pass

    @abstractmethod
    def produce_seccion_empleado(self) -> None:
        pass

    @abstractmethod
    def produce_seccion_animales(self) -> None:
        pass

    @abstractmethod
    def produce_seccion_adoptantes(self) -> None:
        pass

    @abstractmethod
    def produce_seccion_visitantes(self) -> None:
        pass

    @abstractmethod
    def produce_seccion_adopcion(self) -> None:
        pass

    @abstractmethod
    def produce_seccion_visitas_juego(self) -> None:
        pass

    @abstractmethod
    def produce_seccion_informe(self) -> None:
        pass

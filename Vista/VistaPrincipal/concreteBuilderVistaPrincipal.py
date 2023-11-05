from builderVistaPrincipal import BuilderVistaPrincipal
from vistaPrincipal import VistaPrincipal


class ConcreteBuilderVistaPrincipal(BuilderVistaPrincipal):
    def __init__(self):
        self.reset()

    def reset(self):
        self._vista_principal = VistaPrincipal()

    @property
    def vista_principal(self):
        vista_principal = self._vista_principal
        self.reset()
        return vista_principal

    def produce_encabezado(self) -> None:
        pass

    def produce_seccion_empleado(self) -> None:
        pass

    def produce_seccion_animales(self) -> None:
        pass

    def produce_seccion_adoptantes(self) -> None:
        pass

    def produce_seccion_visitantes(self) -> None:
        pass

    def produce_seccion_adopcion(self) -> None:
        pass

    def produce_seccion_visitas_juego(self) -> None:
        pass

    def produce_seccion_informe(self) -> None:
        pass

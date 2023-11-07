from builderVistaPrincipal import BuilderVistaPrincipal


class DirectorVistaPrincipal:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> BuilderVistaPrincipal:
        return self._builder

    @builder.setter
    def builder(self, builder: BuilderVistaPrincipal) -> None:
        self._builder = builder

    def build_vista_admin(self):
        self.builder.produce_encabezado()
        self.builder.produce_seccion_informe()
        self.builder.produce_seccion_empleado()
        self.builder.produce_seccion_animales()
        self.builder.produce_seccion_adopcion()
        self.builder.produce_seccion_adoptantes()
        self.builder.produce_seccion_visitas_juego()
        self.builder.produce_seccion_visitantes()

    def build_vista_encargado(self) -> None:
        self.builder.produce_encabezado()
        self.builder.produce_seccion_informe()
        self.builder.produce_seccion_empleado()
        self.builder.produce_seccion_animales()
        self.builder.produce_seccion_adopcion()
        self.builder.produce_seccion_adoptantes()
        self.builder.produce_seccion_visitas_juego()
        self.builder.produce_seccion_visitantes()

    def build_vista_empleado(self) -> None:
        self.builder.produce_encabezado()
        self.builder.produce_seccion_animales()
        # self.builder.produce_seccion_adopcion()
        # self.builder.produce_seccion_adoptantes()
        # self.builder.produce_seccion_visitas_juego()
        # self.builder.produce_seccion_visitantes()
        

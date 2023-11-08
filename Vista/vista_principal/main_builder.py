from director_vista_principal import DirectorVistaPrincipal
from concrete_builder_vista_principal import ConcreteBuilderVistaPrincipal


director = DirectorVistaPrincipal()
builder = ConcreteBuilderVistaPrincipal()
director.builder = builder

director.build_vista_empleado()
builder.vista_principal.componer_vista()

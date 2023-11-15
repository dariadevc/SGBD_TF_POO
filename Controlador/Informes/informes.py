import os
from datetime import date, datetime
from reportlab.pdfgen import canvas
from pdf import Pdf


class Informe(Pdf):
    def __init__(self, inicio_periodo: date, fin_periodo: date, tipo_informe: str):
        self.__inicio_periodo = inicio_periodo
        self.__fin_periodo = fin_periodo
        self.__nombre_informe = f"{tipo_informe}_{self.__inicio_periodo.strftime('%d %m %y')}-{self.__fin_periodo.strftime('%d %m %y')}"
        self.__ancho = 595.27
        self.__alto = 841.89
        # self.__pdf = None

    def inicializa_pdf(self):
        directorio = os.path.join(os.path.expanduser("~"), "Desktop/Informes/")

        if os.path.exists(directorio):
            nombre_path = str(directorio + self.__nombre_informe + ".pdf")
            print(f"PDF {self.__nombre_informe} generado.")
        else:
            os.mkdir(directorio)
            nombre_path = str(directorio + self.__nombre_informe + ".pdf")
            print(f"Carpeta Informes y PDF {self.__nombre_informe} generados.")

        # self.__pdf = canvas.Canvas(nombre_path, pagesize=(595.27, 841.89))  # A4 pagesize
        return canvas.Canvas(
            nombre_path, pagesize=(self.__ancho, self.__alto)
        )  # A4 pagesize

    def guarda_pdf(self, pdf):
        pdf.save()

    def genera_pdf(self):
        pass


class InformeAdopcionesRescates(Informe):
    def __init__(self, inicio_periodo: date, fin_periodo: date):
        super().__init__(inicio_periodo, fin_periodo, "adopciones_rescates")
        self.__pdf = self.inicializa_pdf()

    def genera_pdf(self):
        # Código para rellenar informe con graficos e información

        # draw a string at x=100, y=800 points
        # point ~ standard desktop publishing (72 DPI)
        # coordinate system:
        #   y
        #   |
        #   |   page
        #   |
        #   |
        #   0-------x

        self.__pdf.drawString(
            50,
            780,
            "Este es un informe acerca de la relación entre las adopciones y los rescates de este mes.",
        )
        inch = 841.89
        self.__pdf.drawImage(
            "Vista/Media/logo-bsf.png",
            self.__ancho / 2,
            self.__alto / 2,
            width=120,
            preserveAspectRatio=True,
            mask="auto",
        )
        # finish page
        self.__pdf.showPage()

        self.guarda_pdf(self.__pdf)


class InformeParticipacionEmpleados(Informe):
    def __init__(self, inicio_periodo: date, fin_periodo: date):
        super().__init__(inicio_periodo, fin_periodo, "participacion_empleados")
        self.__pdf = self.inicializa_pdf()

    def genera_pdf(self):
        # Código para rellenar informe con graficos e información

        # draw a string at x=100, y=800 points
        # point ~ standard desktop publishing (72 DPI)
        # coordinate system:
        #   y
        #   |
        #   |   page
        #   |
        #   |
        #   0-------x

        self.__pdf.drawString(
            50,
            780,
            "Este es un informe acerca de la participación de los empleados en las visitas y las adopciones.",
        )
        # finish page
        self.__pdf.showPage()

        self.guarda_pdf(self.__pdf)


class InformeControlHorariosDias(Informe):
    def __init__(self, inicio_periodo: date, fin_periodo: date):
        super().__init__(inicio_periodo, fin_periodo, "control_horarios_dias")
        self.__pdf = self.inicializa_pdf()

    def genera_pdf(self):
        # Código para rellenar informe con graficos e información

        # draw a string at x=100, y=800 points
        # point ~ standard desktop publishing (72 DPI)
        # coordinate system:
        #   y
        #   |
        #   |   page
        #   |
        #   |
        #   0-------x

        self.__pdf.drawString(
            50, 780, "Este es un informe acerca de los horarios y días más concurridos."
        )
        # finish page
        self.__pdf.showPage()

        self.guarda_pdf(self.__pdf)


# prueba InformeAdopcionesRescates
inicio = datetime(2023, 10, 12)
fin = datetime(2023, 11, 12)

informe = InformeAdopcionesRescates(inicio, fin)
informe.genera_pdf()

informe = InformeParticipacionEmpleados(inicio, fin)
informe.genera_pdf()

informe = InformeControlHorariosDias(inicio, fin)
informe.genera_pdf()

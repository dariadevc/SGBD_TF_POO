# from __future__ import annotations
import os
from datetime import date
from reportlab.pdfgen import canvas
from pdf import Pdf
from Modelo.Personas.adoptante_visitante import AdoptanteVistante
from Modelo.Animales.animal import Animal


class CertificadoAdopcion(Pdf):
    def __init__(
        self, adoptante: AdoptanteVistante, animal: Animal, fecha_adopcion: date
    ):
        self.__adoptante = adoptante
        self.__animal = animal
        self.__fecha_adopcion = fecha_adopcion
        self.__nombre_archivo = f"{self.__fecha_adopcion.strftime('%d %m %y')}-{self.__adoptante.get_apellido}_{self.__adoptante.get_nombre}-{self.__animal.get_codigo}_{self.__animal.get_nombre}"
        self.__pdf = self.inicializa_pdf()

    def inicializa_pdf(self):
        directorio = os.path.join(os.path.expanduser("~"), "Desktop/Adopciones/")

        if os.path.exists(directorio):
            nombre_path = str(directorio + self.__nombre_archivo + ".pdf")
            print(f"PDF {self.__nombre_archivo} generado.")
        else:
            os.mkdir(directorio)
            nombre_path = str(directorio + self.__nombre_archivo + ".pdf")
            print(f"Carpeta Informes y PDF {self.__nombre_archivo} generados.")

        # self.__pdf = canvas.Canvas(nombre_path, pagesize=(595.27, 841.89))  # A4 pagesize
        return canvas.Canvas(
            nombre_path, pagesize=(841.89, 595.27)
        )  # A4 pagesize horizontal

    def guarda_pdf(self, pdf):
        pdf.save()

    def genera_pdf(self):
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
        # finish page
        self.__pdf.showPage()

        self.guarda_pdf(self.__pdf)

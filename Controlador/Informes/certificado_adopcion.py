# from __future__ import annotations
import os
from datetime import date
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from pdf import Pdf
from Modelo.Personas.adoptante_visitante import AdoptanteVistante
from Modelo.Animales.animal import Animal
from Modelo.Personas.usuario_empleado import Usuario


class CertificadoAdopcion(Pdf):
    def __init__(
        self,
        adoptante: AdoptanteVistante,
        animal: Animal,
        fecha_adopcion: date,
        responsable: Usuario,
    ):
        self.__adoptante = adoptante
        self.__animal = animal
        self.__responsable = responsable
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
            nombre_path, pagesize=(595.27, 841.89)
        )  # A4 pagesize horizontal

    def guarda_pdf(self, pdf):
        pdf.save()

    def genera_pdf(self):
        ancho_logo = 100
        alto_logo = (float(A4[1]) - 50) * ancho_logo / (float(A4[0]) - 100)

        self.__pdf.drawImage(
            "Vista/Media/logo-bsf.png",
            (A4[0] - 100) / 2,
            A4[1] - 170,
            width=ancho_logo,
            height=alto_logo,
            preserveAspectRatio=True,
            mask="auto",
        )

        # Configuración de la fuente y tamaño
        self.__pdf.setFont("Helvetica-Bold", 20)
        # self.__pdf.setFillColorRGB(244, 130, 33)

        nombre_refugio = "Best Friends"
        self.__pdf.drawCentredString(A4[0] / 2, 680, nombre_refugio)

        # Fecha de adopción
        self.__pdf.setFont("Helvetica", 12)
        self.__pdf.drawRightString(
            A4[0] - 50, 665, f"{date.today.strftime('%d/%m/%y')}"
        )

        # Título
        self.__pdf.setFont("Helvetica-Bold", 16)
        titulo = "Certificado de Adopción"
        self.__pdf.drawCentredString(A4[0] / 2, 640, titulo)

        # Información del adoptante
        self.__pdf.setFont("Helvetica", 12)
        linea1 = f"El/La Sr./Sra. {self.__adoptante.get_nombre} {self.__adoptante.get_apellido}, identificado/a con DNI Nº {self.__adoptante.get_dni}, ha adoptado"
        linea2 = f"a la mascota con nombre {self.__animal.get_nombre} en el día {self.__fecha_adopcion.strftime('%d/%m/%y')}."
        linea3 = f"El/La Sr./Sra. {self.__adoptante.get_nombre} {self.__adoptante.get_apellido} se compromete a responsabilizarse por el bienestar"
        linea4 = f"de {self.__animal.get_nombre}, informando durante los próximos 4 meses acerca de su estado. "
        self.__pdf.drawString(50, 600, linea1)
        self.__pdf.drawString(50, 580, linea2)
        self.__pdf.drawString(50, 560, linea3)
        self.__pdf.drawString(50, 540, linea4)

        # Información del empleado
        linea5 = f"El/La responsable de la adopción es {self.__responsable.get_nombre} {self.__responsable.get_apellido}, indentificado/a con"
        linea6 = f"DNI Nº {self.__adoptante.get_dni}."
        linea7 = f"{self.__responsable.get_nombre} {self.__responsable.get_apellido} se compromete a contactar mensualmente a {self.__adoptante.get_nombre} {self.__adoptante.get_apellido} para"
        linea8 = f"verificar el estado de {self.__animal.get_nombre} durante el plazo estipulado. "
        self.__pdf.drawString(50, 500, linea5)
        self.__pdf.drawString(50, 480, linea6)
        self.__pdf.drawString(50, 460, linea7)
        self.__pdf.drawString(50, 440, linea8)

        # Termina la página
        self.__pdf.showPage()

        self.guarda_pdf(self.__pdf)

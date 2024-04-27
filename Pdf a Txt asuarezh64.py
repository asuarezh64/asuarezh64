# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yLPgsXqtcPqs-n6RaWq5BgTGYmLJF66y
"""
# Creado por asuarezh64 el 27 de abril de 2024
import os
import pdfplumber
from PyPDF2 import PdfReader

# Instalar las bibliotecas necesarias (PyPDF2 y pdfplumber)
!pip install PyPDF2
!pip install pdfplumber

# Función para leer el texto y los metadatos del PDF
def read_pdf(pdf_file_path):
    # Leer el texto utilizando pdfplumber
    with pdfplumber.open(pdf_file_path) as pdf:
        pdf_text = ""
        for page in pdf.pages:
            pdf_text += page.extract_text()

    # Leer los metadatos utilizando pdfplumber
    with pdfplumber.open(pdf_file_path) as pdf:
        pdf_metadata = pdf.metadata

    return pdf_text, pdf_metadata

# Ruta del archivo PDF que deseas leer (ajusta según tu caso)
pdf_file_path = '/content/TSC Abril 2024.pdf'

# Llamar a la función para leer el texto y los metadatos del PDF
pdf_text, pdf_metadata = read_pdf(pdf_file_path)

# Imprimir el texto del PDF
print("Texto del PDF:")
print(pdf_text)

# Imprimir los metadatos del PDF
print("\nMetadatos del PDF:")
print(pdf_metadata)

# Obtener el nombre y la carpeta del archivo PDF
pdf_folder, pdf_filename = os.path.split(pdf_file_path)

# Guardar todo el texto en un archivo .txt con el mismo nombre y ubicación que el archivo PDF
output_file_path = os.path.join(pdf_folder, pdf_filename.split('.')[0] + '.txt')
with open(output_file_path, 'w') as text_file:
    text_file.write(pdf_text)

print(f"\nEl texto ha sido guardado en: {output_file_path}")

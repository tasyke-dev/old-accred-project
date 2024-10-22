"""!!!Файл функции конвертации .docx в .pdf!!!"""

import os
import sys
import comtypes.client
import time

wdFormatPDF = 17

def convertDocxToPdf(inFile, outFile):

    # Создание COM oобъекта
    word = comtypes.client.CreateObject('Word.Application')
    
    time.sleep(3)

    #конвертация docx в pdf

    #открываем docx
    doc=word.Documents.Open(inFile) 
    # конвертация
    doc.SaveAs(outFile, FileFormat=wdFormatPDF) 
     # закрываем docx
    doc.Close()
    # закрываем ворд
    word.Quit() 
    return None
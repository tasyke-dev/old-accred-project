import os
import comtypes.client
import time


wdFormatPDF = 17


def convertDocxToPdf(inFile, outFile):
    #Вывод директорий
    print(inFile)
    print(outFile)


    # Создание COM oобъекта
    word = comtypes.client.CreateObject('Word.Application')
    
    word.Visible = True
    
    time.sleep(3)

    #конвертация docx в pdf
    doc=word.Documents.Open(inFile) #открываем docx
    doc.SaveAs(outFile, FileFormat=wdFormatPDF) # конвертация
    doc.Close() # закрываем docx
    word.Visible = False

    word.Quit() # закрываем ворд
    return None
in_file=str(input('Введите путь до файла: '))
out_file=str(input('Введить путь для сохранения файла: '))
convertDocxToPdf(in_file, out_file)
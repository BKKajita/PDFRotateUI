import os
import PySimpleGUI as sg
from PyPDF2 import PdfWriter, PdfReader

def pdfRotate_90(path, rotateFileName, filesDirectory):
    pdf = PdfReader(path)
    pdf_writer = PdfWriter()
    for i in range(len(pdf.pages)):
        page = pdf.getPage(i)
        pdf_writer.addPage(page)
        pdf_writer.pages[i].rotate(90)
    output_filename = '{}/{}.pdf'.format(filesDirectory, rotateFileName)
    with open(output_filename, 'wb') as file:
        pdf_writer.write(file)
    sg.popup("Rotação concluída!")

def pdfRotate_180(path, rotateFileName, filesDirectory):
    pdf = PdfReader(path)
    pdf_writer = PdfWriter()
    for i in range(len(pdf.pages)):
        page = pdf.getPage(i)
        pdf_writer.addPage(page)
        pdf_writer.pages[i].rotate(180)
    output_filename = '{}/{}.pdf'.format(filesDirectory, rotateFileName)
    with open(output_filename, 'wb') as file:
        pdf_writer.write(file)
    sg.popup("Rotação concluída!")

def pdfRotate_270(path, rotateFileName, filesDirectory):
    pdf = PdfReader(path)
    pdf_writer = PdfWriter()
    for i in range(len(pdf.pages)):
        page = pdf.getPage(i)
        pdf_writer.addPage(page)
        pdf_writer.pages[i].rotate(270)
    output_filename = '{}/{}.pdf'.format(filesDirectory, rotateFileName)
    with open(output_filename, 'wb') as file:
        pdf_writer.write(file)
    sg.popup("Rotação concluída!")

def mainWindow():
    menu_def = [["Informações",["Sobre","Ajuda","Histórico de versões"]]]
   
    layout = [
        [sg.MenubarCustom(menu_def, tearoff=False)],
        [sg.Text("Escolha uma das opções a seguir:")],
        [sg.Exit("Sair"), sg.Button("90º"), sg.Button("180º"), sg.Button("270º")],
    ]

    window = sg.Window("PDF Rotate", layout)

    while True:
        event, values = window.read()
        print(event, values)
        if event in (sg.WINDOW_CLOSED, "Sair"):
            break
        if event == "Sobre":
            window.disappear()
            sg.popup("PDF Rotate\nVersão 1.0.0\nDesenvolvido por Bruno K. Kajita")
            window.reappear()
        if event == "Ajuda":
            window.disappear()
            sg.popup("Escolhar um valor para rotacionar a página de PDF desejada")
            window.reappear()
        if event == "Histórico de versões":
            window.disappear()
            sg.popup("Versão 1.0.0 - Inicial")
            window.reappear()
        if event == "90º":
            pdfRotate_90(
                path = sg.popup_get_file("Selecione o arquivo:", file_types=(("Arquivos PDF","*.pdf"),)),
                rotateFileName = sg.popup_get_text("Informe o novo nome do arquivo:"),
                filesDirectory = sg.popup_get_folder("Selecione a pasta de destino:")
            )
        if event == "180º":
            pdfRotate_180(
                path = sg.popup_get_file("Selecione o arquivo:", file_types=(("Arquivos PDF","*.pdf"),)),
                rotateFileName = sg.popup_get_text("Informe o novo nome do arquivo:"),
                filesDirectory = sg.popup_get_folder("Selecione a pasta de destino:")
            )
        if event == "270º":
            pdfRotate_270(
                path = sg.popup_get_file("Selecione o arquivo:", file_types=(("Arquivos PDF","*.pdf"),)),
                rotateFileName = sg.popup_get_text("Informe o novo nome do arquivo:"),
                filesDirectory = sg.popup_get_folder("Selecione a pasta de destino:")
            )
           
    window.close()

if __name__ == "__main__":
    sg.theme('Topanga')
    mainWindow()

import win32com.client as win32

def excel_to_pdf(input_file, output_file):
    # Inicia una instancia de Excel
    excel = win32.Dispatch("Excel.Application")
    # Abre el archivo de Excel especificado
    wb = excel.Workbooks.Open(input_file)
    # Exporta el archivo a PDF (0 indica formato PDF)
    wb.ExportAsFixedFormat(0, output_file)
    # Cierra el archivo y la instancia de Excel
    wb.Close()
    excel.Quit()

# Llama a la función con la ruta de tu archivo de entrada y salida
excel_to_pdf("C:/Users/joaquin.astorga/mis_proyectos/format_change/App/doc.xlsx","C:/Users/joaquin.astorga/mis_proyectos/format_change/App/output/doc.pdf")
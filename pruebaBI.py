import win32com.client as win32

def update_data_source(file_path, excel_file):
    # Inicia una instancia de Power BI o la herramienta de BI que estés usando
    # Nota: el nombre "PowerBI.Application" es solo un ejemplo; reemplázalo según el objeto de aplicación específico.
    bi_app = win32.Dispatch("PowerBI.Application")
    
    # Abre el archivo de BI o selecciona el dashboard existente
    dashboard = bi_app.Dashboards.Open(file_path)
    
    # Busca la conexión de datos que quieres actualizar
    data_connection = dashboard.Connections("NombreConexionAnterior")
    
    # Actualiza la conexión para apuntar a un nuevo archivo de Excel
    data_connection.Connection = f"Provider=Microsoft.ACE.OLEDB.12.0;Data Source={excel_file};Extended Properties='Excel 12.0 Xml;HDR=YES';"
    
    # Refresca la conexión para que BI cargue los datos del nuevo archivo
    data_connection.Refresh()
    
    # Guarda el dashboard con la nueva fuente de datos
    dashboard.Save()
    
    print("Fuente de datos actualizada correctamente.")

# Llamar a la función con la ruta de tu dashboard y el nuevo archivo Excel
update_data_source("C:/Users/joaquin.astorga/mis_proyectos/format_change/App/input/dashboard.pbix", "C:/ruta/nuevo_archivo.xlsx")

import win32com.client

applications = ["Excel.Application", "Word.Application", "PowerPoint.Application", "Outlook.Application"]

for app in applications:
    try:
        instance = win32com.client.Dispatch(app)
        print(f"{app} se ha iniciado correctamente.")
        instance.Quit()  # Cierra la aplicación después de comprobar
    except Exception as e:
        print(f"No se pudo iniciar {app}: {e}")

import win32print
import win32ui

printer_name = win32print.GetDefaultPrinter()  # or specify the printer name
hprinter = win32print.OpenPrinter(printer_name)
pdc = win32ui.CreateDC()
pdc.CreatePrinterDC(printer_name)

# Example: Print a simple message
pdc.StartDoc("My Document")
pdc.StartPage()
pdc.TextOut(100, 100, "Hello, Printer!")
pdc.EndPage()
pdc.EndDoc()
pdc.DeleteDC()

import win32print
import win32ui

# Printer name (use the correct printer name if it's not the default)
printer_name = win32print.GetDefaultPrinter()  # or specify the printer name directly

# Open the printer
hprinter = win32print.OpenPrinter(printer_name)

# Start the print job
job_info = ("Drawer Open Command", None, "RAW")
win32print.StartDocPrinter(hprinter, 1, job_info)

# Start the page
win32print.StartPagePrinter(hprinter)

# ESC/POS command to open the cash drawer (ESC p m t1 t2)
drawer_open_command = b'\x1B\x70\x00\x19\xFA'  # Example command to open the drawer

# Write the command to the printer
win32print.WritePrinter(hprinter, drawer_open_command)

# End the page and the document
win32print.EndPagePrinter(hprinter)
win32print.EndDocPrinter(hprinter)

# Close the printer
win32print.ClosePrinter(hprinter)

print("Drawer open command sent to the printer.")

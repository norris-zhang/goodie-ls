import usb
from escpos.printer import Usb
import usb.core
import usb.backend.libusb1

dev = usb.core.find(find_all=True)

# Loop through the devices and check if the printer is connected
for device in dev:
    print(f"Device found: {device}")

backend = usb.backend.libusb1.get_backend()

# Now search for the printer
dev = usb.core.find(backend=backend, find_all=True)
if dev:
    for d in dev:
        print(d)

def find_printer():
    # Find all USB devices
    devices = usb.core.find(find_all=True)

    # Loop through the devices and check for the CITIZEN printer
    for dev in devices:
        # Print device details (Vendor ID and Product ID)
        print(f"Device: {dev}")
        if dev.product == "CT-S310II":  # Adjust this if needed
            print(f"Found CITIZEN printer: Vendor ID: {dev.idVendor}, Product ID: {dev.idProduct}")
            return dev.idVendor, dev.idProduct

# Call the function and print the Vendor ID and Product ID
vendor_id, product_id = find_printer()
print(f"Vendor ID: {vendor_id}, Product ID: {product_id}")

# Replace with the actual Vendor ID and Product ID
VENDOR_ID = 0x1234  # Example Vendor ID
PRODUCT_ID = 0x5678  # Example Product ID

try:
    # Connect to the printer using the Vendor ID and Product ID
    printer = Usb(VENDOR_ID, PRODUCT_ID)

    # Send ESC/POS command to open the cash drawer
    command = b'\x1B\x70\x00\x19\xFA'  # Example command for the drawer
    printer.device.write(1, command)

    print("Cash drawer open command sent successfully.")
except Exception as e:
    print(f"Failed to send command: {e}")

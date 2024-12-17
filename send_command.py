from escpos.printer import Usb

# Replace with the actual Vendor ID and Product ID
VENDOR_ID = 0x1D90  # Example Vendor ID
PRODUCT_ID = 0x2060  # Example Product ID

try:
    # Connect to the printer using the Vendor ID and Product ID
    printer = Usb(VENDOR_ID, PRODUCT_ID)

    # Send the DLE + EOT command to query printer status
    command = b'\x10\x04'  # DLE + EOT
    printer.device.write(1, command)

    print("DLE + EOT command sent successfully.")
except Exception as e:
    print(f"Failed to send command: {e}")

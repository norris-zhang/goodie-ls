from flask import Flask, jsonify
import serial

app = Flask(__name__)

# Define the serial port and baud rate for your printer (adjust as needed)
SERIAL_PORT = 'COM1'
BAUD_RATE = 9600  # Adjust this to match your printer's baud rate


@app.route('/print', methods=['POST'])
def print_text():
    # Send the command to open the cash drawer
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as printer:
            # ESC/POS command to open the cash drawer (e.g., ESC p m t1 t2)
            # Replace this command with the correct one for your printer
            command = b'\x1B\x70\x00\x19\xFA'  # Example ESC/POS command for drawer
            # or printer.write('hello printer!'.encode());
            printer.write(command)

        return jsonify({"message": "Print request and drawer open command sent"}), 200

    except Exception as e:
        return jsonify({"error": f"Failed to send command: {e}"}), 500


if __name__ == "__main__":
    app.run(port=5000)

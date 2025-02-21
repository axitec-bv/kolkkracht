from pymodbus.client import ModbusSerialClient  # Correct import for pymodbus >=3.x
import struct
import time

# Modbus RTU Configuration
MODBUS_PORT = "/dev/ttyUSB0"  # Adjust if necessary
BAUDRATE = 9600  # Default baud rate
PARITY = 'N'  # Default parity (None, Even, Odd)
STOPBITS = 1
BYTESIZE = 8
SLAVE_ID = 2  # Default Modbus ID

# Function to read a floating-point value from two registers
def read_float(client, address):
    try:
        response = client.read_input_registers(address, count=2, slave=SLAVE_ID)
        if response.isError():
            print(f"Error reading register {address}")
            return None

        # Combine registers into a single float (Big Endian)
        raw = struct.pack(">HH", response.registers[0], response.registers[1])
        value = struct.unpack(">f", raw)[0]
        return value
    except Exception as e:
        print(f"Exception: {e}")
        return None

# Create Modbus Serial Client (without method='rtu')
client = ModbusSerialClient(
    port=MODBUS_PORT,
    baudrate=BAUDRATE,
    parity=PARITY,
    stopbits=STOPBITS,
    bytesize=BYTESIZE,
    timeout=1
)

if client.connect():
    print("Connected to SDM230 Modbus meter")

    # Reading key electrical parameters
    voltage = read_float(client, 0x0000)   # Voltage (V)
    current = read_float(client, 0x0006)   # Current (A)
    power = read_float(client, 0x000C)     # Active Power (W)
    energy = read_float(client, 0x0156)    # Total Active Energy (kWh)

    # Display results
    print(f"Voltage: {voltage:.2f} V")
    print(f"Current: {current:.2f} A")
    print(f"Active Power: {power:.2f} W")
    print(f"Total Energy: {energy:.2f} kWh")

    client.close()
else:
    print("Failed to connect to SDM230 Modbus meter")
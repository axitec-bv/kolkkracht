# Kolkkracht

## Features
- Read voltage, current, power, and energy data from an **Eastron SDM230** meter via **Modbus RTU**.
- Measure **RPM** using a GPIO-connected sensor on a Raspberry Pi.
- Uses **pymodbus** for Modbus communication.
- Uses **lgpio** for GPIO handling on Raspberry Pi.

## Repository Structure
```
kolkkracht-main/
│── .gitattributes
│── .gitignore
│── README.md  # This file
│── src/
│   ├── eastronMeter/
│   │   ├── main.py  # Modbus RTU reader for SDM230
│   │   ├── requirements.txt  # Dependencies for SDM230 module
│   ├── rpm/
│   │   ├── main.py  # RPM measurement script
│   │   ├── requirements.txt  # Dependencies for RPM module
```

## Installation
### Prerequisites
Ensure you have **Python 3** installed. It is recommended to run this on a Raspberry Pi.

### Install Dependencies
For the **Eastron SDM230 Modbus** module:
```sh
pip install -r src/eastronMeter/requirements.txt
```

For the **RPM measurement** module:
```sh
pip install -r src/rpm/requirements.txt
```

## Usage
### Read Eastron SDM230 Modbus Meter
Run the Modbus meter script:
```sh
python src/eastronMeter/main.py
```
It will output values for **Voltage (V), Current (A), Active Power (W),** and **Total Energy (kWh).**

### Measure RPM
Run the RPM measurement script with an optional interval:
```sh
python src/rpm/main.py --interval 5
```
The **interval** (in seconds) defines how frequently RPM readings are displayed.

## Hardware Requirements
- **Eastron SDM230 Modbus Meter** connected via RS485-USB adapter.
- **RPM Sensor** connected to GPIO **BCM Pin 17**.

## Troubleshooting
- Ensure **pymodbus** and **pyserial** are installed for Modbus communication.
- For GPIO errors, ensure the script runs with proper permissions (use `sudo` if necessary).
- Verify the wiring and Modbus settings (port, baud rate, parity, stop bits).

## License
This project is open-source. Feel free to modify and contribute!

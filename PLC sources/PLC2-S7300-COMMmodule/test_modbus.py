import easymodbus.modbusClient
import time

ip = input("Enter the IP address of the PLC: ")

plc1 = easymodbus.modbusClient.ModbusClient(ip, 502)

while (True):
    try:
        plc1.connect()
        print("Successfully connected to PLC")
        break
    except:
        print("Error connecting to PLC, trying again...")
        time.sleep(1)
 
while (True):
    
    try:
        coils = plc1.read_coils(0, 1)
    except:
        print("Error reading coils on PLC ")
    
    try:
        request = coils[0]
        plc1.write_single_coil(2, request)

        plc1.read_coils(2, 1)
    except:
        print("Error writing coil on PLC ")
    time.sleep(1)

    

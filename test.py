# import minimalmodbus

# inst = minimalmodbus.Instrument('COM4', 1)  # port name, slave address (in decimal)
# print(inst)
# print(inst.read_registers(3000,1))

# import serial

# serialPort = serial.Serial(port="COM4")
# serialString = ""  # Used to hold data coming over UART
# while 1:
#     # Wait until there is data waiting in the serial buffer
#     # if serialPort.in_waiting > 0:

#         # Read data out of the buffer until a carraige return / new line is found
#         serialString = serialPort.readline()

#         # Print the contents of the serial data
#         try:
#             # print(serialString)
#             print(serialString.decode("Ascii"))
#         except:
#             pass

from pymodbus.client.sync import ModbusSerialClient

client = ModbusSerialClient(
    method='rtu',
    port='COM4',
    baudrate=115200,
    timeout=1,
    parity='N',
    stopbits=1,
    bytesize=8
)

if client.connect():  # Trying for connect to Modbus Server/Slave
    '''Reading from a holding register with the below content.'''
    res = client.read_holding_registers(address=0x9000, count=1, unit=1)
    print(res)

    '''Reading from a discrete register with the below content.'''
    res = client.read_discrete_inputs(address=0x9000, count=1, unit=1)


    if not res.isError():
        print(res.registers)
    else:
        print(res)

else:
    print('Cannot connect to the Modbus Server/Slave')
from datetime import datetime
from pprint import pprint
import serial

def decoding_dacian_electrodacus_data(compressed_data):
    payload = {}
    uncompressed_list_char = [ord(each_char)-35 for each_char in compressed_data]
    single_char_value = uncompressed_list_char[:6]
    double_char_value = uncompressed_list_char[6:7+21]
    triple_char_value = uncompressed_list_char[7+22:]
    double_list = [upper_d*91+lower_d for upper_d, lower_d in zip(double_char_value[::2], double_char_value[1::2])]
    triple_list = [upper_t*91**2+mid_t*91+lower_t for upper_t, mid_t, lower_t in zip(triple_char_value[::3], triple_char_value[1::3], triple_char_value[2::3])]
    payload["Sample Time"] = datetime(year=2000+single_char_value[0], month=single_char_value[1], day=single_char_value[2], hour=single_char_value[3], minute=single_char_value[4], second=single_char_value[5]).strftime("%c")
    payload["SOC"] = double_list[0]
    payload["Cell1"] = double_list[1]/1000
    payload["Cell2"] = double_list[2]/1000
    payload["Cell3"] = double_list[3]/1000
    payload["Cell4"] = double_list[4]/1000
    payload["Cell5"] = double_list[5]/1000
    payload["Cell6"] = double_list[6]/1000
    payload["Cell7"] = double_list[7]/1000
    payload["Cell8"] = double_list[8]/1000
    payload["Internal Temperature F"] = (double_list[9]-450)/10*9/5+32
    payload["Internal Temperature C"] = (double_list[9]-450)/10
    payload["External Temperature F"] = (double_list[10]-450)/10*9/5+32
    payload["External Temperature C"] = (double_list[10]-450)/10
    battery_value = triple_list[0]/1000
    payload["Current of Battery"] = battery_value if compressed_data[28] !="-" else -battery_value
    payload["Current of PV1"] = triple_list[1]/1000
    payload["Current of PV2"] = triple_list[2]/1000
    payload["Current of Load"] = triple_list[3]/1000
    payload["ADC2"] = triple_list[4]
    payload["ADC3"] = triple_list[5]
    payload["ADC4"] = triple_list[6]
    payload["Heat1"] = triple_list[7]
    payload["Heat2"] = triple_list[8]
    error_codes_tuple = list(filter(lambda each_dig:  int(each_dig[0])==1, zip(bin(triple_list[9]).replace("0b","")[::-1], "OV OVLK UV UVLK IOT COC DOC DSC CELF OPEN LVC ECCF CFET EOC DFET".split(' '))))
    error_codes = [error[1] for error in error_codes_tuple]    
    payload["Error"] =  error_codes
    payload["Voltage of Battery"] = sum(double_list[1:9])/1000
    payload["Voltage Cell Delta"] = (max(double_list[1:9]) - min(double_list[1:9]))/1000
    return payload

while True:
        ser = serial.Serial('/dev/ttyAMA0', 115200)
        data = ser.readline()
        compressed_string = data.decode('utf-8').strip()
        uncompressed_string = decoding_dacian_electrodacus_data(compressed_string)
        pprint(uncompressed_string)

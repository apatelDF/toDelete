from time import sleep
from smbus2 as smbus

class MLX90640():

    def __init__(self, address=0x33, bus_num=1):
        self.bus_num = bus_num
        self.address = address # Slave adress
        self.bus = smbus.SMBus(bus=bus_num)

    def read_reg(self, reg_addr):
        for i in range(self.comm_retries):
            try:
                return self.bus.read_word_data(self.address, reg_addr)
            except IOError as e:
                #"Rate limiting" - sleeping to prevent problems with sensor
                #when requesting data too quickly
                sleep(self.comm_sleep_amount)
        #By this time, we made a couple requests and the sensor didn't respond
        #(judging by the fact we haven't returned from this function yet)
        #So let's just re-raise the last IOError we got
        raise e

    def I2CRead(self, reg_addr, wordsToRead): #  wordsToRead is the number of 16 bit words to read
            for i in range(self.comm_retries):
                try:
                    raw = self.bus.read_i2c_block_data(self.adress, reg_addr, wordsToRead*2)
                except IOError as e:
                    if(i == self.comm_retries -1):
                        raise e
                    sleep(self.comm_sleep_amount)

            i2cData = [None] * wordsToReads
            index = 0
            for i in range(0, wordsToRead*2, 2):
                i2cData[index] = raw[i] + raw[i+1]
                index = index + 1



    def dumpEE():
        return  I2CRead(0x2400, 832)

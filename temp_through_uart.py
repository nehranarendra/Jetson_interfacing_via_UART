import smbus2
import time
import serial

# ADT7420 I2C addresses
ADT7420_ADDRS = [0x48, 0x49, 0x4A, 0x4B]

# ADT7420 registers
ADT7420_REG_CONFIG = 0x01
ADT7420_REG_TEMP_MSB = 0x00

def read_temp_celsius(addr):
    # Initialize I2C bus
    bus = smbus2.SMBus(1)

    # Read temperature data
    temp_data = bus.read_i2c_block_data(addr, ADT7420_REG_TEMP_MSB, 2)

    # Convert temperature data to temperature in degrees Celsius
    temp_celsius = ((temp_data[0] << 9) | temp_data[1]) / 256.0
    
    return temp_celsius

def main():
    try:
        # Open serial port for UART communication
        ser = serial.Serial('/dev/ttyTHS1', 9600, timeout=1)  # Update with your UART port
        
        # Check if the serial port is open
        if not ser.is_open:
            ser.open()

        while True:
            # Wait for a response
            response = ser.readline().decode('utf-8')
            # Read temperature data from all sensors
            temps = [read_temp_celsius(addr) for addr in ADT7420_ADDRS]
                
            if response:
                print(f"Received: {response}")
                
                print(temps)             
                # Send temperature data over UART
                # Concatenate temperature messages with commas
                message = ','.join(map(str, temps))
                ser.write(message.encode('utf-8'))
                print("Sent: messages")
                
            else:
                print("No response received.")
            
            # Wait for 1 second before reading again
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Exiting...")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()




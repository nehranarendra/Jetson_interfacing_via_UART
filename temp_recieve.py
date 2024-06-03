import serial
import time

def main():
    try:
        # Open serial port       
        ser = serial.Serial('/dev/ttyTHS0', 9600, timeout=1)  # Update with your UART port
        
        # Check if the serial port is open
        if not ser.is_open:
            ser.open()

        while True:
            # Message to be sent
            message = "hello rakhi"
            
            # Send message
            ser.write(message.encode('utf-8'))
            #ser.write(message.encode)
            print(f"Sent: {message}")
            
            # Wait for a response
            response = ser.readline().decode('utf-8')
            
            if response:
                print(f"Received: {response}")
            else:
                print("No response received.")
            
            # Delay before sending the next message
            time.sleep(1)
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

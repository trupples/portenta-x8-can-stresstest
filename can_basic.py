import can
import time
import sys

msg_id = int(sys.argv[1]) if len(sys.argv) == 2 else 123

with can.Bus(channel='can1', interface='socketcan') as bus:
    for i in range(1000):
        msg = can.Message(arbitration_id = msg_id, data = [i % 256], is_extended_id=False)

        try:
            bus.send(msg)
            print(f"Sent message with ID {hex(msg_id)} and content {hex(i%256)}")
        except can.CanError as e:
            print(f"ERROR {e}")

        time.sleep(0.1)


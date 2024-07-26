import pyfirmata
import time
from timeit import default_timer as timer
import pyfirmata.util


board = pyfirmata.Arduino("COM3")

it = pyfirmata.util.Iterator(board)
it.start()

# led = board.get_pin('d:13:o')
# seconds = 0
# while (seconds < 3):
#     start = timer()
#     led.write(True)
#     seconds+=1
#     time.sleep(1)
#     led.write(False)
#     time.sleep(1)
#     print(f"time passed: {seconds} seconds")
# end = timer()
# print(f"start: {start:.2f} | end: {end:.3f} | Duration: {end-start}")   

#pin 6 echo
#pin 7 trig
echo = board.get_pin('d:6:i')
trig = board.get_pin('d:7:o')

print(trig.read())
print(trig.write(True))
while True:
    time.sleep(0.5)
    trig.write(True)
    time.sleep(0.00001)
    trig.write(False)
    while echo.read() == False:
        print("first")
        start = timer()
        if echo.read() == True:
            print("last")
            end = timer()
            print(f"start: {start:.8f} | end: {end:.8f}")
            duration = end - start
            distance = (duration * 0.000343) /2
    print(f"Distance: {distance:.3f}")
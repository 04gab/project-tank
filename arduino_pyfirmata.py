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

print(echo.read()==False)
# print(trig.read())
# print(trig.write(True))
# while True:
#     #clear trig pin
#     trig.write(False)
#     board.pass_time(0.00002)

#     trig.write(True)
#     board.pass_time(0.00001)
#     trig.write(False)
#     limit_start = time.time()
#     echo.read(True)
#     while echo.read() == True:
#         if time.time() - limit_start > 1:
#             break
#         pass
#     start = timer()
#     while echo.read() == True:
#         pass

#     end = timer()
#     duration = end - start
#     distance = (duration * 34300) /2
#     print(f"start: {start:.8f} | end: {end:.8f} | Duration: {duration}")
#     print(f"Distance: {distance:.3f}")
   
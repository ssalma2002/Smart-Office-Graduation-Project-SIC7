from gpiozero import MotionSensor

pir = MotionSensor(17)

if __name__ == "__main__":
    pir.wait_for_motion()
    print("Motion detected!")
    pir.wait_for_no_motion()
    print("Motion ended!")
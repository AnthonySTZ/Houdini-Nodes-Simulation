import time
import threading

thread = False


def write() -> None:
    i = 0
    global thread
    while thread and i < 10:
        print(f"{i} seconds")
        time.sleep(1)
        i += 1


def simulate() -> None:
    print("Simulating the process...")
    global thread
    thread = True
    threading.Thread(target=write, daemon=True).start()


def stop_simulation() -> None:
    global thread
    thread = False
    print("Simulation stopped.")

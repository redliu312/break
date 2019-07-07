from pynput import mouse
from datetime import datetime
from threading import Thread
import time

max_static_time = 300

update_loc_time_stack = [(None, None)]


def on_move(x, y):
    now_loc = (x, y)
    update_loc_time_stack[0] = (now_loc, datetime.now())


def check_log():
    while True:

        loc, update_time = update_loc_time_stack[0]
        if loc is None:
            continue
        now = datetime.now()
        check_duration = (now - update_time).total_seconds()
        if check_duration > max_static_time:
            print("you did not move for a while, move cursor for you")
            mouse_control = mouse.Controller()
            mouse_control.move(-1, -1)
        else:
            print("you move the cursor {} secs ago".format(check_duration))
        time.sleep(1)


def main():
    checker = Thread(target=check_log, )
    checker.setDaemon(True)
    checker.start()
    with mouse.Listener(on_move=on_move) as listener:
        listener.join()


if __name__ == "__main__":
    main()

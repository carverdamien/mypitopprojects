import threading

# This function stores values from ITERABLE in a buffer.
# If it was not able to get a new value from iterable after DELAY seconds,
# it will flush the buffer and call ACTION on the bufferized values.
def delay_action_until_iterable_blocks(iterable, action, delay=5):
    buff = []
    def func():
        b = []
        while len(buff) > 0:
            b.append(buff.pop(0))
        if len(b) > 0:
            action(b)
    t = threading.Timer(delay,func)
    t.start()
    for i in iterable:
        buff.append(i)
        t.cancel()
        t = threading.Timer(delay,func)
        t.start()

# For testing
def iterableKeyboardInput():
    while True:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            yield ch
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

if __name__ == '__main__':
    import sys, tty, termios
    def buffprintter(buff):
        sys.stdout.write(''.join(buff))
        sys.stdout.flush()
    delay_action_until_iterable_blocks(iterableKeyboardInput(),buffprintter)

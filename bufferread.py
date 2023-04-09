import argparse
import sys

class TesteBuffer:
    def __init__(self, buffer=None):
        self.buffer = buffer

    def run(self):
        if self.buffer:
            print("Buffer was " + buffer)
            print(self.buffer.decode())
        else:
            print("no buffer")

if __name__ == '__main__':

    buffer = sys.stdin.read()

    tb = TesteBuffer(buffer.encode())
    tb.run()
#!/usr/bin/env python3

from argparse import ArgumentParser
import os

from pyarduino import Arduino

ARDUINO_WARNING = " You almost certainly do not want to change this, unless you've also updated the arduino code."

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--seconds", dest="seconds", metavar="S", type=int, default=60,
                        help="For how many seconds to capture data. -1 will capture until you ctrl-c out of it.")
    parser.add_argument("--filename", dest="filename", metavar="FILE", type=str, default="data.txt",
                        help="For how many seconds to capture data.")
    parser.add_argument("--baud", dest="baud", metavar="bps", type=int, default=1000000,
                        help="The baud rate for the serial connection." + ARDUINO_WARNING)
    parser.add_argument("--sumof", dest="sumof", metavar="#", type=int, default=6,
                        help="How many different sensor readings are getting added together into each value written to the serial stream." + ARDUINO_WARNING)

    return parser.parse_args()

def main():
    args = parse_args()
    stream_timeout = args.seconds
    data_file = args.filename
    baud = args.baud
    sumof = max(args.sumof, 1)
    temp_file = "{}.tmp".format(data_file)
    with arduino.Arduino.discover(baud=baud, timeout=0.1) as dev:
        dev.stream_to_file(filename=temp_file, stream_timeout=stream_timeout, batch_size=1000)
    with open(temp_file,"rb") as tf:
        with open(data_file, "wb") as df:
            # The first few bytes are usually gibberish due to starting mid-stream,
            # so ignore stuff until after the first newline, which should be
            # the start of a reading.
            while tf.read(1) != "\n".encode("utf-8"):
                pass
            df.write(tf.read().strip())
    os.remove(temp_file)
    with open(data_file, "r") as f:
        length = len(f.readlines())
    per_second = length/stream_timeout
    print("Data points per second: {}".format(per_second))
    if sumof > 1:
        print("Total readings per second: {}".format(per_second * sumof))
    print("Microsecond resolution (albeit smoothed): {}".format(1000000/(per_second * sumof)))

if __name__ == '__main__':
    main()

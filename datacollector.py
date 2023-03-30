#!/usr/bin/python

import csv
import datetime
import os
import sys

import plotter

if len(sys.argv) < 2:
    print("need to pass project csv file!")
    sys.exit(1)

FILENAME = f"{sys.argv[1]}"

duration = int(input("Session duration in seconds: "))
threshold = plotter.permin(int(input("Goal: ")), duration)
phase = input("Session phase: ")

timezone = datetime.datetime.utcnow().astimezone().tzinfo

if not os.path.exists(FILENAME):
    with open(FILENAME, "w") as f:
        w = csv.writer(f)
        w.writerow(["timestamp", "phase", "correct", "wrong", "threshold", "duration"])

while True:
    correct = int(input("Correct count: "))
    wrong = int(input("Wrong count: "))
    with open(FILENAME, "a") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                datetime.datetime.now(timezone).strftime("%Y-%m-%dT%H:%M:%S %Z"),
                phase,
                correct,
                wrong,
                threshold,
                duration,
            ]
        )
        print("Stored!\n")


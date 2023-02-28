#!/usr/bin/python

"""
Plots the out.csv as a SCC
"""


from datetime import datetime, date
from matplotlib import pyplot as plt
import numpy as np
import csv
import sys

DAILY = 0
WEEKLY = DAILY+1
MONTHLY = WEEKLY+1
YEARLY = MONTHLY+1

PERIOD = WEEKLY
GOAL = 70

def permin(count, duration):
    """Takes a count and a duration in seconds. Returns count per minute"""
    mins = duration/60
    return count / mins

def add_phase(ax, x, y, text, rotation=76):
    if x != 0:
        ax.axvline(x, color="grey", ls="--")

    ax.text(x, y, text, rotation=rotation, color="grey")


def get_date(stamp):
    tmp = datetime.strptime(stamp, "%Y-%m-%dT%H:%M:%S %Z")
    return tmp


LIMIT = get_date("2022-10-01T00:00:00 CET")

def main():

    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else: 
        filename = "out.csv"

    # read csv EXPECTS [timestamp, phase, correct, wrong, threshold, duration]
    rows = []
    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append(row)
    rows = rows[1:] # drop titles

    # only keep new dates
    rows = [
        row for row in rows
        if get_date(row[0]) >= LIMIT
    ]

    # TODO: generate list of phases (first new phase descriptor defines
    # timestamp for phase)

    # accumulate total per day --- can be altered to MAX or MIN for each day
#    correct_counts = {}
#    last = ""
#    print("counting correct")
#    for row in rows:
#        day = get_date(row[0]).isoformat()
#        if day != last:
#            last = day
#            correct_counts[last] = 0
#        correct_counts[last] += 1



    fig, ax = plt.subplots(1,1)
    ax.set_yscale("log")

    #add_celeration_angles(ax, length, min_value, max_value)

    # TODO: programmatically add phases
    phases = []
    last = ""
    for row in rows:
        if row[1] == last:
            continue

        last = row[1]
        add_phase(ax, get_date(row[0]), 2, row[1])
    

    # plot values


    print("plotting correct")
    xs = [get_date(row[0]) for row in rows]
    correct = [permin(float(row[2]), float(row[5])) for row in rows]
    wrong = [permin(float(row[3]), float(row[5])) for row in rows]
    threshold = [float(row[4]) for row in rows]
    duration = [float(row[5])/60 for row in rows] # duration in minutes
    ax.plot(xs, correct, "o", ms=3, color="blue", label="Correct")
    ax.plot(xs, wrong, "x", ms=3, color="red", label="Wrong")
    ax.plot(xs, threshold, ">", ms=3, color="green", label="Goal")
    ax.plot(xs, duration, "<", ms=3, color="black", label="Duration in minutes")

    
    ax.set_ylabel(f"Counts per minute")
    ax.set_xlabel("Time")

    plt.grid(True, which="both")
    plt.grid(which='major',axis ='y', linewidth='1', color='black')
    plt.grid(which='major',axis ='x', linewidth='1')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    ax.legend()



    # x-axis gridlines
    from matplotlib.dates import DayLocator, WeekdayLocator, MinuteLocator, HourLocator
    from matplotlib import dates
    #ax.minorticks_on()
    ax.xaxis.set_major_locator(DayLocator())
    #ax.xaxis.set_minor_locator(WeekdayLocator(byweekday=[dates.MO]))
    #ax.xaxis.set_minor_locator(MinuteLocator(byminute=[0,15,30,45]))
    ax.xaxis.set_minor_locator(HourLocator())

    ax.fmt_xdata = dates.DateFormatter("%Y-%m-%d %H:%M:%S")
    fig.autofmt_xdate()

    plt.show()








if __name__=="__main__":
    main()


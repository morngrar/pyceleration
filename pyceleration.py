#!/usr/bin/python3

from matplotlib import pyplot as plt
import numpy as np



def nanpad(li):
    tmp = [e for e in li]
    empty = 10 - len(tmp)
    for i in range(empty):
        tmp.append(np.nan)
    return tmp


def genx(f, n, start=1):
    y = [start]
    for i in range(n):
        tmp = y[-1]*f
        if tmp > start*10:
            break
        y.append(tmp)
    return y

def genBar(value):
    """Creates a session-long bar in the form of a series at value"""
    return [value for i in range(11)]

def displaceSeries(series, sessions):
    n = nanpad([])
    tmp = []
    for i in range(sessions):
        tmp += n
    
    return tmp + series

def example():
    fig, ax = plt.subplots(1,1)
    ax.set_yscale("log")
    ax.set_xlim(0, 140)


    x1_1 = displaceSeries(genx(1.1, 10, start=0.01), 11)
    x1_2 = displaceSeries(genx(1.2, 10, start=0.01), 12)
    x1_3 = displaceSeries(genx(1.3, 10, start=0.01), 13)
    x1_5 = displaceSeries(genx(1.5, 10, start=0.001), 11)
    x2 = displaceSeries(genx(2, 10, start=0.001), 12)
    x3 = displaceSeries(genx(3, 10, start=0.001), 13)

    ax.plot(x1_1, label="x1.1", lw=2.5)
    ax.plot(x1_2, label="x1.2", lw=2.5)
    ax.plot(x1_3, label="x1.3", lw=2.5)
    ax.plot(x1_5, label="x1.5", lw=2.5)
    ax.plot(x2, label="x2", lw=2.5)
    ax.plot(x3, label="x3", lw=2.5)
    ax.legend()


    correct = [1, 1.2, 2.3, 4.1, 5, 4.3, 9]
    wrong = list(reversed(correct))
    correct.insert(0, np.nan)
    wrong.insert(0, np.nan)
    tmp = nanpad(correct)
    c_data = np.asarray(tmp)
    w_data = np.asarray(nanpad(wrong))
    threshold = genBar(10)

    t2 = displaceSeries(threshold, 2)

    timing = genBar(0.5)

    ax.plot(c_data, "ok", ms=2)
    ax.plot(w_data, "rx")
    ax.plot(threshold, "b")
    ax.plot(timing, "g", ls="dashed")
    ax.plot(t2, "b")

    ax.axvline(10)
    ax.text(2,0.006, "Phase 1", rotation=76)
    ax.text(2+10,0.006, "Phase 2", rotation=76)

    #custom = [*n,np.nan, 3, 3.5, 4, 7, 3.2, 8, 6.5]
    #xs = np.arange(0,len(custom), step=1)
    #ax.plot(xs, custom)

    ax.set_yticks([0.001, 0.005, 0.01, 0.1, 0.5, 1, 5, 10, 50, 100, 500, 1000])
    ax.set_yticklabels([0.001, 0.005, 0.01, 0.1, 0.5, 1, 5, 10, 50, 100, 500, 1000])

    ax.set_xticks(np.arange(0, 150, step=10))
    ax.set_xticklabels(np.arange(0, 15, step=1))

    plt.grid()


    ratio = 100
    x_left, x_right = ax.get_xlim()
    y_low, y_high = ax.get_ylim()
    ax.set_aspect(abs((x_right-x_left)/(y_low-y_high))*ratio)

    plt.show()


if __name__=="__main__":
    example()

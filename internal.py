
from matplotlib import pyplot as plt
import numpy as np

def genx(f, n, start=1):
    y = [start]
    for i in range(n):
        tmp = y[-1]*f
        if tmp > start*10:
            break
        y.append(tmp)
    return y



def nanpad(li):
    tmp = [e for e in li]
    empty = 10 - len(tmp)
    for i in range(empty):
        tmp.append(np.nan)
    return tmp

def apply_scale_ratio(ax, scale):
    ratio = scale[-1]/10
    x_left, x_right = ax.get_xlim()
    y_low, y_high = ax.get_ylim()
    ax.set_aspect(abs((x_right-x_left)/(y_low-y_high))*ratio)


def apply_xrange(ax, length, divide_by_ten):
    step=10
    scale_length = length+step
    xrange = np.arange(0, scale_length, step=step)
    ax.set_xticks(xrange)
    labels = xrange
    if divide_by_ten:
        labels = np.arange(0, scale_length//step, step=1)
    else:
        labels = np.arange(0, scale_length, step=step)

    ax.set_xticklabels(labels)

def apply_log_range(ax, start, end):
    scale = generate_log_scale(start, end)
    ax.set_yticks(scale)
    ax.set_yticklabels(scale)
    return scale

def log_range(start, end):
    li = [start]
    while li[-1] < end:
        tmp = li[-1]*10
        if tmp >= 1:
            tmp = int(tmp)
        li.append(tmp)

    return li

def generate_log_scale(start, end):

    base_range = log_range(start, end)
    fivers = log_range(start*5, end)

    scale = [
        n
        for pair in zip(base_range, fivers)
        for n in pair
    ]
    scale = scale[:-1]

    return scale

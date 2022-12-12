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

def generate_bar(value, length=11):
    """Creates a session-long bar in the form of a series at value"""
    return [value for i in range(length)]

def displace_series(series, sessions):
    n = nanpad([])
    tmp = []
    for i in range(sessions):
        tmp += n
    
    return tmp + series

def _prepare_figure(length, min_value=0.001, max_value=1000, divide_by_ten=False):
    fig, ax = plt.subplots(1,1)
    ax.set_yscale("log")
    ax.set_xlim(0, length)

    return ax

def example():
    length = 140
    min_value = 0.001
    max_value = 1000
    divide_by_ten=False

    ax = _prepare_figure(length)


    _add_celeration_angles(ax, length, min_value=min_value, max_value=max_value)


    correct = [1, 1.2, 2.3, 4.1, 5, 4.3, 9]
    wrong = list(reversed(correct))
    correct.insert(0, np.nan)
    wrong.insert(0, np.nan)
    tmp = nanpad(correct)
    c_data = np.asarray(tmp)
    w_data = np.asarray(nanpad(wrong))
    threshold = generate_bar(10)

    t2 = displace_series(threshold, 2)

    timing = generate_bar(0.5)

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

    _apply_scaling(ax, length, min_value=min_value, max_value=max_value, divide_by_ten=divide_by_ten)

    plt.show()


def _add_celeration_angles(ax, chart_length, min_value=0.001, max_value=1000):

    upper_y = max_value/100 
    lower_y = min_value

    color = "#c4c4c4"
    
    start_session = chart_length//10-3

    def calc_text_x(offset):
        return 0.5+(start_session+offset)*10

    upper_text_y = upper_y*10 + upper_y

    ax.text(calc_text_x(1),upper_text_y, "x1.1", color=color)
    x1_1 = displace_series(genx(1.1, 10, start=upper_y), start_session+1)
    ax.text(calc_text_x(2),upper_text_y, "x1.2", color=color)
    x1_2 = displace_series(genx(1.2, 10, start=upper_y), start_session+2)
    ax.text(calc_text_x(3),upper_text_y, "x1.3", color=color)
    x1_3 = displace_series(genx(1.3, 10, start=upper_y), start_session+3)

    lower_text_y = lower_y *10 +lower_y

    x1_5 = displace_series(genx(1.5, 10, start=lower_y), start_session+1)
    ax.text(calc_text_x(1),lower_text_y, "x1.5", color=color)
    x2 = displace_series(genx(2, 10, start=lower_y), start_session+2)
    ax.text(calc_text_x(2)+1,lower_text_y, "x2", color=color)
    x3 = displace_series(genx(3, 10, start=lower_y), start_session+3)
    ax.text(calc_text_x(3)+1,lower_text_y, "x3", color=color)

    ax.plot(x1_1, label="x1.1", lw=2.5, color=color)
    ax.plot(x1_2, label="x1.2", lw=2.5, color=color)
    ax.plot(x1_3, label="x1.3", lw=2.5, color=color)
    ax.plot(x1_5, label="x1.5", lw=2.5, color=color)
    ax.plot(x2, label="x2", lw=2.5, color=color)
    ax.plot(x3, label="x3", lw=2.5, color=color)

def _apply_scaling(ax, length, min_value=0.001, max_value=1000, divide_by_ten=False):
    scale_length = length+10
    scale = _apply_log_range(ax, min_value, max_value)
    _apply_xrange(ax, scale_length, divide_by_ten=divide_by_ten)
    plt.grid()
    _apply_scale_ratio(ax, scale)

def _apply_scale_ratio(ax, scale):
    ratio = scale[-1]/10
    x_left, x_right = ax.get_xlim()
    y_low, y_high = ax.get_ylim()
    ax.set_aspect(abs((x_right-x_left)/(y_low-y_high))*ratio)

def _apply_xrange(ax, length, step=10, divide_by_ten=True):
    scale_length = length+10
    xrange = np.arange(0, scale_length, step=step)
    ax.set_xticks(xrange)
    labels = xrange
    if divide_by_ten:
        labels = np.arange(0, scale_length//10, step=1)
    else:
        labels = np.arange(0, scale_length, step=10)

    ax.set_xticklabels(labels)

def _apply_log_range(ax, start, end):
    scale = _generate_log_scale(start, end)
    ax.set_yticks(scale)
    ax.set_yticklabels(scale)
    return scale

def _log_range(start, end):
    li = [start]
    while li[-1] < end:
        tmp = li[-1]*10
        if tmp >= 1:
            tmp = int(tmp)
        li.append(tmp)

    return li

def _generate_log_scale(start, end):

    base_range = _log_range(start, end)
    fivers = _log_range(start*5, end)

    scale = [
        n
        for pair in zip(base_range, fivers)
        for n in pair
    ]
    scale = scale[:-1]

    return scale

if __name__=="__main__":
    example()

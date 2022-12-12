#!/usr/bin/python3


from matplotlib import pyplot as plt
import numpy as np

import internal


def displace_series(series, sessions):
    n = internal.nanpad([])
    tmp = []
    for i in range(sessions):
        tmp += n
    
    return tmp + series

def prepare_figure(
        length, 
        min_value=0.001, 
        max_value=1000, 
        divide_by_ten=False
):
    fig, ax = plt.subplots(1,1)
    ax.set_yscale("log")
    ax.set_xlim(0, length)

    return ax

def add_phase(ax, x, y, text, rotation=76):
    if x != 0:
        ax.axvline(x, color="black", ls="--")

    ax.text(2+x, y, text, rotation=rotation)

def plot_correct(ax, data, offset=0):
    tmp = [np.nan for i in range(offset+1)]
    tmp += data
    ax.plot(tmp, "ok", ms=2)

def plot_wrong(ax, data, offset=0):
    tmp = [np.nan for i in range(offset+1)]
    tmp += data
    ax.plot(tmp, "rx")

def plot_threshold(ax, value, length=10, offset=0):
    data = [value for i in range(length)]
    tmp = [np.nan for i in range(offset+1)]
    tmp += data
    ax.plot(tmp, "b")

def plot_timing(ax, value, length=10, offset=0):
    data = [value for i in range(length)]
    tmp = [np.nan for i in range(offset+1)]
    tmp += data
    ax.plot(tmp, "g", ls="dashed")

def example():
    length = 140
    min_value = 0.001
    max_value = 1000
    divide_by_ten=False

    ax = prepare_figure(length)
    add_celeration_angles(ax, length, min_value, max_value)


    correct = [1, 1.2, 2.3, 4.1, 5, 4.3, 9]
    wrong = list(reversed(correct))


    plot_correct(ax, correct)
    plot_wrong(ax, wrong)
    plot_threshold(ax,10)
    plot_timing(ax, 0.5)

    plot_threshold(ax, 10, offset=2*10)

    plot_correct(ax, correct, 2*10)

    add_phase(ax, 0, 0.006, "Phase 1")
    add_phase(ax, 10, 0.006, "Phase 2")


    apply_scaling(ax, length, min_value, max_value, divide_by_ten)

    plt.show()


def add_celeration_angles(ax, chart_length, min_value, max_value):

    upper_y = max_value/100 
    lower_y = min_value

    color = "#c4c4c4"
    
    start_session = chart_length//10-3

    def calc_text_x(offset):
        return 0.5+(start_session+offset)*10

    upper_text_y = upper_y*10 + upper_y

    ax.text(
        calc_text_x(1), 
        upper_text_y, 
        "x1.1", 
        color=color
    )
    x1_1 = displace_series(
        internal.genx(1.1, 10, start=upper_y), 
        start_session+1
    )
    ax.text(calc_text_x(2), upper_text_y, "x1.2", color=color)
    x1_2 = displace_series(
        internal.genx(1.2, 10, start=upper_y), 
        start_session+2
    )
    ax.text(calc_text_x(3),upper_text_y, "x1.3", color=color)
    x1_3 = displace_series(
        internal.genx(1.3, 10, start=upper_y), 
        start_session+3
    )

    lower_text_y = lower_y *10 +lower_y

    x1_5 = displace_series(
        internal.genx(1.5, 10, start=lower_y), 
        start_session+1
    )
    ax.text(calc_text_x(1), lower_text_y, "x1.5", color=color)
    x2 = displace_series(
        internal.genx(2, 10, start=lower_y), 
        start_session+2
    )
    ax.text(calc_text_x(2)+1, lower_text_y, "x2", color=color)
    x3 = displace_series(
        internal.genx(3, 10, start=lower_y), 
        start_session+3
    )
    ax.text(calc_text_x(3)+1, lower_text_y, "x3", color=color)

    ax.plot(x1_1, label="x1.1", lw=2.5, color=color)
    ax.plot(x1_2, label="x1.2", lw=2.5, color=color)
    ax.plot(x1_3, label="x1.3", lw=2.5, color=color)
    ax.plot(x1_5, label="x1.5", lw=2.5, color=color)
    ax.plot(x2, label="x2", lw=2.5, color=color)
    ax.plot(x3, label="x3", lw=2.5, color=color)

def apply_scaling(ax, length, min_value, max_value, divide_by_ten):
    scale_length = length+10
    scale = internal.apply_log_range(ax, min_value, max_value)
    internal.apply_xrange(ax, scale_length, divide_by_ten=divide_by_ten)
    plt.grid()
    internal.apply_scale_ratio(ax, scale)



if __name__=="__main__":
    example()

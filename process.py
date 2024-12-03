import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import logging

from functions import pend, fx1, fx2, fx3, fx4, fx5, fx6, fx7, fx8, fx9, fx10, fx11, fx12, fx
from radar_diagram import RadarDiagram
from utils import lines

data_sol = []
logger = logging.getLogger('uvicorn.error')


def fill_diagrams(data, initial_equations, restrictions):
    radar1 = RadarDiagram()
    radar1.draw('./static/images/diagram.png', initial_equations, u_list,
                "Характеристики системы в начальный момент времени", restrictions)
    radar1.draw('./static/images/diagram2.png', data[int(len(data) / 4)], u_list,
                "Характеристики системы в 1 четверти", restrictions)
    radar1.draw('./static/images/diagram3.png', data[int(len(data) / 2)], u_list,
                "Характеристики системы во 2 четверти", restrictions)
    radar1.draw('./static/images/diagram4.png', data[int(len(data) / 4 * 3)], u_list,
                "Характеристики системы в 3 четверти", restrictions)
    radar1.draw('./static/images/diagram5.png', data[-1, :], u_list,
                "Характеристики системы в последний момент времени", restrictions)


def create_graphic(t, data, faks):
    # fig, axs = plt.subplots(figsize=(20, 12))
    # plt.subplot(111)
    # for i in range(12):
    #     plt.plot(t, data[:, i], color=lines[i][0], linestyle=lines[i][1], label=u_list[i])
    # plt.xlabel("t")
    # plt.xlim([0, 1])
    # plt.legend(loc='lower right', bbox_to_anchor=(1, 1), labelspacing=0.1, fontsize='small')
    first_graphic(t, faks)
    draw_third_graphic(t)
    # plt.tight_layout()
    # fig.savefig('./static/images/figure.png', bbox_inches='tight')


def first_graphic(t, faks):
    fig, axs = plt.subplots(figsize=(15, 10))
    plt.subplot(1, 1, 1)
    x1 = []
    x2 = []
    x3 = []
    x4 = []
    x5 = []
    x6 = []
    x7 = []
    x8 = []
    x9 = []
    for i in t:
        x1.append(fx(i, faks[0]))
        x2.append(fx(i, faks[1]))
        x3.append(fx(i, faks[2]))
        x4.append(fx(i, faks[3]))
        x5.append(fx(i, faks[4]))
        x6.append(fx(i, faks[5]))
        x7.append(fx(i, faks[6]))
        x8.append(fx(i, faks[7]))
        x9.append(fx(i, faks[8]))

    plt.plot(t, x1, label='S')
    plt.plot(t, x2, label='F')
    plt.plot(t, x3, label='G')
    plt.plot(t, x4, label='T')
    plt.plot(t, x5, label='A')
    plt.plot(t, x6, label='D')
    plt.plot(t, x7, label='I')
    plt.plot(t, x8, label='P')
    plt.plot(t, x9, label='C')
    plt.legend(loc='best')
    plt.xlabel('t')
    fig.savefig("./static/images/figure.png")


def draw_third_graphic(t):
    fig, axs = plt.subplots(figsize=(15, 10))
    plt.subplot(1, 1, 1)
    x1 = []
    x2 = []
    x3 = []
    x4 = []
    x5 = []
    x6 = []
    x7 = []
    x8 = []
    x9 = []
    x10 = []
    x11 = []
    x12 = []
    for i in t:
        x1.append(fx1(i))
        x2.append(fx2(i))
        x3.append(fx3(i))
        x4.append(fx4(i))
        x5.append(fx5(i))
        x6.append(fx6(i))
        x7.append(fx7(i))
        x8.append(fx8(i))
        x9.append(fx9(i))
        x10.append(fx10(i))
        x11.append(fx11(i))
        x12.append(fx12(i))

    plt.plot(t, x1, label='X1')
    plt.plot(t, x2, label='X2')
    plt.plot(t, x3, label='X3')
    plt.plot(t, x4, label='X4')
    plt.plot(t, x5, label='X5')
    plt.plot(t, x6, label='X6')
    plt.plot(t, x7, label='X7')
    plt.plot(t, x8, label='X8')
    plt.plot(t, x9, label='X9')
    plt.plot(t, x10, label='X10')
    plt.plot(t, x11, label='X11')
    plt.plot(t, x12, label='X12')
    plt.legend(loc='best')
    plt.xlabel('t')
    fig.savefig("./static/images/figure2.png")


def cast_to_float(initial_equations, faks, restrictions):
    for i in range(len(initial_equations)):
        initial_equations[i] = float(initial_equations[i])

    for i in range(len(faks)):
        for j in range(len(faks[i])):
            faks[i][j] = float(faks[i][j])

    for i in range(len(restrictions)):
        restrictions[i] = float(restrictions[i])

    return initial_equations, faks, restrictions


def process(initial_equations, faks, restrictions):
    global data_sol

    cast_to_float(initial_equations, faks, restrictions)
    t = np.linspace(0, 1)
    data_sol = odeint(pend, initial_equations, t, args=(faks, restrictions))
    create_graphic(t, data_sol, faks)
    fill_diagrams(data_sol, initial_equations, restrictions)


u_list = [
    "Численность группировки сил, участвующих в аварийно-спасательных работах",
    "Количество жилых домов, разрушенных и поврежденных в результате наводнения",
    "Численность населения, эвакуированного из зоны затопления",
    "Количество погибших",
    "Протяженность железных и автомобильных дорог, оказавшихся в зоне затопления",
    "Количество промышленных предприятий в зоне наводнения",
    "Количество транспортных средств, участвующих в аварийно-спасательных работах",
    "Численность населения в зоне затопления",
    "Площадь сельскохозяйственных угодий, охваченных наводнением",
    "Количество погибших сельскохозяйственных животных",
    "Ущерб основным производственным фондам в зоне затопления",
    "Ущерб оборотным производственным фондам в зоне затопления"
]

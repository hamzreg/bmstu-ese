import matplotlib.pyplot as plt
from cocomo import (
    Driver,
    DRIVERS,
    DRIVERS_INDEXES,
    evaluate_project
)

def plot_employees_bar(employees: list):
    x = [i for i in range(1, 6)]
    bars = plt.bar(x, employees)
    ax = plt.gca()

    for i, patch in enumerate(ax.patches):
        ax.text(patch.get_x() + patch.get_width()/2.,
                1.0025 * employees[i],
                '{}'.format(int(employees[i])),
                ha='center', va='bottom')

    plt.xlabel('Стадии жизненного цикла')
    plt.ylabel('Число сотрудников')
    plt.show()


def task1(mode_index: int, kloc: float):
    drivers = [Driver.nominal for _ in range(len(DRIVERS))]

    results = {
        'MODP': {'work': [], 'time': []},
        'TOOL': {'work': [], 'time': []},
        'ACAP': {'work': [], 'time': []},
        'PCAP': {'work': [], 'time': []},
    }

    for modp in DRIVERS['MODP']:
        drivers[DRIVERS_INDEXES['MODP']] = modp

        work, time = evaluate_project(mode_index, drivers, kloc)

        results['MODP']['work'].append(work)
        results['MODP']['time'].append(time)

    drivers[DRIVERS_INDEXES['MODP']] = Driver.nominal

    for tool in DRIVERS['TOOL']:
        drivers[DRIVERS_INDEXES['TOOL']] = tool

        work, time = evaluate_project(mode_index, drivers, kloc)

        results['TOOL']['work'].append(work)
        results['TOOL']['time'].append(time)

    drivers[DRIVERS_INDEXES['TOOL']] = Driver.nominal

    for acap in DRIVERS['ACAP']:
        drivers[DRIVERS_INDEXES['ACAP']] = acap

        work, time = evaluate_project(mode_index, drivers, kloc)

        results['ACAP']['work'].append(work)
        results['ACAP']['time'].append(time)

    drivers[DRIVERS_INDEXES['ACAP']] = Driver.nominal

    for pcap in DRIVERS['PCAP']:
        drivers[DRIVERS_INDEXES['PCAP']] = pcap

        work, time = evaluate_project(mode_index, drivers, kloc)

        results['PCAP']['work'].append(work)
        results['PCAP']['time'].append(time)

    drivers[DRIVERS_INDEXES['PCAP']] = Driver.nominal

    __plot_task1(results)

def __plot_task1(results):
    x = ['Очень низкий', 'Низкий', 'Номинальный',
         'Высокий', 'Очень высокий']

    plt.figure(figsize=(24, 8))
    plt.suptitle('Зависимость трудозатрат и времени разработки от атрибутов персонала и проекта')
    
    plt.subplot(121)
    plt.plot(x, results['MODP']['work'], label='MODP')
    plt.plot(x, results['TOOL']['work'], label='TOOL')
    plt.plot(x, results['ACAP']['work'], label='ACAP')
    plt.plot(x, results['PCAP']['work'], label='PCAP')
    plt.ylabel('Трудозатраты')
    plt.xlabel('Значение драйвера')
    plt.legend()
    plt.grid(True)

    plt.subplot(122)
    plt.plot(x, results['MODP']['time'], label='MODP')
    plt.plot(x, results['TOOL']['time'], label='TOOL')
    plt.plot(x, results['ACAP']['time'], label='ACAP')
    plt.plot(x, results['PCAP']['time'], label='PCAP')
    plt.ylabel('Время разработки')
    plt.xlabel('Значение драйвера')
    plt.legend()
    plt.grid(True)
    plt.show()

def task2(mode_index: int, kloc: float):
    drivers = [1 for _ in range(len(DRIVERS))]
    drivers[DRIVERS_INDEXES['MODP']] = Driver.high_modp
    drivers[DRIVERS_INDEXES['TOOL']] = Driver.high_tool

    results = {
        'CPLX': {'work': [], 'time': []},
        'SCED': {'work': [], 'time': []},
    }

    for cplx in DRIVERS['CPLX']:
        drivers[DRIVERS_INDEXES['CPLX']] = cplx

        work, time = evaluate_project(mode_index, drivers, kloc)

        results['CPLX']['work'].append(work)
        results['CPLX']['time'].append(time)

    drivers[DRIVERS_INDEXES['CPLX']] = 1

    for sced in DRIVERS['SCED']:
        drivers[DRIVERS_INDEXES['SCED']] = sced

        work, time = evaluate_project(mode_index, drivers, kloc)

        results['SCED']['work'].append(work)
        results['SCED']['time'].append(time)

    drivers[DRIVERS_INDEXES['SCED']] = 1

    __plot_task2(results)

def __plot_task2(results):
    x = ['Очень низкий', 'Низкий', 'Номинальный',
         'Высокий', 'Очень высокий']

    plt.figure(figsize=(24, 8))
    plt.suptitle('Зависимость трудозатрат и времени от сложности продукта и требуемых сроков разработки'
                 ' при высоких MODP и TOOL')
    
    plt.subplot(121)
    plt.plot(x, results['CPLX']['work'], label='CPLX')
    plt.plot(x, results['SCED']['work'], label='SCED')
    plt.ylabel('Трудозатраты')
    plt.xlabel('Значение драйвера')
    plt.legend()
    plt.grid(True)

    plt.subplot(122)
    plt.plot(x, results['CPLX']['time'], label='CPLX')
    plt.plot(x, results['SCED']['time'], label='SCED')
    plt.ylabel('Время разработки')
    plt.xlabel('Значение драйвера')
    plt.legend()
    plt.grid(True)
    plt.show()
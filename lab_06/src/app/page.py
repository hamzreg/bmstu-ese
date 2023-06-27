from PyQt6.QtWidgets import (
    QWidget,
    QComboBox,
    QLineEdit,
    QFormLayout,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox
)
from dataclasses import dataclass
import matplotlib.pyplot as plt

from cocomo import (
    DRIVERS,
    DRIVERS_INDEXES,
    evaluate_project,
    get_life_cycle,
    get_wbs
)
from charts import (
    plot_employees_bar,
    task1,
    task2
)

@dataclass
class Settings:
    driver_width = 150

    evaluate_button_width = 200
    evaluate_button_text = 'Оценить параметры проекта'
    explore_button_width = 150
    explore_button_text = 'Исследовать влияние'

    life_cycle_table_width = 958
    life_cycle_table_height = 230
    life_cycle_item_width = 130
    wbs_table_width = 772
    wbs_table_height = 290
    wbs_item_width = 150

    error_title = 'Ошибка ввода'


class Page(QWidget):
    def __init__(self):
        super().__init__()

        self.mode = QComboBox()
        self.mode.addItems(['Обычный', 'Промежуточный', 'Встроенный'])
        self.mode.setCurrentIndex(1)
        self.mode.setFixedWidth(Settings.driver_width)

        self.kloc = QLineEdit()
        self.kloc.setFixedWidth(Settings.driver_width)
        self.kloc.setText('55')

        self.salary = QLineEdit()
        self.salary.setFixedWidth(Settings.driver_width)


        self.rely = QComboBox()
        self.rely.addItems(['Очень низкий', 'Низкий', 'Номинальный',
                            'Высокий', 'Очень высокий'])
        self.rely.setCurrentIndex(2)
        self.rely.setFixedWidth(Settings.driver_width)

        self.data = QComboBox()
        self.data.addItems(['Низкий', 'Номинальный',
                            'Высокий', 'Очень высокий'])
        self.data.setCurrentIndex(2)
        self.data.setFixedWidth(Settings.driver_width)

        self.cplx = QComboBox()
        self.cplx.addItems(['Очень низкий', 'Низкий', 'Номинальный',
                            'Высокий', 'Очень высокий'])
        self.cplx.setCurrentIndex(2)
        self.cplx.setFixedWidth(Settings.driver_width)
        

        self.time = QComboBox()
        self.time.addItems(['Номинальный', 'Высокий', 'Очень высокий'])
        self.time.setCurrentIndex(0)
        self.time.setFixedWidth(Settings.driver_width)

        self.stor = QComboBox()
        self.stor.addItems(['Номинальный', 'Высокий', 'Очень высокий'])
        self.stor.setCurrentIndex(0)
        self.stor.setFixedWidth(Settings.driver_width)

        self.virt = QComboBox()
        self.virt.addItems(['Низкий', 'Номинальный',
                            'Высокий', 'Очень высокий'])
        self.virt.setCurrentIndex(1)
        self.virt.setFixedWidth(Settings.driver_width)

        self.turn = QComboBox()
        self.turn.addItems(['Низкий', 'Номинальный',
                            'Высокий', 'Очень высокий'])
        self.turn.setCurrentIndex(1)
        self.turn.setFixedWidth(Settings.driver_width)


        self.acap = QComboBox()
        self.acap.addItems(['Очень низкий', 'Низкий', 'Номинальный',
                            'Высокий', 'Очень высокий'])
        self.acap.setCurrentIndex(3)
        self.acap.setFixedWidth(Settings.driver_width)

        self.aexp = QComboBox()
        self.aexp.addItems(['Очень низкий', 'Низкий', 'Номинальный',
                            'Высокий', 'Очень высокий'])
        self.aexp.setCurrentIndex(2)
        self.aexp.setFixedWidth(Settings.driver_width)

        self.pcap = QComboBox()
        self.pcap.addItems(['Очень низкий', 'Низкий', 'Номинальный',
                            'Высокий', 'Очень высокий'])
        self.pcap.setCurrentIndex(2)
        self.pcap.setFixedWidth(Settings.driver_width)

        self.vexp = QComboBox()
        self.vexp.addItems(['Очень низкий', 'Низкий', 
                            'Номинальный', 'Высокий'])
        self.vexp.setCurrentIndex(2)
        self.vexp.setFixedWidth(Settings.driver_width)

        self.lexp = QComboBox()
        self.lexp.addItems(['Очень низкий', 'Низкий', 
                            'Номинальный', 'Высокий'])
        self.lexp.setCurrentIndex(2)
        self.lexp.setFixedWidth(Settings.driver_width)


        self.modp = QComboBox()
        self.modp.addItems(['Очень низкий', 'Низкий', 'Номинальный',
                            'Высокий', 'Очень высокий'])
        self.modp.setCurrentIndex(2)
        self.modp.setFixedWidth(Settings.driver_width)

        self.tool = QComboBox()
        self.tool.addItems(['Очень низкий', 'Низкий', 'Номинальный',
                            'Высокий', 'Очень высокий'])
        self.tool.setCurrentIndex(2)
        self.tool.setFixedWidth(Settings.driver_width)

        self.sced = QComboBox()
        self.sced.addItems(['Очень низкий', 'Низкий', 'Номинальный',
                            'Высокий', 'Очень высокий'])
        self.sced.setCurrentIndex(2)
        self.sced.setFixedWidth(Settings.driver_width)

        drivers = QFormLayout()
        drivers.addRow('Режим проекта', self.mode)
        drivers.addRow('KLOC', self.kloc)
        drivers.addRow('Средняя заработная плата (тыс. рублей)', self.salary)

        drivers.addRow('Требуемая надежность RELY', self.rely)
        drivers.addRow('Размер базы данных DATA', self.data)
        drivers.addRow('Сложность продукта CPLX', self.cplx)

        drivers.addRow('Ограничение времени выполнения TIME', self.time)
        drivers.addRow('Ограничение объема основной памяти STOR', self.stor)
        drivers.addRow('Изменчивость виртуальной машины VIRT', self.virt)
        drivers.addRow('Время реакции компьютера TURN', self.turn)

        drivers.addRow('Способности аналитика ACAP', self.acap)
        drivers.addRow('Знание приложений AEXP', self.aexp)
        drivers.addRow('Способности программиста PCAP', self.pcap)
        drivers.addRow('Знание виртуальной машины VEXP', self.vexp)
        drivers.addRow('Знание языка программирования LEXP', self.lexp)

        drivers.addRow('Использование современных методов MODP', self.modp)
        drivers.addRow('Использование программных инструментов TOOL', self.tool)
        drivers.addRow('Требуемые сроки разработки SCED', self.sced)


        evaluate_button = QPushButton('Оценить параметры проекта')
        evaluate_button.setFixedWidth(Settings.evaluate_button_width)
        evaluate_button.clicked.connect(self.__evaluate_project)

        explore_button = QPushButton('Исследовать влияние')
        explore_button.setFixedWidth(Settings.explore_button_width)
        explore_button.clicked.connect(self.__explore_influence)

        buttons = QHBoxLayout()
        buttons.addWidget(evaluate_button)
        buttons.addWidget(explore_button)

        parameters = QVBoxLayout()
        parameters.addLayout(drivers)
        parameters.addLayout(buttons)

        self.__create_tables()

        tables = QVBoxLayout()
        tables.addWidget(QLabel('Распределение работ и времени по стадиям жизненного цикла'))
        tables.addWidget(self.life_cycle)
        tables.addWidget(QLabel('Распределение работ по видам деятельности WBS'))
        tables.addWidget(self.wbs)
        

        hbox = QHBoxLayout()
        hbox.addLayout(parameters)
        hbox.addLayout(tables)

        self.setLayout(hbox)

    def __evaluate_project(self):
        try:
            kloc = float(self.kloc.text())
            salary = float(self.salary.text())

            if kloc <= 0:
                raise ValueError
            
            if salary <= 0:
                raise ValueError
        except ValueError:
            self.__error_msg('Число строк и заработная плата должны быть положительными.')
            return
        
        mode_index = self.mode.currentIndex()
        
        drivers = [
            DRIVERS['RELY'][self.rely.currentIndex()],
            DRIVERS['DATA'][self.data.currentIndex()],
            DRIVERS['CPLX'][self.cplx.currentIndex()],

            DRIVERS['TIME'][self.time.currentIndex()],
            DRIVERS['STOR'][self.stor.currentIndex()],
            DRIVERS['VIRT'][self.virt.currentIndex()],
            DRIVERS['TURN'][self.turn.currentIndex()],

            DRIVERS['ACAP'][self.acap.currentIndex()],
            DRIVERS['AEXP'][self.aexp.currentIndex()],
            DRIVERS['PCAP'][self.pcap.currentIndex()],
            DRIVERS['VEXP'][self.vexp.currentIndex()],
            DRIVERS['LEXP'][self.lexp.currentIndex()],

            DRIVERS['MODP'][self.modp.currentIndex()],
            DRIVERS['TOOL'][self.tool.currentIndex()],
            DRIVERS['SCED'][self.sced.currentIndex()]
        ]

        work, time = evaluate_project(mode_index, drivers, kloc)

        life_cycle = get_life_cycle(work, time)
        self.__fill_life_cycle(life_cycle)

        wbs = get_wbs(work, salary)
        self.__fill_wbs(wbs)

        employees = [elem['employees'] for elem in life_cycle.values()]
        plot_employees_bar(employees[:5])

    def __explore_influence(self):
        try:
            kloc = float(self.kloc.text())

            if kloc <= 0:
                raise ValueError
        except ValueError:
            self.__error_msg('Число строк должно быть положительными.')
            return
        
        mode_index = self.mode.currentIndex()

        task1(mode_index, kloc)
        task2(mode_index, kloc)

    def __create_tables(self):
        self.life_cycle = QTableWidget()
        self.life_cycle.setFixedSize(Settings.life_cycle_table_width,
                                     Settings.life_cycle_table_height)
        self.life_cycle.horizontalHeader().setDefaultSectionSize(
            Settings.life_cycle_item_width)
        self.life_cycle.setRowCount(7)
        self.life_cycle.setColumnCount(5)

        self.life_cycle.setVerticalHeaderItem(0,
            QTableWidgetItem('Планирование и определение требований'))
        self.life_cycle.setVerticalHeaderItem(1,
            QTableWidgetItem('Проектирование продукта'))
        self.life_cycle.setVerticalHeaderItem(2,
            QTableWidgetItem('Детальное проектирование'))
        self.life_cycle.setVerticalHeaderItem(3,
            QTableWidgetItem('Кодирование и тестирование отдельных модулей'))
        self.life_cycle.setVerticalHeaderItem(4,
            QTableWidgetItem('Интеграция и тестирование'))
        self.life_cycle.setVerticalHeaderItem(5,
            QTableWidgetItem('Итого без планирования'))
        self.life_cycle.setVerticalHeaderItem(6,
            QTableWidgetItem('ИТОГО'))
        
        self.life_cycle.setHorizontalHeaderItem(0,
            QTableWidgetItem('Трудозатраты (%)'))
        self.life_cycle.setHorizontalHeaderItem(1,
            QTableWidgetItem('Трудозатраты'))
        self.life_cycle.setHorizontalHeaderItem(2,
            QTableWidgetItem('Время (%)'))
        self.life_cycle.setHorizontalHeaderItem(3,
            QTableWidgetItem('Время'))
        self.life_cycle.setHorizontalHeaderItem(4,
            QTableWidgetItem('Сотрудники'))
        

        self.wbs = QTableWidget()
        self.wbs.setFixedSize(Settings.wbs_table_width, 
                              Settings.wbs_table_height)
        self.wbs.horizontalHeader().setDefaultSectionSize(
            Settings.wbs_item_width)
        self.wbs.setRowCount(9)
        self.wbs.setColumnCount(3)

        self.wbs.setVerticalHeaderItem(0,
            QTableWidgetItem('Анализ требований'))
        self.wbs.setVerticalHeaderItem(1,
            QTableWidgetItem('Проектирование продукта'))
        self.wbs.setVerticalHeaderItem(2,
            QTableWidgetItem('Программирование'))
        self.wbs.setVerticalHeaderItem(3,
            QTableWidgetItem('Планирование тестирования'))
        self.wbs.setVerticalHeaderItem(4,
            QTableWidgetItem('Варификация и аттестация'))
        self.wbs.setVerticalHeaderItem(5,
            QTableWidgetItem('Канцелярия проекта'))
        self.wbs.setVerticalHeaderItem(6,
            QTableWidgetItem('Управление конфигурацией и обеспечение качества'))
        self.wbs.setVerticalHeaderItem(7,
            QTableWidgetItem('Создание руководств'))
        self.wbs.setVerticalHeaderItem(8,
            QTableWidgetItem('ИТОГО'))
        
        self.wbs.setHorizontalHeaderItem(0,
            QTableWidgetItem('Бюджет (%)'))
        self.wbs.setHorizontalHeaderItem(1,
            QTableWidgetItem('Человеко-месяцы'))
        self.wbs.setHorizontalHeaderItem(2,
            QTableWidgetItem('Затраты (тыс. рублей)'))
        
    def __fill_life_cycle(self, life_cycle: dict):
        for i, elem in enumerate(life_cycle.values()):
            self.life_cycle.setItem(i, 0, QTableWidgetItem(str(round(elem['work%'], 2))))
            self.life_cycle.setItem(i, 1, QTableWidgetItem(str(round(elem['work'], 2))))
            self.life_cycle.setItem(i, 2, QTableWidgetItem(str(round(elem['time%'], 2))))
            self.life_cycle.setItem(i, 3, QTableWidgetItem(str(round(elem['time'], 2))))
            self.life_cycle.setItem(i, 4, QTableWidgetItem(str(elem['employees'])))

    def __fill_wbs(self, wbs: dict):
        for i, elem in enumerate(wbs.values()):
            self.wbs.setItem(i, 0, QTableWidgetItem(str(round(elem['budget%'], 2))))
            self.wbs.setItem(i, 1, QTableWidgetItem(str(round(elem['work'], 2))))
            self.wbs.setItem(i, 2, QTableWidgetItem(str(round(elem['costs'], 2))))

    def __error_msg(self, text):
        msg = QMessageBox()

        msg.setText(text)
        msg.setWindowTitle(Settings.error_title)

        msg.exec()

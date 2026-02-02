from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QRadioButton, QGroupBox, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt


class MemoryCardUi:
    def setupUi(self, main_window):
        self.centralWidget = QWidget()
        main_window.setCentralWidget(self.centralWidget)
        main_window.resize(300, 300)
        main_window.setWindowTitle("Memory card")

        self.label_question = QLabel("Вопрос")
        self.pushButton_submit = QPushButton("Ответить")

        self.verticalLayout_main = QVBoxLayout()
        self.verticalLayout_answer1 = QVBoxLayout()
        self.verticalLayout_answer2 = QVBoxLayout()
        self.horizontalLayout_line1 = QHBoxLayout()
        self.horizontalLayout_line2 = QHBoxLayout()
        self.horizontalLayout_line3 = QHBoxLayout()

        self.label_statistics = QLabel("Статистика")

        self.verticalLayout_main.addWidget(self.label_statistics, alignment=Qt.AlignRight)
        self.verticalLayout_main.addLayout(self.horizontalLayout_line1, stretch=2)
        self.verticalLayout_main.addLayout(self.horizontalLayout_line2, stretch=8)
        self.verticalLayout_main.addStretch(1)
        self.verticalLayout_main.addLayout(self.horizontalLayout_line3, stretch=1)
        self.verticalLayout_main.addStretch(1)
        self.verticalLayout_main.addSpacing(5)


        self.groupBox_radio = QGroupBox("Варианты ответов")
        self.horizontalLayout_groupBox_radio = QHBoxLayout()
        self.radioButton_answer1 = QRadioButton("Ответ 1")
        self.radioButton_answer2 = QRadioButton("Ответ 2")
        self.radioButton_answer3 = QRadioButton("Ответ 3")
        self.radioButton_answer4 = QRadioButton("Ответ 4")
        self.horizontalLayout_groupBox_radio.addLayout(self.verticalLayout_answer1)
        self.horizontalLayout_groupBox_radio.addLayout(self.verticalLayout_answer2)
        self.groupBox_radio.setLayout(self.horizontalLayout_groupBox_radio)

        self.verticalLayout_answer1.addWidget(self.radioButton_answer1)
        self.verticalLayout_answer1.addWidget(self.radioButton_answer2)
        self.verticalLayout_answer2.addWidget(self.radioButton_answer3)
        self.verticalLayout_answer2.addWidget(self.radioButton_answer4)

        self.groupBox_answer = QGroupBox("Результат теста")
        self.verticalLayout_groupBox_answer = QVBoxLayout()
        self.label_answer_result = QLabel("Прав или нет")
        self.label_answer_correct = QLabel("Правильный ответ")
        self.verticalLayout_groupBox_answer.addWidget(self.label_answer_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
        self.verticalLayout_groupBox_answer.addWidget(self.label_answer_correct, alignment=Qt.AlignCenter, stretch=2)
        self.groupBox_answer.setLayout(self.verticalLayout_groupBox_answer)

        
        self.horizontalLayout_line1.addWidget(self.label_question, alignment=Qt.AlignCenter)

        self.horizontalLayout_line2.addWidget(self.groupBox_radio)
        self.horizontalLayout_line2.addWidget(self.groupBox_answer)

        self.horizontalLayout_line3.addStretch(1)
        self.horizontalLayout_line3.addWidget(self.pushButton_submit, stretch=2)
        self.horizontalLayout_line3.addStretch(1)

        self.centralWidget.setLayout(self.verticalLayout_main)

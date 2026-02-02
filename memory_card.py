from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
from memory_card_ui import MemoryCardUi
from questions import Questions


class MemoryCard(QMainWindow, MemoryCardUi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.groupBox_answer.hide()

        self.current_question_right = None
        self.correct, self.wrong = 0, 0

        self.questions = Questions()
        self.questions.add_question("Сколько будет 2х2", "4", "2", "1", "5")
        self.questions.add_question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский')
        self.questions.add_question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий')
        self.questions.add_question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата')
        self.questions.shuffle_question()

        self.buttons = [
            self.radioButton_answer1,
            self.radioButton_answer2,
            self.radioButton_answer3,
            self.radioButton_answer4
            ]

        self.ask()
        self.connect()

    def connect(self):
        self.pushButton_submit.clicked.connect(self.groupBox_switcher)

    def error(self, error_text):
        error = QMessageBox()
        error.setWindowTitle("Ошибка")
        error.setText(error_text)
        error.exec_()

    def groupBox_switcher(self):
        if self.groupBox_radio.isVisible():
                if not any([btn.isChecked() for btn in self.buttons]):
                    self.error("Выберите ответ")
                    return
                self.check_answer()
                self.groupBox_radio.hide()
                self.groupBox_answer.show()
                self.pushButton_submit.setText("Следующий вопрос")
        else:
            for button in self.buttons:
                button.setAutoExclusive(False)
                button.setChecked(False)
                button.setAutoExclusive(True)

            self.ask()
            self.groupBox_radio.show()
            self.groupBox_answer.hide()
            self.pushButton_submit.setText("Ответить")

    def ask(self):
        question, right_answer, random_answer = self.questions.next_question_random()
        self.current_question_right = right_answer

        self.label_question.setText(question)
        
        for index, btn in enumerate(self.buttons):
            btn.setText(random_answer[index])

    def check_answer(self):
        right_btn = max(self.buttons, key=lambda btn: btn.isChecked())
        if right_btn.text() == self.current_question_right:
            self.correct += 1
            self.label_answer_result.setText("Правильно!")
            self.label_answer_correct.setText(f"Все верно правильный ответ {self.current_question_right}")
        else:
            self.wrong += 1
            self.label_answer_result.setText("Не правильно!")
            self.label_answer_correct.setText(f"Правильный ответ {self.current_question_right}")
        self.update_statistics()

    def update_statistics(self):
        self.label_statistics.setText(f"Правильных ответов: {self.correct}\nНе правильных ответов: {self.wrong}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MemoryCard()
    window.show()
    sys.exit(app.exec_())
    
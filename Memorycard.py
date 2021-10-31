from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
QApplication, QWidget, 
QHBoxLayout, QVBoxLayout, 
QGroupBox, QButtonGroup, QRadioButton,  
QPushButton, QLabel)

window.setWindowTitle('Memo Card')

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question=question
        self.right_answer=right_answer
        self.wrong1=wrong1
        self.wrong2=wrong2
        self.wrong3=wrong3
 
app = QApplication([])
window=QWidget()
 
btn_OK = QPushButton('Ответить') 
lb_Question = QLabel('Самый сложный вопрос в мире!') 
 
RadioGroupBox = QGroupBox("Варианты ответов")
 
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
 
RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
 
RadioGroupBox.setLayout(layout_ans1)
 
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') 
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
 
layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)
 
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым
 
# ----------------------------------------------------------
# Виджеты и макеты созданы, далее - функции:
# ----------------------------------------------------------

window.question = -1
def next_question():
    window.question+=1
    if window.question >= len(quetion_list):
        window.question=0
    q=question_list[window.qwestion]
    ask(q)

def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
 
def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # вернули ограничения, теперь только одна радиокнопка может быть выбрана
 
#https://github.com/hypnotic322/memory_card
answers=[rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setTexst(q.right_answer)
    answers[1].setTexst(q.wrong1)
    answers[2].setTexst(q.wrong2)
    answers[3].setTexst(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def chow_correct(res):
    lb_Result.setText(res)
    show_result()

def test():
    if answers[0].isCrecked():
        show_correct('Верно!')
    elif answers[1].isCrecked or answers[2].isCrecked or answers[3].isCrecked:
        show_correct('Неверно!')

def click_OK():
    if btn_OK.text()=='Ответить':
        test()
    else:
        next_question()

q=Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итольянский')
question_list=[]
question_list.append(q)
question_list.append(Question('1000-7', '993', '998', '4', '21'))
window.question=-1
next_question()
btn_OK.clicked.connect(click_OK) # проверяем, что панель ответов показывается при нажатии на кнопку
window.setLayout(layout_card)
window.show()
app.exec_()

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import shuffle
class Question():
        def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
                self.question = question
                self.right_answer = right_answer
                self.wrong1 = wrong1
                self.wrong2 = wrong2
                self.wrong3 = wrong3

q1 = Question("In what year was the grear fire of London", "1666", "1999", "1062", "666")
q2 = Question("How old is the queen of England", "95","96","100","97")
q3 = Question("How far is the sun?", "148.28 million km", "138.50 million km","128.75 million km","150.20 million km")
q4 = Question("How far is a mile in km?", "1.609344 km", "1.539954 km","1.249913 km","1.847564 km")
q5 = Question("Who is the most whelthiest man?", "Elon Musk", "Bill Gates", "Mark Zuckerberg","PewDiePie")

q_list = [q1,q2,q3,q4,q5]

def next_qst():
        if len(q_list):
                shuffle(q_list)
                main_win.counter = main_win.counter + 1
                if main_win.counter >= len(q_list):
                        main_win.counter = 0
                q=q_list[main_win.counter]
                ask(q)
                q_list.remove(q)
        else:
                label1.setText("There are no more quastion")
                b1.setText("Finish")
def show_ans():
        gbox1.hide()
        gbox2.show()
        main_win.counter3 = 1
        ans_b.setText("Next question")
        if b_list[0].isChecked ():
                label2.setText("Correct!")
                main_win.counter2 += 1
        else:
                label2.setText("Incorrect!")
        label4.setText("Correct answers: "+str(main_win.counter2))
        label5.setText("user rating: "+str(main_win.counter2/main_win.counter3*100)+" %")
def show_qst():
        gbox1.show()
        gbox2.hide()
        ans_b.setText("Answer")
        RadioGroup.setExclusive(False)
        b1.setChecked(False)
        b2.setChecked(False)
        b3.setChecked(False)
        b4.setChecked(False)
        RadioGroup.setExclusive(True)
def test():
        if b1.text() =="Finish":
                quit()
        elif ans_b.text() == "Answer":
                show_ans()
        else:
                next_qst()    
def ask(q: Question):
        shuffle(b_list)
        label1.setText(q.question)
        b_list[0].setText(q.right_answer)
        b_list[1].setText(q.wrong1)
        b_list[2].setText(q.wrong2)
        b_list[3].setText(q.wrong3)
        label3.setText(q.right_answer)
        show_qst()



app=QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Memory Card App")
main_win.move(400,300)
main_win.resize(400,300)
main_win.counter = -1
main_win.counter2 = 0
main_win.counter3 = 0

label1 = QLabel("A very difficult question.")
gbox1 = QGroupBox("Answer options")
gbox2 = QGroupBox("Correct Answer:")
label2=QLabel("--Correct/Incorrect--")
label3=QLabel("--correct answer written here--")
label4 = QLabel("--correct answers: 0--")
label5 = QLabel("--User rating: 0%--")
v4 = QVBoxLayout()
v4.addWidget(label2)
v4.addWidget(label3)
gbox2.setLayout(v4)
b1=QRadioButton("Option 1")
b2=QRadioButton("Option 2")
b3=QRadioButton("Option 3")
b4=QRadioButton("Option 4")
ans_b = QPushButton("Answer")
b_list = [b1,b2,b3,b4]


RadioGroup = QButtonGroup()
RadioGroup.addButton(b1)
RadioGroup.addButton(b2)
RadioGroup.addButton(b3)
RadioGroup.addButton(b4)

v1=QVBoxLayout()
v2=QVBoxLayout()
v3=QVBoxLayout()
h1=QHBoxLayout()

v1.addWidget(label4, alignment=Qt.AlignRight)
v1.addWidget(label5, alignment=Qt.AlignRight)
v1.addWidget(label1, alignment=Qt.AlignCenter)
v1.addWidget(gbox1)
v1.addWidget(gbox2) 
v1.addWidget(ans_b, stretch=3)
v2.addWidget(b1)
v2.addWidget(b2)
v3.addWidget(b3)
v3.addWidget(b4)
h1.addLayout(v2)
h1.addLayout(v3)
gbox1.setLayout(h1)

main_win.setLayout(v1)
next_qst()

gbox2.hide()
ans_b.clicked.connect(test)
main_win.show()
app.exec()

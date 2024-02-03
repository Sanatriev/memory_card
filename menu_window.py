from PyQt5.QtWidgets import*
from PyQt5.QtCore import Qt

app=QApplication([])

q=QLabel("Введіть запитаня")
q_red = QLineEdit()
a = QLabel("Введіть вірну відповідь")
a_red = QLineEdit()
w1 = QLabel("Введіть першу хибну відповідь")
w1_red=QLineEdit()
w2=QLabel("Введьть другу хибну відповідь")
w2_red=QLineEdit()
w3=QLabel("Введьть третю хибну відповідь")
w3_red=QLineEdit()

btn_add=QPushButton("Додати запитаня")
btn_clear=QPushButton("Очистити")

btn_back=QPushButton("Назад")
stat=QLabel("Статистика")
stat_info=QLabel("Інфо")

line_menu=QVBoxLayout()
line1_menu=QVBoxLayout()
line2_menu=QVBoxLayout()

line1_menu.addWidget(q)
line1_menu.addWidget(a)
line1_menu.addWidget(w1)
line1_menu.addWidget(w2)
line1_menu.addWidget(w3)

line2_menu.addWidget(q_red)
line2_menu.addWidget(a_red)
line2_menu.addWidget(w1_red)
line2_menu.addWidget(w2_red)
line2_menu.addWidget(w3_red)


line_hor=QHBoxLayout()
line2_hor=QHBoxLayout()

line_hor.addLayout(line1_menu)
line_hor.addLayout(line2_menu)

line2_hor.addWidget(btn_add)
line2_hor.addWidget(btn_clear)

line_menu.addLayout(line_hor)
line2_menu.addLayout(line2_hor)

line_menu.addWidget(stat)
line_menu.addWidget(stat_info)
line_menu.addWidget(btn_back)

menu_win=QWidget()
menu_win.setLayout(line_menu)

menu_win.show()

app.exec()

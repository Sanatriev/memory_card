from PyQt5.QtWidgets import*
app=QApplication([])
from main_window import*

main_win=QWidget()
main_win.resize(600,500)
main_win.setWindowTitle("Memory Card")
main_win.move(300,300)



main_win.setLayout(line)

btn_answer.clicked.connect(swich_scrern)
main_win.show()



app.exec()

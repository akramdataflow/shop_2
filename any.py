import sys 
from PySide6.QtWidgets import QSpinBox, QMainWindow, QPushButton, QGridLayout, QFrame, QVBoxLayout, QLabel , QLineEdit
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import Qt, QSize

class Lists(QMainWindow):
    def _init_(self, controller):
        super()._init_()
        self.controller = controller

        self.setWindowTitle("القوائم")
        self.resize(500, 500)

        # فريم جديد
        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)

        # فريم العنوان مع Layout خاص به
        lest_label_frame = QFrame()
        layout1 = QVBoxLayout(lest_label_frame)  # استخدام Layout منفصل
        lest_label_frame.setStyleSheet("""
            background-color: #50F296; 
            color: white;
            background-repeat: no-repeat;
            background-position: center;
        """)
        lest_label_frame.setFixedHeight(50)

        new_layout.addWidget(lest_label_frame, 0, 0 , 1 , 0)  # الهيدر 

        # فريم يحتوي على باقي العناصر مع Layout منفصل
        frame = QFrame()
        layout2 = QGridLayout(frame)
        new_layout.addWidget(frame, 1, 1)

        # إضافة أيقونة في Layout1 (Layout العنوان)
        icon_label = QLabel(lest_label_frame)
        icon = QIcon('./static/09.png')  
        icon_label.setPixmap(icon.pixmap(100, 100))  # تحديد حجم الأيقونة
        layout1.addWidget(icon_label)

        # إضافة نص في Layout2 (Layout الفريم)
        label_price = QLabel("السعر")
        label_price.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        layout2.addWidget(label_price, 0, 3)

        price_input = QLineEdit()
        price_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        layout2.addWidget(price_input, 0, 2)

        # اسم الشركة
        label_company = QLabel("أسم الشركة")
        label_company.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        layout2.addWidget(label_company, 0, 1)

        company_input = QLineEdit()
        company_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        layout2.addWidget(company_input, 0, 0)

        # التاريخ والوقت
        label_datetime = QLabel("التاريخ والوقت")
        label_datetime.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        layout2.addWidget(label_datetime, 1, 1)

        datetime_input = QLineEdit()
        datetime_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        layout2.addWidget(datetime_input, 1, 0)

        # رقم القائمة
        label_list_number = QLabel("رقم القائمة")
        label_list_number.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        layout2.addWidget(label_list_number, 1, 3)

        list_number_input = QLineEdit()
        list_number_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        layout2.addWidget(list_number_input, 1, 2)



        # الفريم الاسفل الابيض 

        frame_white= QFrame()
        frame_white.setStyleSheet("""

                       QFrame  {
                    background-color: #fff; 
                                  
                                  
                                   }
           
                                  
                                  
                                  
                                  """)
        
        new_layout = QGridLayout(frame_white,2,0)
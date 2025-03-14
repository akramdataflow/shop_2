import sys 
from PySide6.QtWidgets import QSpinBox, QMainWindow, QPushButton, QGridLayout, QFrame, QVBoxLayout, QLabel , QLineEdit , QSizePolicy, QDateEdit, QTableWidget, QTableWidgetItem, QSizePolicy, QHeaderView, QAbstractItemView, QHBoxLayout
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import QDate, QSize
from datetime import datetime

class MyView(QMainWindow):
    def __init__(self, controller=None):
        super().__init__()
        self.controller = controller

        self.setGeometry(100, 200, 800, 1000)

        self.showMaximized()

        main_frame = QFrame()
        main_frame.setStyleSheet(
            """background-color: #fff"""
        )
        layout = QGridLayout(main_frame)

        label_frame = QFrame()
        label_frame_layout = QVBoxLayout(label_frame)
        label_frame.setStyleSheet("""
                                  background-color: #1A3654; 
                                  color: white;
                                  background-image: url('./static/لنكيدو Market.png');
                                  background-repeat: no-repeat;
                                  background-position: center;
                                  """)
        label_frame.setFixedHeight(100)
        label_frame.setGeometry(0, 0, 800, 1000)

        
        

        



        layout.addWidget(label_frame, 0, 0)

        self.setCentralWidget(main_frame)

        frame = QFrame()
        frame_layout = QGridLayout(frame)
        layout.addWidget(frame, 1, 0)

        icon = QIcon('./static/Untitled (4).png')

        # Button 1
        button1 = QPushButton()
        button1.clicked.connect(self.controller.show_list)
        button1.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-image: url('./static/Group 1.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button1.setIcon(icon)
        button1.setIconSize(QSize(200, 200))
        frame_layout.addWidget(button1, 0, 0)

        # Button 2
        button2 = QPushButton()
        button2.clicked.connect(self.controller.show_sales)
        button2.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-image: url('./static/Group 2.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button2.setIcon(icon)
        button2.setIconSize(QSize(200, 200))
        frame_layout.addWidget(button2, 0, 1)

        # Button 3
        button3 = QPushButton()
    
        button3.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-image: url('./static/Group 3.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button3.setIcon(icon)
        button3.clicked.connect(self.controller.show_Purchases)
        button3.setIconSize(QSize(200, 200))
        frame_layout.addWidget(button3, 0, 2)

        # Button 4
        button4 = QPushButton()
        button4.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-image: url('./static/Group 4.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button4.setIcon(icon)
        button4.clicked.connect(self.controller.show_Deferred)
        button4.setIconSize(QSize(200, 200))
        frame_layout.addWidget(button4, 1, 0)

        # Button 5
        button5 = QPushButton()
        button5.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-image: url('./static/Group 5.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button5.setIcon(icon)
        button5.clicked.connect(self.controller.show_materials)
        button5.setIconSize(QSize(200, 200))
        frame_layout.addWidget(button5, 1, 1)

        # Button 6
        button6 = QPushButton()
        button6.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-image: url('./static/Group 6.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button6.setIcon(icon)
        button6.clicked.connect(self.controller.show_closet)       
        button6.setIconSize(QSize(200, 200))
        frame_layout.addWidget(button6, 1, 2)

        # Button 7
        button7 = QPushButton()
        button7.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-repeat: no-repeat;
                background-image: url('./static/Group 7.png');
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button7.setIcon(icon)
        button7.clicked.connect(self.controller.show_Data_analysis) 
        button7.setIconSize(QSize(200, 200))
        frame_layout.addWidget(button7, 2, 0)


class Lists(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("القوائم")
        self.resize(500, 500)

        self.showMaximized()

        
        # فريم جديد
        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
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
        # 1,2 لكي تاخذ صف واحد وعمودين الاول والثاني
        new_layout.addWidget(lest_label_frame, 0, 0, 1, 2)  # الهيدر 

        # فريم يحتوي على باقي العناصر مع Layout منفصل
        frame = QFrame()
        layout2 = QGridLayout(frame)
        new_layout.addWidget(frame, 1, 0, 1, 2)

        # إضافة أيقونة في Layout1 (Layout العنوان)
        icon_label = QLabel(lest_label_frame)
        icon = QIcon('./static/12.png')  
        icon_label.setPixmap(icon.pixmap(100, 100))  # تحديد حجم الأيقونة
        layout1.addWidget(icon_label)



        
        frame = QFrame()
        data_frame_layout = QVBoxLayout(frame)
        
        # استرجاع البيانات من الموديل عبر الكونترولر
        # Get the bill details from the model
        bill_details = controller.get_bill_detales_from_model()
        
        # Assign total_price_list from bill_details
        total_price_list = bill_details[-1]
        
        # Convert total_price_list to floats
        total_price_list = [float(price) for price in total_price_list]
        
        # Calculate the total price for all items
        total_price_for_all_items = sum(total_price_list)      
        # إنشاء جدول البيانات
        self.table = QTableWidget()

        #جعل حجم الجدول يتناسب مع حجم الشاشه 
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        self.table.setAlternatingRowColors(True)
        
        # تعيين خلفية الجدول إلى اللون الأبيض
        self.table.setStyleSheet("background-color: white;")

        
        # إعداد الجدول: تعيين الأعمدة
        self.table.setColumnCount(5)  # عدد الأعمدة (الاسم، النوع، العدد، تاريخ الانتهاء)
        self.table.setHorizontalHeaderLabels(['المادة','سعر القطعة','العدد', 'السعر الكلي', 'الترميز'])  # العناوين
        
        # تعبئة الجدول بالبيانات
        if bill_details and len(bill_details[0]) > 0:  # التأكد من وجود بيانات
            row_count = len(bill_details[0])  # افتراض أن جميع الأعمدة لها نفس الطول
            self.table.setRowCount(row_count)
        
            # تعبئة البيانات في الجدول
            for row in range(row_count): 
                self.table.setItem(row, 4, QTableWidgetItem(bill_details[0][row]))  # إدخال الاسم
                self.table.setItem(row, 0, QTableWidgetItem(bill_details[1][row]))  # إدخال رقم الهاتف
                self.table.setItem(row, 1, QTableWidgetItem(str(bill_details[2][row])))  # إدخال العنوان
                self.table.setItem(row, 2, QTableWidgetItem(str(bill_details[3][row])))  #السعر
                self.table.setItem(row, 3, QTableWidgetItem(str(bill_details[4][row])))   #id
        
            # تعديل حجم الأعمدة لتناسب المحتوى بعد تعبئة الجدول
            self.table.resizeColumnsToContents()
        else:
            self.table.setRowCount(0)
        
        # إضافة الجدول إلى التخطيط داخل الفريم
        data_frame_layout.addWidget(self.table)
        
        # تعيين التخطيط للفريم
        frame.setLayout(data_frame_layout)
        
        # إضافة الفريم إلى التخطيط الخارجي
        new_layout.addWidget(frame, 1, 0)
        
        #فريم المجموع
        total_frame = QFrame()
        total_frame_layout = QHBoxLayout(total_frame)
        new_layout.addWidget(total_frame, 2, 0, 1, 2)

        date = datetime.now().strftime('%Y-%m-%d')

        label = QLabel(f"تاريخ الفاتورة : {date}")
        label.setStyleSheet('''
            background-color: #ffffff;
            font-family: Inter;
            font-size:20px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        total_frame_layout.addWidget(label)


        label = QLabel(f"رقم الفاتورة : {33000}")
        label.setStyleSheet('''
             background-color: #ffffff;
            font-family: Inter;
            font-size:20px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        total_frame_layout.addWidget(label)

        label = QLabel(f"المجموع : {total_price_for_all_items}")
        label.setStyleSheet('''
             background-color: #ffffff;
            font-family: Inter;
            font-size:20px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        total_frame_layout.addWidget(label)


        
        #انشاء فريم للحفض الفريم الابيض الجانبي
        save_frame = QFrame()
        save_frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #1A3654;
        """)
        save_frame_layout = QGridLayout(save_frame)
        # save_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

       

        label = QLabel("")
        label.setStyleSheet('''
             background-color: #1A3654;
            font-family: Inter;
            font-size:20px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')

        save_frame_layout.addWidget(label,0,0)
        # 1,1 تعني العمود الثاني والصف الثاني

        # 2,1 تعني انهو ياخذ صفين الثاني والثالث وياخذ عمود واحد
        new_layout.addWidget(save_frame,1,1)


        button1 = QPushButton()
        button1.setStyleSheet("""
                 QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                              
                              
                               """)
        
        icon = QIcon('./static/13.png')  # تحميل الأيقونة
        button1.setIcon(icon)
        button1.setIconSize(QSize(200, 62))
       
        save_frame_layout.addWidget(button1,0,0)
        


        
        button2 = QPushButton()
        button2.clicked.connect(self.controller.del_bill_detales_show)
        button2.setStyleSheet("""
                     QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }       
                              
                               """)
        
        icon = QIcon('./static/14.png')  # تحميل الأيقونة
        button2.setIcon(icon)
        button2.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button2,1,0)
        
        

        
        button3 = QPushButton()
        button3.clicked.connect(self.controller.show_Deferred)
        button3.setStyleSheet("""
                    QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }      
                              
                               """)
        
        icon = QIcon('./static/15.png')  # تحميل الأيقونة
        button3.setIcon(icon)
        button3.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button3,2,0)
        


    





       

class Sales(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("المبيعات")
        self.resize(500, 500)
         
        # فريم جديد
       
 # فريم جديد
        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
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
        # 1,2 لكي تاخذ صف واحد وعمودين الاول والثاني
        new_layout.addWidget(lest_label_frame, 0, 0, 1, 2)  # الهيدر 

        # فريم يحتوي على باقي العناصر مع Layout منفصل
        frame = QFrame()
        layout2 = QGridLayout(frame)
        new_layout.addWidget(frame, 1, 0, 1, 2)

        # إضافة أيقونة في Layout1 (Layout العنوان)
        icon_label = QLabel(lest_label_frame)
        icon = QIcon('./static/10.png')  
        icon_label.setPixmap(icon.pixmap(100, 100))  # تحديد حجم الأيقونة
        layout1.addWidget(icon_label)

        save_frame = QFrame()
        save_frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #1A3654;
        """)
        save_frame_layout = QGridLayout(save_frame)
        # save_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        frame = QFrame()
        frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        frame.setFixedHeight(700)
        new_layout.addWidget(frame,1,0)
        frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)



    

        
        #انشاء فريم للحفض الفريم الابيض الجانبي
        save_frame = QFrame()
        save_frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #1A3654;
        """)
        save_frame_layout = QGridLayout(save_frame)


        
        label = QLabel("")
        label.setStyleSheet('''
             background-color: #1A3654;
            font-family: Inter;
            font-size:20px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')

        save_frame_layout.addWidget(label,0,0)
        # 1,1 تعني العمود الثاني والصف الثاني

        # 2,1 تعني انهو ياخذ صفين الثاني والثالث وياخذ عمود واحد
        new_layout.addWidget(save_frame,1,1)



        # البحث في فريم الجانبي لل (save frame layout)

        label_history = QLabel("التاريخ")
        label_history.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_history, 0, 1)

        history_input = QLineEdit()
        
       
        
        history_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(history_input, 0, 0)





        #المجموع 
        button3 = QPushButton()
        button3.setStyleSheet("""
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;
                             
                               """)
        
        icon = QIcon('./static/Group 9 (1).png')  # تحميل الأيقونة
        button3.setIcon(icon)
        button3.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button3,1,0)
        


        total_input = QLineEdit()
        total_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(total_input, 2, 0)


       











class Purchases(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("المشتريات")
        self.resize(500, 500)
        
        # فريم جديد
        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
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
        # 1,2 لكي تاخذ صف واحد وعمودين الاول والثاني
        new_layout.addWidget(lest_label_frame, 0, 0, 1, 2)  # الهيدر 

        # فريم يحتوي على باقي العناصر مع Layout منفصل
        frame = QFrame()
        layout2 = QGridLayout(frame)
        new_layout.addWidget(frame, 1, 0, 1, 2)

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

        self.price = QLineEdit()
        self.price.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        layout2.addWidget(self.price, 0, 2)

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

        self.company_name = QLineEdit()
        self.company_name.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        layout2.addWidget(self.company_name, 0, 0)

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

        self.date_h = QDateEdit()
        self.date_h.setDate(QDate.currentDate())  # إضافة الأقواس

        self.date_h.setDisplayFormat("dd/MM/yyyy")
        self.date_h.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        layout2.addWidget(self.date_h, 1, 0)



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

        self.bill_num = QLineEdit()
        self.bill_num.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        layout2.addWidget(self.bill_num, 1, 2)

       
        
        
        frame = QFrame()
        data_frame_layout = QVBoxLayout(frame)
        
        # استرجاع البيانات من الموديل عبر الكونترولر
        data_tabel = self.controller.get_purc_from_model()
        
        # إنشاء جدول البيانات
        self.table = QTableWidget()

        #جعل حجم الجدول يتناسب مع حجم الشاشه 
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.table.setAlternatingRowColors(True)
        
        # تعيين خلفية الجدول إلى اللون الأبيض
        self.table.setStyleSheet("background-color: white;")

        
        # إعداد الجدول: تعيين الأعمدة
        self.table.setColumnCount(5)  
        self.table.setHorizontalHeaderLabels(['السعر', 'اسم الشركة', 'رقم القاىمة', 'التاريخ والوقت', 'الترميز']) 
        
        # تعبئة الجدول بالبيانات
        if data_tabel and len(data_tabel[0]) > 0:  # التأكد من وجود بيانات
            row_count = len(data_tabel[0])  # افتراض أن جميع الأعمدة لها نفس الطول
            self.table.setRowCount(row_count)
        
            # تعبئة البيانات في الجدول
            for row in range(row_count):
                self.table.setItem(row, 4, QTableWidgetItem(str(data_tabel[0][row])))  
                self.table.setItem(row, 0, QTableWidgetItem(data_tabel[1][row]))  # إدخال الاسم
                self.table.setItem(row, 1, QTableWidgetItem(data_tabel[2][row]))  # إدخال النوع
                self.table.setItem(row, 2, QTableWidgetItem(str(data_tabel[3][row])))  # إدخال العدد
                self.table.setItem(row, 3, QTableWidgetItem(str(data_tabel[4][row])))  # إدخال تاريخ الانتهاء
                
        
            # تعديل حجم الأعمدة لتناسب المحتوى بعد تعبئة الجدول
            self.table.resizeColumnsToContents()
        else:
            self.table.setRowCount(0)
        
        # إضافة الجدول إلى التخطيط داخل الفريم
        data_frame_layout.addWidget(self.table)
        
        # تعيين التخطيط للفريم
        frame.setLayout(data_frame_layout)
        
        # إضافة الفريم إلى التخطيط الخارجي
        new_layout.addWidget(frame, 2, 0)

       

        save_frame = QFrame()
        save_frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #1A3654;
        """)
        save_frame_layout = QGridLayout(save_frame)
        # save_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)



        label = QLabel("")
        label.setStyleSheet('''
             background-color: #1A3654;
            font-family: Inter;
            font-size:20px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')

        save_frame_layout.addWidget(label,0,1)
        # 1,1 تعني العمود الثاني والصف الثاني

        # 2,1 تعني انهو ياخذ صفين الثاني والثالث وياخذ عمود واحد
        new_layout.addWidget(save_frame,2,2)



        button1 = QPushButton()
        button1.clicked.connect(self.send_purc_to_controller)
        button1.setStyleSheet("""
                 QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                              
                              
                               """)
        
        icon = QIcon('./static/Group 8 (1).png')  # تحميل الأيقونة
        button1.setIcon(icon)
        button1.setIconSize(QSize(90, 36))
       
        save_frame_layout.addWidget(button1,0,0)
       



        
        button2 = QPushButton()
        button2.clicked.connect(self.controller.del_purc_show)
        button2.setStyleSheet("""
                    QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }       
                              
                               """)
        
        icon = QIcon('./static/Group 8 (2).png')  # تحميل الأيقونة
        button2.setIcon(icon)
        button2.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button2,1,0)
        




        
        
        


        label = QLabel(f"المجموع : {save_frame_layout}")
        label.setStyleSheet('''
             background-color: #ffffff;
            font-family: Inter;
            font-size:20px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label,2,0)

    def send_purc_to_controller(self):
        # الحصول على البيانات من الواجهة
        price = self.price.text()
        company_name = self.company_name.text()
        bill_num = self.bill_num.text()
        date = self.date_h.date().toString('yyyy-MM-dd')
        

        # إرسال البيانات إلى الكونترولر لإضافتها للنموذج
        self.controller.add_purc_to_model(price, company_name, bill_num, date)

        # تحديث الجدول بعد الحفظ
        self.refresh_table()

    def refresh_table(self):
        # استرجاع البيانات من النموذج عبر الكونترولر
        data_table = self.controller.get_purc_from_model()

        # مسح البيانات القديمة في الجدول
        self.table.setRowCount(0)

        # تعبئة الجدول بالبيانات الجديدة
        if data_table and len(data_table[0]) > 0:
            row_count = len(data_table[0])  # افتراض أن جميع الأعمدة لها نفس الطول
            self.table.setRowCount(row_count)

            for row in range(row_count):
                self.table.setItem(row, 4, QTableWidgetItem(str(data_table[0][row])))  # إدخال الاسم
                self.table.setItem(row, 0, QTableWidgetItem(data_table[1][row]))  # إدخال الاسم
                self.table.setItem(row, 1, QTableWidgetItem(data_table[2][row]))  # إدخال النوع
                self.table.setItem(row, 2, QTableWidgetItem(str(data_table[3][row])))  # إدخال العدد
                self.table.setItem(row, 3, QTableWidgetItem(str(data_table[4][row])))  # إدخال تاريخ الانتهاء
                




        












#4


class Deferred(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("دفع مؤجل")
        self.resize(500, 500)

        self.showMaximized()

         
        # فريم جديد
        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
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
        # 1,2 لكي تاخذ صف واحد وعمودين الاول والثاني
        new_layout.addWidget(lest_label_frame, 0, 0, 1, 2)  # الهيدر 

        # فريم يحتوي على باقي العناصر مع Layout منفصل
        frame = QFrame()
        
        new_layout.addWidget(frame, 1, 0, 1, 2)

        # إضافة أيقونة في Layout1 (Layout العنوان)
        icon_label = QLabel(lest_label_frame)
        icon = QIcon('./static/15.png')  
        icon_label.setPixmap(icon.pixmap(100, 100))  # تحديد حجم الأيقونة
        layout1.addWidget(icon_label)


         #انشاء فريم لوضع البيانات الفريم الابيض السفلي
        
         #انشاء فريم لوضع البيانات الفريم الابيض السفلي
        frame = QFrame()
        data_frame_layout = QVBoxLayout(frame)
        
        # استرجاع البيانات من الموديل عبر الكونترولر
        data_tabel = self.controller.get_Deferred_from_model()
        
        # إنشاء جدول البيانات
        self.table = QTableWidget()

        #جعل حجم الجدول يتناسب مع حجم الشاشه 
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.table.setAlternatingRowColors(True)
        
        # تعيين خلفية الجدول إلى اللون الأبيض
        self.table.setStyleSheet("background-color: white;")

        
        # إعداد الجدول: تعيين الأعمدة
        self.table.setColumnCount(5)  # عدد الأعمدة (الاسم، النوع، العدد، تاريخ الانتهاء)
        self.table.setHorizontalHeaderLabels(['اسم العميل', 'رقم الهاتف', 'العنوان', 'السعر', 'الترميز'])  # العناوين
        
        # تعبئة الجدول بالبيانات
        if data_tabel and len(data_tabel[0]) > 0:  # التأكد من وجود بيانات
            row_count = len(data_tabel[0])  # افتراض أن جميع الأعمدة لها نفس الطول
            self.table.setRowCount(row_count)
        
            # تعبئة البيانات في الجدول
            for row in range(row_count): 
                self.table.setItem(row, 0, QTableWidgetItem(data_tabel[1][row]))  # إدخال الاسم
                self.table.setItem(row, 1, QTableWidgetItem(data_tabel[2][row]))  # إدخال رقم الهاتف
                self.table.setItem(row, 2, QTableWidgetItem(str(data_tabel[3][row])))  # إدخال العنوان
                self.table.setItem(row, 3, QTableWidgetItem(str(data_tabel[4][row])))  #السعر
                self.table.setItem(row, 4, QTableWidgetItem(str(data_tabel[0][row])))   #id
        
            # تعديل حجم الأعمدة لتناسب المحتوى بعد تعبئة الجدول
            self.table.resizeColumnsToContents()
        else:
            self.table.setRowCount(0)
        
        # إضافة الجدول إلى التخطيط داخل الفريم
        data_frame_layout.addWidget(self.table)
        
        # تعيين التخطيط للفريم
        frame.setLayout(data_frame_layout)
        
        # إضافة الفريم إلى التخطيط الخارجي
        new_layout.addWidget(frame, 1, 0)
    


        
        #انشاء فريم للحفض الفريم الابيض الجانبي
        save_frame = QFrame()
        save_frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #1A3654;
        """)
        save_frame_layout = QGridLayout(save_frame)
        

       




        label = QLabel("")
        label.setStyleSheet('''
             background-color: #1A3654;
            font-family: Inter;
            font-size:20px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')

        save_frame_layout.addWidget(label,0,2)
        # 1,1 تعني العمود الثاني والصف الثاني

        # 2,1 تعني انهو ياخذ صفين الثاني والثالث وياخذ عمود واحد
        new_layout.addWidget(save_frame,1,1)


        
        
        # البحث في فريم الجانبي لل (save frame layout)

        label_history = QLabel("اسم العميل")
        label_history.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_history, 0, 1)

        self.customer_name = QLineEdit()
        self.customer_name.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget( self.customer_name, 0, 0)


        
        # البحث في فريم الجانبي لل (save frame layout)

        label_history = QLabel("رقم الهاتف ")
        label_history.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_history, 1, 1)

        self.phone_num = QLineEdit()
        self.phone_num.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.phone_num , 1, 0)

        ######
        
        
        # البحث في فريم الجانبي لل (save frame layout)

        label_number = QLabel("العنوان")
        label_number.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_number, 2, 1)

        self.address = QLineEdit()
        self.address.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.address, 2, 0)



        
        # البحث في فريم الجانبي لل (save frame layout)

        label_End_date = QLabel("السعر ")
        label_End_date.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_End_date, 3, 1)

        self.price = QLineEdit()
        self.price.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.price, 3, 0)


         #المجموع 
        button1 = QPushButton()
        button1.clicked.connect(self.send_data_defer_to_controller)
        button1.setStyleSheet("""
                    QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                             
                               """)
        
        icon = QIcon('./static/Group 8 (1).png')  # تحميل الأيقونة
        button1.setIcon(icon)
        button1.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button1,4,0,1,2)



        button2 = QPushButton()
        button2.clicked.connect(self.controller.update_defer_show)
        button2.setStyleSheet("""
                     QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                             
                               """)
        
        icon = QIcon('./static/20.png')  # تحميل الأيقونة
        button2.setIcon(icon)
        button2.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button2,5,0,1,2)

        
        button3 = QPushButton()
        button3.clicked.connect(self.controller.del_defer_show)
        button3.setStyleSheet("""
                     QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                             
                               """)
        
        icon = QIcon('./static/14.png')  # تحميل الأيقونة
        button3.setIcon(icon)
        button3.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button3,6,0,1,2)


        
    def send_data_defer_to_controller(self):
        # الحصول على البيانات من الواجهة
        customer_name = self.customer_name.text()
        phone_num = self.phone_num.text()
        address = self.address.text()
        price = self.price.text()

        # إرسال البيانات إلى الكونترولر لإضافتها للنموذج
        self.controller.add_Deferred_to_model(customer_name, phone_num, address, price)

        # تحديث الجدول بعد الحفظ
        self.refresh_table()

    def refresh_table(self):
        # استرجاع البيانات من النموذج عبر الكونترولر
        data_table = self.controller.get_Deferred_from_model()

        # مسح البيانات القديمة في الجدول
        self.table.setRowCount(0)

        # تعبئة الجدول بالبيانات الجديدة
        if data_table and len(data_table[0]) > 0:
            row_count = len(data_table[0])  # افتراض أن جميع الأعمدة لها نفس الطول
            self.table.setRowCount(row_count)

            
            for row in range(row_count):
                self.table.setItem(row, 4, QTableWidgetItem(str(data_table[0][row])))  # إدخال الاسم
                self.table.setItem(row, 0, QTableWidgetItem(data_table[1][row]))  # إدخال الاسم
                self.table.setItem(row, 1, QTableWidgetItem(data_table[2][row]))  # إدخال النوع
                self.table.setItem(row, 2, QTableWidgetItem(str(data_table[3][row])))  # إدخال العدد
                self.table.setItem(row, 3, QTableWidgetItem(str(data_table[4][row])))







class  Materials(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("اضافة مواد")
        self.resize(500, 500)

        self.showMaximized()
        
        # فريم جديد
        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
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
        # 1,2 لكي تاخذ صف واحد وعمودين الاول والثاني
        new_layout.addWidget(lest_label_frame, 0, 0, 1, 2)  # الهيدر 

        # فريم يحتوي على باقي العناصر مع Layout منفصل
        frame = QFrame()
        new_layout.addWidget(frame, 1, 0, 1, 2)

        # إضافة أيقونة في Layout1 (Layout العنوان)
        icon_label = QLabel(lest_label_frame)
        icon = QIcon('./static/17.png')  
        icon_label.setPixmap(icon.pixmap(100, 100))  # تحديد حجم الأيقونة
        layout1.addWidget(icon_label)






         #انشاء فريم لوضع البيانات الفريم الابيض السفلي
        frame = QFrame()
        data_frame_layout = QVBoxLayout(frame)
        
        # استرجاع البيانات من الموديل عبر الكونترولر
        data_tabel = self.controller.get_material_from_model()
        
        # إنشاء جدول البيانات
        self.table = QTableWidget()

        #جعل حجم الجدول يتناسب مع حجم الشاشه 
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.table.setAlternatingRowColors(True)
        
        # تعيين خلفية الجدول إلى اللون الأبيض
        self.table.setStyleSheet("background-color: white;")

        
        # إعداد الجدول: تعيين الأعمدة
        self.table.setColumnCount(6)  # عدد الأعمدة (الاسم، النوع، العدد، تاريخ الانتهاء)
        self.table.setHorizontalHeaderLabels(['الاسم', 'النوع', 'العدد', 'تاريخ الانتهاء', 'السعر', 'الترميز'])  # العناوين
        
        # تعبئة الجدول بالبيانات
        if data_tabel and len(data_tabel[0]) > 0:  # التأكد من وجود بيانات
            row_count = len(data_tabel[0])  # افتراض أن جميع الأعمدة لها نفس الطول
            self.table.setRowCount(row_count)
        
            # تعبئة البيانات في الجدول
            for row in range(row_count):
                self.table.setItem(row, 5, QTableWidgetItem(str(data_tabel[0][row])))  
                self.table.setItem(row, 0, QTableWidgetItem(data_tabel[1][row]))  # إدخال الاسم
                self.table.setItem(row, 1, QTableWidgetItem(data_tabel[2][row]))  # إدخال النوع
                self.table.setItem(row, 2, QTableWidgetItem(str(data_tabel[3][row])))  # إدخال العدد
                self.table.setItem(row, 3, QTableWidgetItem(str(data_tabel[4][row])))  # إدخال تاريخ الانتهاء
                self.table.setItem(row, 4, QTableWidgetItem(str(data_tabel[5][row])))
        
            # تعديل حجم الأعمدة لتناسب المحتوى بعد تعبئة الجدول
            self.table.resizeColumnsToContents()
        else:
            self.table.setRowCount(0)
        
        # إضافة الجدول إلى التخطيط داخل الفريم
        data_frame_layout.addWidget(self.table)
        
        # تعيين التخطيط للفريم
        frame.setLayout(data_frame_layout)
        
        # إضافة الفريم إلى التخطيط الخارجي
        new_layout.addWidget(frame, 1, 0)
    






        
        #انشاء فريم للحفض الفريم الابيض الجانبي
        save_frame = QFrame()
        save_frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #1A3654;
        """)
        save_frame_layout = QGridLayout(save_frame)
        # save_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

       




        label = QLabel("")
        label.setStyleSheet('''
             background-color: #1A3654;
            font-family: Inter;
            font-size:20px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')

        save_frame_layout.addWidget(label,0,0)
        # 1,1 تعني العمود الثاني والصف الثاني

        # 2,1 تعني انهو ياخذ صفين الثاني والثالث وياخذ عمود واحد
        new_layout.addWidget(save_frame,1,1)


        
        
        # البحث في فريم الجانبي لل (save frame layout)

        label_history = QLabel("اسم المادة")
        label_history.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_history, 0, 1)

        self.name_of_mat = QLineEdit()
        self.name_of_mat.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.name_of_mat, 0, 0)



        
        # البحث في فريم الجانبي لل (save frame layout)

        label_history = QLabel("نوع المادة")
        label_history.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_history, 1, 1)

        self.type_of_mat = QLineEdit()
        self.type_of_mat.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.type_of_mat, 1, 0)

        ######
        
        
        # البحث في فريم الجانبي لل (save frame layout)

        label_number = QLabel("العدد")
        label_number.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_number, 2, 1)

        self.count_of_mat = QLineEdit()
        self.count_of_mat.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.count_of_mat, 2, 0)



        
        # البحث في فريم الجانبي لل (save frame layout)

        label_End_date = QLabel("تاريخ الانتهاء")
        label_End_date.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_End_date, 3, 1)

        self.expaier_of_mat = QDateEdit()
        # تعيين التاريخ الافتراضي ليكون تاريخ اليوم
        self.expaier_of_mat.setDate(QDate.currentDate())

        # تعيين تنسيق العرض ليشمل اليوم والشهر والسنة فقط
        self.expaier_of_mat.setDisplayFormat("dd/MM/yyyy")


        self.expaier_of_mat.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.expaier_of_mat, 3, 0)


        label_number = QLabel("السعر")
        label_number.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_number, 4, 1)

        self.price_of_mat = QLineEdit()
        self.price_of_mat.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.price_of_mat, 4, 0)


         #المجموع 
        button1 = QPushButton()
        button1.clicked.connect(self.send_data_to_controller)
        button1.setStyleSheet("""
                     QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                             
                               """)
        
        icon = QIcon('./static/Group 8 (1).png')  # تحميل الأيقونة
        button1.setIcon(icon)
        button1.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button1,5,0,1,2)
        




        button2 = QPushButton()
        button2.clicked.connect(self.controller.update_mat_show)
        button2.setStyleSheet("""
                     QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                             
                               """)
        
        icon = QIcon('./static/20.png')  # تحميل الأيقونة
        button2.setIcon(icon)
        button2.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button2,6,0,1,2)

        
        button3 = QPushButton()
        button3.clicked.connect(self.controller.del_mat_show)
        button3.setStyleSheet("""
                     QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                             
                               """)
        
        icon = QIcon('./static/14.png')  # تحميل الأيقونة
        button3.setIcon(icon)
        button3.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button3,7,0,1,2)


    def send_data_to_controller(self):
        # الحصول على البيانات من الواجهة
        name = self.name_of_mat.text()
        type = self.type_of_mat.text()
        count = self.count_of_mat.text()
        expaier = self.expaier_of_mat.date().toString('yyyy-MM-dd')
        price = self.price_of_mat.text()

        # إرسال البيانات إلى الكونترولر لإضافتها للنموذج
        self.controller.add_material_to_model(name, type, count, expaier, price)

        # تحديث الجدول بعد الحفظ
        self.refresh_table()

    def refresh_table(self):
        # استرجاع البيانات من النموذج عبر الكونترولر
        data_table = self.controller.get_material_from_model()

        # مسح البيانات القديمة في الجدول
        self.table.setRowCount(0)

        # تعبئة الجدول بالبيانات الجديدة
        if data_table and len(data_table[0]) > 0:
            row_count = len(data_table[0])  # افتراض أن جميع الأعمدة لها نفس الطول
            self.table.setRowCount(row_count)

            for row in range(row_count):
                self.table.setItem(row, 5, QTableWidgetItem(str(data_table[0][row])))  # إدخال الاسم
                self.table.setItem(row, 0, QTableWidgetItem(data_table[1][row]))  # إدخال الاسم
                self.table.setItem(row, 1, QTableWidgetItem(data_table[2][row]))  # إدخال النوع
                self.table.setItem(row, 2, QTableWidgetItem(str(data_table[3][row])))  # إدخال العدد
                self.table.setItem(row, 3, QTableWidgetItem(str(data_table[4][row])))  # إدخال تاريخ الانتهاء
                self.table.setItem(row, 4, QTableWidgetItem(str(data_table[5][row])))



        


        



        




class Closet(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("المخزن")
        self.resize(500, 500)


         
        # فريم جديد
        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
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
        # 1,2 لكي تاخذ صف واحد وعمودين الاول والثاني
        new_layout.addWidget(lest_label_frame, 0, 0, 1, 2)  # الهيدر 

        # فريم يحتوي على باقي العناصر مع Layout منفصل
        frame = QFrame()
        layout2 = QGridLayout(frame)
        new_layout.addWidget(frame, 1, 0, 1, 2)

        # إضافة أيقونة في Layout1 (Layout العنوان)
        icon_label = QLabel(lest_label_frame)
        icon = QIcon('./static/16.png')  
        icon_label.setPixmap(icon.pixmap(100, 100))  # تحديد حجم الأيقونة
        layout1.addWidget(icon_label)


         #انشاء فريم لوضع البيانات الفريم الابيض السفلي
        frame = QFrame()
        frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        frame.setFixedHeight(700)
        new_layout.addWidget(frame,1,0)
        frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        
        #انشاء فريم للحفض الفريم الابيض الجانبي
        save_frame = QFrame()
        save_frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #1A3654;
        """)
        save_frame_layout = QGridLayout(save_frame)
        # save_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

       




        label = QLabel("")
        label.setStyleSheet('''
             background-color: #1A3654;
            font-family: Inter;
            font-size:20px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')

        save_frame_layout.addWidget(label,0,0)
        # 1,1 تعني العمود الثاني والصف الثاني

        # 2,1 تعني انهو ياخذ صفين الثاني والثالث وياخذ عمود واحد
        new_layout.addWidget(save_frame,1,1)



        
        # البحث في فريم الجانبي لل (save frame layout)

        label_history = QLabel("البحث")
        label_history.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_history, 0, 1)

        history_input = QLineEdit()
        history_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(history_input, 0, 0)



        
        # البحث في فريم الجانبي لل (save frame layout)

        label_history = QLabel("النوع")
        label_history.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_history, 1, 1)

        history_input = QLineEdit()
        history_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(history_input, 1, 0)


        
        #المجموع 
        button3 = QPushButton()
        button3.setStyleSheet("""
                     QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                             
                               """)
        
        icon = QIcon('./static/14.png')  # تحميل الأيقونة
        button3.setIcon(icon)
        button3.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button3,2,0,1,2)
        







class Data_analysis(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("تحليل")
        self.resize(500, 500)




class DelMat(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("تعديل المادة")
        self.resize(300, 250)


         
        # فريم جديد
        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)


        label = QLabel('اكتب ترميز المنتج الذي تريد حذفه')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,0,1)

        self.id_mat = QLineEdit('')
        self.id_mat.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.id_mat,0,0)

        button1 = QPushButton()
        button1.clicked.connect(self.send_id_mat_to_controller)
        button1.setStyleSheet("""
                     QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                             
                               """)
        
        icon = QIcon('./static/14.png')  # تحميل الأيقونة
        button1.setIcon(icon)
        button1.setIconSize(QSize(90, 36))
        
        new_layout.addWidget(button1,1,0,1,2)

    def send_id_mat_to_controller(self):
        id_mat = self.id_mat.text()
        self.controller.del_material_from_model(id_mat)



class UpdateMat(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("حذف مادة")
        self.resize(300, 250)


         
        # فريم جديد
        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)


        label = QLabel('اكتب ترميز المنتج الذي تريد تعديله')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,0,1)

        self.id_mat = QLineEdit('')
        self.id_mat.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.id_mat,0,0)


        label = QLabel('اسم المادة')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,1,1)

        self.name_mat = QLineEdit('')
        self.name_mat.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.name_mat,1,0)
        

        label = QLabel('نوع المادة')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,2,1)



        self.type_mat = QLineEdit('')
        self.type_mat.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.type_mat,2,0)


        label = QLabel('السعر')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,3,1)



        self.price_mat = QLineEdit('')
        self.price_mat.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.price_mat,3,0)



        label = QLabel("تاريخ الانتهاء")
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,4,1)

        self.expaier_mat = QDateEdit()
        # تعيين التاريخ الافتراضي ليكون تاريخ اليوم
        self.expaier_mat.setDate(QDate.currentDate())

        # تعيين تنسيق العرض ليشمل اليوم والشهر والسنة فقط
        self.expaier_mat.setDisplayFormat("dd/MM/yyyy")


        self.expaier_mat.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.expaier_mat,4,0)



        button = QPushButton()
        button.clicked.connect(self.send_update_data_to_controller)
        button.setStyleSheet("""
                     QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                             
                               """)
        
        icon = QIcon('./static/20.png')  # تحميل الأيقونة
        button.setIcon(icon)
        button.setIconSize(QSize(90, 36))

        new_layout.addWidget(button,5,0,1,2)

    def send_update_data_to_controller(self):
        id_mat = self.id_mat.text()
        name = self.name_mat.text()
        type = self.type_mat.text()
        price = self.price_mat.text()
        expaier = self.expaier_mat.date().toString('yyyy-MM-dd')
        self.controller.update_material_to_model(id_mat, name, type, price, expaier)

        



class DelDefer(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("تعديل المادة")
        self.resize(300, 250)


        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)


        label = QLabel('اكتب ترميز المنتج الذي تريد حذفه')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,0,1)

        self.id_defe = QLineEdit('')
        self.id_defe.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.id_defe,0,0)

        button1 = QPushButton()
        button1.clicked.connect(self.send_id_defe_to_controller)
        button1.setStyleSheet("""
                     QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                             
                               """)
        
        icon = QIcon('./static/14.png')  # تحميل الأيقونة
        button1.setIcon(icon)
        button1.setIconSize(QSize(90, 36))
        
        new_layout.addWidget(button1,1,0,1,2)

    def send_id_defe_to_controller(self):
        id_defe = self.id_defe.text()
        self.controller.del_Deferred_from_model(id_defe)

        




class UpdateDefer(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("تعديل مادة")
        self.resize(300, 250)

        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)


        label = QLabel('اكتب ترميز المنتج الذي تريد تعديله')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,0,1)

        self.id_defe = QLineEdit('')
        self.id_defe.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.id_defe,0,0)


        label = QLabel('اسم العميل')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,1,1)

        self.customer_name = QLineEdit('')
        self.customer_name.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.customer_name,1,0)
        

        label = QLabel(' رقم الهاتف')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,2,1)



        self.phone_num= QLineEdit('')
        self.phone_num.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.phone_num,2,0)


        label = QLabel('العنوان')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,3,1)



        self.address = QLineEdit('')
        self.address.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.address,3,0)


        
        label = QLabel('السعر')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,4,1)



        self.price = QLineEdit('')
        self.price.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.price,4,0)





        button = QPushButton()
        button.clicked.connect(self.send_update_data_defer_to_controller)
        button.setStyleSheet("""
                     QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                             
                               """)
        
        icon = QIcon('./static/20.png')  # تحميل الأيقونة
        button.setIcon(icon)
        button.setIconSize(QSize(90, 36))

        new_layout.addWidget(button,5,0,1,2)


    def send_update_data_defer_to_controller(self):
        id_defe = self.id_defe.text()
        customer_name = self.customer_name.text()
        phone_num = self.phone_num.text()
        address = self.address.text()
        price = self.price.text()
        self.controller.update_Deferred_to_model(id_defe, customer_name, phone_num, address, price)

        
    
class DelListDetales(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("حذف تفاصيل الطلب")
        self.resize(300, 250)


        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)


        label = QLabel('اكتب ترميز المنتج الذي تريد حذفه')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,0,1)

        self.id_defe = QLineEdit('')
        self.id_defe.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.id_defe,0,0)

        button1 = QPushButton()
        button1.clicked.connect(self.send_id_defe_to_controller)
        button1.setStyleSheet("""
                     QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                             
                               """)
        
        icon = QIcon('./static/14.png')  # تحميل الأيقونة
        button1.setIcon(icon)
        button1.setIconSize(QSize(90, 36))
        
        new_layout.addWidget(button1,1,0,1,2)

    def send_id_defe_to_controller(self):
        id_defe = self.id_defe.text()
        self.controller.del_bill_detales_from_model(id_defe)


        

class Delpurc(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("حذف المادة")
        self.resize(300, 250)


         
        # فريم جديد
        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)


        label = QLabel('اكتب ترميز المنتج الذي تريد حذفه')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,0,1)

        self.purc_id = QLineEdit('')
        self.purc_id.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.purc_id,0,0)

        button1 = QPushButton()
        button1.clicked.connect(self.send_id_purc_to_controller)
        button1.setStyleSheet("""
                     QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                             
                               """)
        
        icon = QIcon('./static/14.png')  # تحميل الأيقونة
        button1.setIcon(icon)
        button1.setIconSize(QSize(90, 36))
        
        new_layout.addWidget(button1,1,0,1,2)

    def send_id_purc_to_controller(self):
        id_purc = self.purc_id.text()  # استخدم purc_id بدلاً من id_purc

        self.controller.del_purc_from_model(id_purc)


        
        
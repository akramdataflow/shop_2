import sys 
from PySide6.QtWidgets import QSpinBox, QMainWindow, QPushButton, QGridLayout, QFrame, QVBoxLayout, QLabel , QLineEdit , QSizePolicy
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import Qt, QSize


class MyView(QMainWindow):
    def __init__(self, controller=None):
        super().__init__()
        self.controller = controller

        self.setGeometry(100, 200, 800, 1000)

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
        button1.clicked.connect(controller.show_list)
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
        button1.setIconSize(QSize(250, 250))
        frame_layout.addWidget(button1, 0, 0)

        # Button 2
        button2 = QPushButton()
        button2.clicked.connect(controller.show_sales)
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
        button2.setIconSize(QSize(250, 250))
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
        button3.clicked.connect(controller.show_Purchases)
        button3.setIconSize(QSize(250, 250))
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
        button4.clicked.connect(controller.show_Deferred)
        button4.setIconSize(QSize(250, 250))
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
        button5.clicked.connect(controller.show_materials)
        button5.setIconSize(QSize(250, 250))
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
        button6.clicked.connect(controller.show_closet)       
        button6.setIconSize(QSize(250, 250))
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
        button7.clicked.connect(controller.show_closet) 
        button7.setIconSize(QSize(250, 250))
        frame_layout.addWidget(button7, 2, 0)


class Lists(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("القوائم")
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
        icon = QIcon('./static/12.png')  
        icon_label.setPixmap(icon.pixmap(100, 100))  # تحديد حجم الأيقونة
        layout1.addWidget(icon_label)



        
        #انشاء فريم لوضع البيانات الفريم الابيض السفلي
        frame = QFrame()
        frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
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
        button1.setIconSize(QSize(229, 62))
       
        save_frame_layout.addWidget(button1,0,0)
        


        
        button2 = QPushButton()
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



         #انشاء فريم لوضع البيانات الفريم الابيض السفلي
        frame = QFrame()
        frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
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

        #انشاء فريم لوضع البيانات الفريم الابيض السفلي
        frame = QFrame()
        frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(frame,2,0)
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
        new_layout.addWidget(save_frame,2,1)



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
        
        icon = QIcon('./static/Group 8 (1).png')  # تحميل الأيقونة
        button1.setIcon(icon)
        button1.setIconSize(QSize(90, 36))
       
        save_frame_layout.addWidget(button1,0,0)
       



        
        button2 = QPushButton()
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
        
        save_frame_layout.addWidget(button3,2,0)
        


        total_input = QLineEdit()
        total_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(total_input, 3, 0)

        












#4


class Deferred(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("دفع مؤجل")
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
        icon = QIcon('./static/15.png')  
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

        history_input = QLineEdit()
        history_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(history_input, 0, 0)



        
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

        history_input = QLineEdit()
        history_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(history_input, 1, 0)

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

        number_input = QLineEdit()
        number_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(number_input, 2, 0)



        
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

        End_date_input = QLineEdit()
        End_date_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(End_date_input, 3, 0)


         #المجموع 
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
        
        icon = QIcon('./static/Group 8 (1).png')  # تحميل الأيقونة
        button1.setIcon(icon)
        button1.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button1,4,0,1,2)



        button2 = QPushButton()
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




class  Materials(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("اضافة مواد")
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
        icon = QIcon('./static/17.png')  
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

        history_input = QLineEdit()
        history_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(history_input, 0, 0)



        
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

        history_input = QLineEdit()
        history_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(history_input, 1, 0)

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

        number_input = QLineEdit()
        number_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(number_input, 2, 0)



        
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

        End_date_input = QLineEdit()
        End_date_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(End_date_input, 3, 0)


         #المجموع 
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
        
        icon = QIcon('./static/Group 8 (1).png')  # تحميل الأيقونة
        button1.setIcon(icon)
        button1.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button1,4,0,1,2)



        button2 = QPushButton()
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


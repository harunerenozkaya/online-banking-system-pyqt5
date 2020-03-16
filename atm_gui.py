from PyQt5.QtWidgets import QWidget, QLabel , QPushButton , QLineEdit , QMessageBox
from PyQt5.QtGui import QBitmap, QIcon , QPixmap
from PyQt5 import QtCore
from PyQt5.Qt import QCursor , QIntValidator ,QSize , QShortcut , QKeySequence
from PyQt5 import Qt

class Atm_Gui(object):
  
        def SetupGui(self,MainWindow):
                MainWindow.setObjectName("MainWindow")

                
                self.setFixedSize(450,700)
                self.setWindowTitle("Online Bank System")
                self.setWindowIcon(QIcon("bank-logo.png"))

                ##################
                ## Login Screen ##
                ##################


                self.w_login_screen = QWidget(self)
                self.w_login_screen.setGeometry(0,0,450,700)
                self.w_login_screen.setStyleSheet("background-color: rgb(233,233,233)")
                
                self.lbl_login_logo = QLabel(self.w_login_screen)
                self.lbl_login_logo.setGeometry(75,10,250,250)
                self.lbl_login_logo.setPixmap(QPixmap("bank-logo.png").scaled(300,300))
                

                self.le_login_ctz_number_bar = QLineEdit(self.w_login_screen)
                self.le_login_ctz_number_bar.setGeometry(60,300,330,30)
                self.le_login_ctz_number_bar.setPlaceholderText("Citizenship Number")
                self.le_login_ctz_number_bar.setStyleSheet("""  QLineEdit { background:white; 
                                                                        border-width: 1px;
                                                                        border-style: solid;
                                                                        border-radius: 10px;
                                                                        }
                                                                        
                                                                        """)

                self.le_login_password_bar = QLineEdit(self.w_login_screen)
                self.le_login_password_bar.setGeometry(60,350,330,30)
                self.le_login_password_bar.setPlaceholderText("Password")
                self.le_login_password_bar.setEchoMode(QLineEdit.Password)
                self.le_login_password_bar.setStyleSheet("""  QLineEdit {   background:white; 
                                                                        border-width: 1px;
                                                                        border-style: solid;
                                                                        border-radius: 10px;
                                                                        
                                                                        }
                                                                        
                                                                        """)

                self.btn_login_button = QPushButton("Login",self.w_login_screen)
                self.btn_login_button.setGeometry(155,400,130,30)
                self.btn_login_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
                self.btn_login_button.setStyleSheet(""" QPushButton {  
                                                                color:white;
                                                                font-family : "Arial"; 
                                                                font-size:15px; 
                                                                font-weight:bold;   
                                                                background-color: rgb(112,108,97);
                                                                border-width: 3px;
                                                                border-color:black;
                                                                border-style: solid;
                                                                border-radius: 10px; }

                                                        QPushButton:hover {
                                                                border-width: 5px;
                                                                border-color:black;
                                                                border-style: solid;
                                                                border-radius: 10px
                                                                                
                                                        }

                                                        QPushButton:pressed {
                                                                border-color:black;  
                                                                font-style : italic;                 
                                                        }
                                                                """)
                
                
                self.lbl_login_text_create_account = QLabel("Don't you have any account ?",self.w_login_screen)
                self.lbl_login_text_create_account.setGeometry(140,480,180,30)

                self.btn_signup_button = QPushButton("Sign Up",self.w_login_screen)
                self.btn_signup_button.setGeometry(155,520,130,30)
                self.btn_signup_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
                self.btn_signup_button.setStyleSheet(""" QPushButton {  
                                                                color:white;
                                                                font-family : "Arial"; 
                                                                font-size:15px; 
                                                                font-weight:bold;   
                                                                background-color: rgb(112,108,97);
                                                                border-width: 3px;
                                                                border-color:black;
                                                                border-style: solid;
                                                                border-radius: 10px; }

                                                        QPushButton:hover {
                                                                border-width: 5px;
                                                                border-color:black;
                                                                border-style: solid;
                                                                border-radius: 10px
                                                                                
                                                        }

                                                        QPushButton:pressed {
                                                                border-color:black;  
                                                                font-style : italic;                 
                                                        }
                                                                """)

                self.lbl_dev_sign = QLabel("Dev.Harun Eren Özkaya",self.w_login_screen)
                self.lbl_dev_sign.setGeometry(155,670,150,20)
                self.lbl_dev_sign.setStyleSheet(""" QLabel{  
                                                        font-style:italic;
                                                        text-decoration : underline;

                                                                }    """)

                #####################
                ## Register Screen ##
                #####################

                self.w_register_screen = QWidget(self)
                self.w_register_screen.setGeometry(0,0,450,700)
                self.w_register_screen.setStyleSheet("background-color: rgb(233,233,233)")
                self.w_register_screen.hide()

                
                self.lbl_register_logo = QLabel(self.w_register_screen)
                self.lbl_register_logo.setGeometry(75,10,250,250)
                self.lbl_register_logo.setPixmap(QPixmap("bank-logo.png").scaled(300,300))

                self.le_register_ctz_number_bar = QLineEdit(self.w_register_screen)
                self.le_register_ctz_number_bar.setGeometry(60,300,330,30)
                self.le_register_ctz_number_bar.setPlaceholderText("Citizenship Number")
                self.le_register_ctz_number_bar.setStyleSheet("""  QLineEdit { background:white; 
                                                                        border-width: 1px;
                                                                        border-style: solid;
                                                                        border-radius: 10px;}
                                                                        
                                                                        """)

                self.le_register_name_bar = QLineEdit(self.w_register_screen)
                self.le_register_name_bar.setGeometry(60,350,330,30)
                self.le_register_name_bar.setPlaceholderText("Name")
                self.le_register_name_bar.setStyleSheet("""  QLineEdit {   background:white; 
                                                                        border-width: 1px;
                                                                        border-style: solid;
                                                                        border-radius: 10px;
                                                                        
                                                                        }
                                                                        
                                                                        """)

                self.le_register_surname_bar = QLineEdit(self.w_register_screen)
                self.le_register_surname_bar.setGeometry(60,400,330,30)
                self.le_register_surname_bar.setPlaceholderText("Surname")
                self.le_register_surname_bar.setStyleSheet("""  QLineEdit {   background:white; 
                                                                        border-width: 1px;
                                                                        border-style: solid;
                                                                        border-radius: 10px;
                                                                        
                                                                        }
                                                                        
                                                                        """)
                self.le_register_age_bar = QLineEdit(self.w_register_screen)
                self.le_register_age_bar.setGeometry(60,450,330,30)
                self.le_register_age_bar.setValidator(QIntValidator(0,200))
                self.le_register_age_bar.setPlaceholderText("Age")
                self.le_register_age_bar.setStyleSheet("""  QLineEdit {   background:white; 
                                                                        border-width: 1px;
                                                                        border-style: solid;
                                                                        border-radius: 10px;
                                                                        
                                                                        }
                                                                        
                                                                        """)

                self.le_register_birthdate_bar = QLineEdit(self.w_register_screen)
                self.le_register_birthdate_bar.setGeometry(60,500,330,30)
                self.le_register_birthdate_bar.setPlaceholderText("Birth Date (YYYY-MM-DD)")
                self.le_register_birthdate_bar.setStyleSheet("""  QLineEdit {   background:white; 
                                                                        border-width: 1px;
                                                                        border-style: solid;
                                                                        border-radius: 10px;
                                                                        
                                                                        }
                                                                        
                                                                        """)

                
                self.le_register_password_bar = QLineEdit(self.w_register_screen)
                self.le_register_password_bar.setGeometry(60,550,330,30)
                self.le_register_password_bar.setPlaceholderText("Password")
                self.le_register_password_bar.setEchoMode(QLineEdit.Password)
                self.le_register_password_bar.setStyleSheet("""  QLineEdit {   background:white; 
                                                                        border-width: 1px;
                                                                        border-style: solid;
                                                                        border-radius: 10px;
                                                                        
                                                                        }
                                                                        
                                                                        """)


                self.btn_signup_register_button = QPushButton("Sign Up",self.w_register_screen)
                self.btn_signup_register_button.setGeometry(155,600,130,30)
                self.btn_signup_register_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
                self.btn_signup_register_button.setStyleSheet(""" QPushButton {  
                                                                color:white;
                                                                font-family : "Arial"; 
                                                                font-size:15px; 
                                                                font-weight:bold;   
                                                                background-color:rgb(112,108,97);
                                                                border-width: 3px;
                                                                border-color:black;
                                                                border-style: solid;
                                                                border-radius: 10px; }

                                                        QPushButton:hover {
                                                                border-width: 5px;
                                                                border-color:black;
                                                                border-style: solid;
                                                                border-radius: 10px
                                                                                
                                                        }

                                                        QPushButton:pressed {
                                                                border-color:black;  
                                                                font-style : italic;                 
                                                        }
                                                                """)


                self.lbl_register_dev_sign = QLabel("Dev.Harun Eren Özkaya",self.w_register_screen)
                self.lbl_register_dev_sign.setGeometry(155,670,150,20)
                self.lbl_register_dev_sign.setStyleSheet(""" QLabel{  
                                                        font-style:italic;
                                                        text-decoration : underline;

                                                                }    """)

                self.btn_back_to_login_screen = QPushButton(self.w_register_screen)
                self.btn_back_to_login_screen.setGeometry(20,650,30,30)
                self.btn_back_to_login_screen.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
                self.btn_back_to_login_screen.setIcon(QIcon("backarrow.png"))
                self.btn_back_to_login_screen.setStyleSheet(""" QPushButton {  
                                                                border-width: 10px;
                                                                border-style: solid;
                                                                
                                                                qproperty-iconSize: 32px 32px;
                                                                }
                                                                

                                                        QPushButton:hover {

                                                                qproperty-icon: url("/backrow_hover.png");
                                                                
                                                                                
                                                        }

                                                        QPushButton:pressed {

                                                                qproperty-iconSize: 200px 200px;

                                                        }
                                                                """)




                #################
                ## Main Screen ##
                #################

                self.w_main_screen = QWidget(self)
                self.w_main_screen.setGeometry(0,0,450,700)
                self.w_main_screen.setStyleSheet("background:rgb(233,233,233);")
                self.w_main_screen.hide()

                self.lbl_top_banner_main = QLabel(self.w_main_screen)
                self.lbl_top_banner_main.setGeometry(0,0,450,60)
                self.lbl_top_banner_main.setStyleSheet("background:black;")

                self.lbl_bottom_banner_main = QLabel(self.w_main_screen)
                self.lbl_bottom_banner_main.setGeometry(0,640,450,60)
                self.lbl_bottom_banner_main.setStyleSheet("background:black;")

                ## TOP BANNER

                self.lbl_person_logo = QLabel(self.w_main_screen)
                self.lbl_person_logo.setGeometry(5,5,20,20)
                self.lbl_person_logo.setPixmap(QPixmap("person_logo.png").scaled(20,20))
                self.lbl_person_logo.setStyleSheet("background:black;")

                self.lbl_user_name_text = QLabel(self.w_main_screen)
                self.lbl_user_name_text.setGeometry(30,5,150,20)
                self.lbl_user_name_text.setStyleSheet("background:black; color:white; font-size:15px;")

                self.lbl_user_id_text = QLabel(self.w_main_screen)
                self.lbl_user_id_text.setGeometry(7,27,175,20)
                self.lbl_user_id_text.setStyleSheet("background:black; color:white;")

                self.lbl_balance_logo = QLabel(self.w_main_screen)
                self.lbl_balance_logo.setGeometry(425,5,20,20)
                self.lbl_balance_logo.setPixmap(QPixmap("balance_logo.png").scaled(20,20))
                self.lbl_balance_logo.setStyleSheet("background : black;")

                self.lbl_loan_logo = QLabel(self.w_main_screen)
                self.lbl_loan_logo.setGeometry(425,35,20,20)
                self.lbl_loan_logo.setPixmap(QPixmap("loan_logo.png").scaled(20,20))
                self.lbl_loan_logo.setStyleSheet("background : black;")

                self.lbl_balance_text = QLabel(self.w_main_screen)
                self.lbl_balance_text.setGeometry(270,5,150,20)
                self.lbl_balance_text.setStyleSheet("background:black; font-size:20px; color:white;")
                self.lbl_balance_text.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

                self.lbl_loan_text = QLabel(self.w_main_screen)
                self.lbl_loan_text.setGeometry(270,35,150,20)
                self.lbl_loan_text.setStyleSheet("background:black; font-size:20px; color:white;")
                self.lbl_loan_text.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                
                ## BOTTOM BANNER

                self.lbl_app_logo_main = QLabel(self.w_main_screen)
                self.lbl_app_logo_main.setGeometry(190,640,60,60)
                self.lbl_app_logo_main.setPixmap(QPixmap("bank-logo_white.png").scaled(70,70))
                self.lbl_app_logo_main.setStyleSheet("background-color:black;")

                self.btn_exit = QPushButton(self.w_main_screen)
                self.btn_exit.setStyleSheet("""QPushButton {
                                                                        background:black;
                                                                        border-style:solid;
                                                                        border-width: 0px;
                                                                        }""")
                self.btn_exit.setGeometry(10,645,50,50)
                self.btn_exit.setIcon(QIcon("exit_logo.png"))
                self.btn_exit.setIconSize(QSize(50,50))
                self.btn_exit.setCursor(QCursor(QtCore.Qt.PointingHandCursor))


                self.btn_settings = QPushButton(self.w_main_screen)
                self.btn_settings.setStyleSheet("background:black;")
                self.btn_settings.setGeometry(380,645,50,50)
                self.btn_settings.setIcon(QIcon("setting_logo.png"))
                self.btn_settings.setIconSize(QSize(50,50))
                self.btn_settings.setCursor(QCursor(QtCore.Qt.PointingHandCursor))


                ## MIDDLE AREA

                self.btn_money_withdraw = QPushButton("Withdraw Money",self.w_main_screen)
                self.btn_money_withdraw.setGeometry(85,115,280,70)
                self.btn_money_withdraw.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
                self.btn_money_withdraw.setStyleSheet("""QPushButton {  color:white;
                                                                        font-size:20px;
                                                                        border-radius:10px;
                                                                        border-style:solid;
                                                                        border-width:5px;
                                                                        border-color:black;
                                                                        background-color: rgb(112,108,97);
                                                                        }
                                                                        
                                                                        
                                                        QPushButton:hover {               
                                                                        border-radius:10px;
                                                                        border-style:solid;
                                                                        border-width:7px;
                                                                        border-color:black;  


                                                                        
                                                                       } """)



                self.btn_money_deposit = QPushButton("Deposit Money",self.w_main_screen)
                self.btn_money_deposit.setGeometry(85,215,280,70)
                self.btn_money_deposit.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
                self.btn_money_deposit.setStyleSheet("""QPushButton {  color:white;
                                                                        font-size:20px;
                                                                        border-radius:10px;
                                                                        border-style:solid;
                                                                        border-width:5px;
                                                                        border-color:black;
                                                                        background-color: rgb(112,108,97);
                                                                        }
                                                                        
                                                                        
                                                        QPushButton:hover {               
                                                                        border-radius:10px;
                                                                        border-style:solid;
                                                                        border-width:7px;
                                                                        border-color:black;  


                                                                        
                                                                       }                        """)



                self.btn_money_transfer = QPushButton("Money Transfer",self.w_main_screen)
                self.btn_money_transfer.setGeometry(85,315,280,70)
                self.btn_money_transfer.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
                self.btn_money_transfer.setStyleSheet("""       QPushButton {  color:white;
                                                                        font-size:20px;
                                                                        border-radius:10px;
                                                                        border-style:solid;
                                                                        border-width:5px;
                                                                        border-color:black;
                                                                        background-color: rgb(112,108,97);
                                                                        }       
                                                                        
                                                                QPushButton:hover {               
                                                                        border-radius:10px;
                                                                        border-style:solid;
                                                                        border-width:7px;
                                                                        border-color:black;  
                                                                        
                                                                       }        
                                                                        
                                                                        """)



                self.btn_take_credit = QPushButton("Take Credit",self.w_main_screen)
                self.btn_take_credit.setGeometry(85,415,280,70)
                self.btn_take_credit.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
                self.btn_take_credit.setStyleSheet("""  QPushButton {  color:white;
                                                                        font-size:20px;
                                                                        border-radius:10px;
                                                                        border-style:solid;
                                                                        border-width:5px;
                                                                        border-color:black;
                                                                        background-color: rgb(112,108,97);
                                                                        }
                                                                        
                                                        QPushButton:hover {               
                                                                        border-radius:10px;
                                                                        border-style:solid;
                                                                        border-width:7px;
                                                                        border-color:black;  

                                                                        
                                                                       }                
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        """)



                self.btn_close_credit = QPushButton("Close Credit",self.w_main_screen)
                self.btn_close_credit.setGeometry(85,515,280,70)
                self.btn_close_credit.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
                self.btn_close_credit.setStyleSheet(""" QPushButton {  color:white;
                                                                        font-size:20px;
                                                                        border-radius:10px;
                                                                        border-style:solid;
                                                                        border-width:5px;
                                                                        border-color:black;
                                                                        background-color: rgb(112,108,97);
                                                                        }
                                                                        
                                                                        
                                                        QPushButton:hover {               
                                                                        border-radius:10px;
                                                                        border-style:solid;
                                                                        border-width:7px;
                                                                        border-color:black;  

                                                                        
                                                                       }                
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        """)



                ####################
                ## WITHDRAW MONEY ##
                ####################

                self.w_withdraw_money = QWidget(self.w_main_screen)
                self.w_withdraw_money.setGeometry(0,60,450,580)
                self.w_withdraw_money.setStyleSheet("background-color:rgb(233,233,233);")
                self.w_withdraw_money.hide()

                self.lbl_withdraw_text = QLabel("Withdraw Money",self.w_withdraw_money)
                self.lbl_withdraw_text.setStyleSheet("font-size :40px;")
                self.lbl_withdraw_text.setGeometry(75,10,300,50)
                
                self.btn_back_from_wth_to_main = QPushButton(self.w_withdraw_money)
                self.btn_back_from_wth_to_main.setIcon(QIcon("backarrow.png"))
                self.btn_back_from_wth_to_main.setGeometry(15,520,40,40)
                self.btn_back_from_wth_to_main.setIconSize(QSize(40,40))
                self.btn_back_from_wth_to_main.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
                self.btn_back_from_wth_to_main.setStyleSheet("border-width:3px; border-style:solid; border-color:black;")

                self.le_withdraw_money_amount = QLineEdit(self.w_withdraw_money)
                self.le_withdraw_money_amount.setGeometry(75,220,300,50)
                self.le_withdraw_money_amount.setPlaceholderText("Money Amount")
                self.le_withdraw_money_amount.setValidator(QIntValidator(0,99999999))
                self.le_withdraw_money_amount.setStyleSheet("""  QLineEdit {
                                                                        border-color:black;
                                                                        border-width:3px;
                                                                        border-style:solid;
                                                                        border-radius:15px;
                                                                        background:white;



                                                                       } """)

                self.btn_withdraw_okay = QPushButton("Withdraw",self.w_withdraw_money)
                self.btn_withdraw_okay.setGeometry(175,285,100,40)
                self.btn_withdraw_okay.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
                self.btn_withdraw_okay.setStyleSheet("""QPushButton {  color:white;
                                                                        font-size:15px;
                                                                        border-radius:10px;
                                                                        border-style:solid;
                                                                        border-width:3px;
                                                                        border-color:black;
                                                                        background-color: rgb(112,108,97);
                                                                        }
                                                                        
                                                                        
                                                        QPushButton:hover {               
                                                                        border-radius:10px;
                                                                        border-style:solid;
                                                                        border-width:5px;
                                                                        border-color:black;  


                                                                        
                                                                       } """)

                ####################
                ## DEPOSIT MONEY ##
                ####################

                self.w_deposit_money = QWidget(self.w_main_screen)
                self.w_deposit_money.setGeometry(0,60,450,580)
                self.w_deposit_money.setStyleSheet("background-color:rgb(233,233,233);")
                self.w_deposit_money.hide()

                self.lbl_deposit_text = QLabel("Deposit Money",self.w_deposit_money)
                self.lbl_deposit_text.setStyleSheet("font-size :40px;")
                self.lbl_deposit_text.setGeometry(90,10,300,50)
                
                self.btn_back_from_dpst_to_main = QPushButton(self.w_deposit_money)
                self.btn_back_from_dpst_to_main.setIcon(QIcon("backarrow.png"))
                self.btn_back_from_dpst_to_main.setGeometry(15,520,40,40)
                self.btn_back_from_dpst_to_main.setIconSize(QSize(40,40))
                self.btn_back_from_dpst_to_main.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
                self.btn_back_from_dpst_to_main.setStyleSheet("border-width:3px; border-style:solid; border-color:black;")

                self.le_deposit_money_amount = QLineEdit(self.w_deposit_money)
                self.le_deposit_money_amount.setGeometry(75,220,300,50)
                self.le_deposit_money_amount.setPlaceholderText("Money Amount")
                self.le_deposit_money_amount.setValidator(QIntValidator(0,99999999))
                self.le_deposit_money_amount.setStyleSheet("""  QLineEdit {
                                                                        border-color:black;
                                                                        border-width:3px;
                                                                        border-style:solid;
                                                                        border-radius:15px;
                                                                        background:white;



                                                                       } """)

                self.btn_deposit_okay = QPushButton("Deposit",self.w_deposit_money)
                self.btn_deposit_okay.setGeometry(175,285,100,40)
                self.btn_deposit_okay.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
                self.btn_deposit_okay.setStyleSheet("""QPushButton {  color:white;
                                                                        font-size:15px;
                                                                        border-radius:10px;
                                                                        border-style:solid;
                                                                        border-width:3px;
                                                                        border-color:black;
                                                                        background-color: rgb(112,108,97);
                                                                        }
                                                                        
                                                                        
                                                        QPushButton:hover {               
                                                                        border-radius:10px;
                                                                        border-style:solid;
                                                                        border-width:5px;
                                                                        border-color:black;  


                                                                        
                                                                       } """)

          
                ####################
                ## MONEY TRANSFER ##
                ####################

                self.w_money_transfer = QWidget(self.w_main_screen)
                self.w_money_transfer.setGeometry(0,60,450,580)
                self.w_money_transfer.setStyleSheet("background-color:rgb(233,233,233);")
                self.w_money_transfer.hide()

                self.lbl_moneytransfer_text = QLabel("Money Transfer",self.w_money_transfer)
                self.lbl_moneytransfer_text.setStyleSheet("font-size :40px;")
                self.lbl_moneytransfer_text.setGeometry(85,10,300,50)
                
                self.btn_back_from_mts_to_main = QPushButton(self.w_money_transfer)
                self.btn_back_from_mts_to_main.setIcon(QIcon("backarrow.png"))
                self.btn_back_from_mts_to_main.setGeometry(15,520,40,40)
                self.btn_back_from_mts_to_main.setIconSize(QSize(40,40))
                self.btn_back_from_mts_to_main.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
                self.btn_back_from_mts_to_main.setStyleSheet("border-width:3px; border-style:solid; border-color:black;")

                self.le_transfer_money_amount = QLineEdit(self.w_money_transfer)
                self.le_transfer_money_amount.setGeometry(75,220,300,50)
                self.le_transfer_money_amount.setPlaceholderText("Money Amount")
                self.le_transfer_money_amount.setValidator(QIntValidator(0,99999999))
                self.le_transfer_money_amount.setStyleSheet("""  QLineEdit {
                                                                        border-color:black;
                                                                        border-width:3px;
                                                                        border-style:solid;
                                                                        border-radius:15px;
                                                                        background:white;

                                                                       } """)

                self.le_transfer_money_id = QLineEdit(self.w_money_transfer)
                self.le_transfer_money_id.setGeometry(75,160,300,50)
                self.le_transfer_money_id.setPlaceholderText("Recipient ID")
                self.le_transfer_money_id.setStyleSheet("""  QLineEdit {
                                                                        border-color:black;
                                                                        border-width:3px;
                                                                        border-style:solid;
                                                                        border-radius:15px;
                                                                        background:white;

                                                                       } """)


                self.btn_transfer_okay = QPushButton("Transfer",self.w_money_transfer)
                self.btn_transfer_okay.setGeometry(175,285,100,40)
                self.btn_transfer_okay.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
                self.btn_transfer_okay.setStyleSheet("""QPushButton {  color:white;
                                                                        font-size:15px;
                                                                        border-radius:10px;
                                                                        border-style:solid;
                                                                        border-width:3px;
                                                                        border-color:black;
                                                                        background-color: rgb(112,108,97);
                                                                        }
                                                                        
                                                                        
                                                        QPushButton:hover {               
                                                                        border-radius:10px;
                                                                        border-style:solid;
                                                                        border-width:5px;
                                                                        border-color:black;  


                                                                        
                                                                       } """)

                ####################
                ## TAKE CREDIT ##
                ####################

                self.w_take_credit = QWidget(self.w_main_screen)
                self.w_take_credit.setGeometry(0,60,450,580)
                self.w_take_credit.setStyleSheet("background-color:rgb(233,233,233);")
                self.w_take_credit.hide()

                self.lbl_takecredit_text = QLabel("Take Credit",self.w_take_credit)
                self.lbl_takecredit_text.setStyleSheet("font-size :40px;")
                self.lbl_takecredit_text.setGeometry(120,10,300,50)
                
                self.btn_back_from_tcrdt_to_main = QPushButton(self.w_take_credit)
                self.btn_back_from_tcrdt_to_main.setIcon(QIcon("backarrow.png"))
                self.btn_back_from_tcrdt_to_main.setGeometry(15,520,40,40)
                self.btn_back_from_tcrdt_to_main.setIconSize(QSize(40,40))
                self.btn_back_from_tcrdt_to_main.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
                self.btn_back_from_tcrdt_to_main.setStyleSheet("border-width:3px; border-style:solid; border-color:black;")

                self.le_take_credit_amount = QLineEdit(self.w_take_credit)
                self.le_take_credit_amount.setGeometry(75,160,300,50)
                self.le_take_credit_amount.setPlaceholderText("Credit Amount")
                self.le_take_credit_amount.setValidator(QIntValidator(0,99999999))
                self.le_take_credit_amount.setStyleSheet("""  QLineEdit {
                                                                        border-color:black;
                                                                        border-width:3px;
                                                                        border-style:solid;
                                                                        border-radius:15px;
                                                                        background:white;

                                                                       } """)

                self.le_loan_amount = QLineEdit(self.w_take_credit)
                self.le_loan_amount.setGeometry(75,220,300,50)
                self.le_loan_amount.setPlaceholderText("Loan")
                self.le_loan_amount.setReadOnly(True)
                self.le_loan_amount.setStyleSheet("""  QLineEdit {
                                                                        border-color:black;
                                                                        border-width:3px;
                                                                        border-style:solid;
                                                                        border-radius:15px;
                                                                        background:white;

                                                                       } """)


                self.btn_take_credit_okay = QPushButton("Take Credit",self.w_take_credit)
                self.btn_take_credit_okay.setGeometry(175,285,100,40)
                self.btn_take_credit_okay.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
                self.btn_take_credit_okay.setStyleSheet("""QPushButton {  color:white;
                                                                        font-size:15px;
                                                                        border-radius:10px;
                                                                        border-style:solid;
                                                                        border-width:3px;
                                                                        border-color:black;
                                                                        background-color: rgb(112,108,97);
                                                                        }
                                                                        
                                                                        
                                                        QPushButton:hover {               
                                                                        border-radius:10px;
                                                                        border-style:solid;
                                                                        border-width:5px;
                                                                        border-color:black;  


                                                                        
                                                                       } """)

                ####################
                ## CLOSE CREDIT ##
                ####################

                self.w_close_credit = QWidget(self.w_main_screen)
                self.w_close_credit.setGeometry(0,60,450,580)
                self.w_close_credit.setStyleSheet("background-color:rgb(233,233,233);")
                self.w_close_credit.hide()

                self.lbl_closecredit_text = QLabel("Close Credit",self.w_close_credit)
                self.lbl_closecredit_text.setStyleSheet("font-size :40px;")
                self.lbl_closecredit_text.setGeometry(120,10,300,50)
                
                self.btn_back_from_clscrdt_to_main = QPushButton(self.w_close_credit)
                self.btn_back_from_clscrdt_to_main.setIcon(QIcon("backarrow.png"))
                self.btn_back_from_clscrdt_to_main.setGeometry(15,520,40,40)
                self.btn_back_from_clscrdt_to_main.setIconSize(QSize(40,40))
                self.btn_back_from_clscrdt_to_main.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
                self.btn_back_from_clscrdt_to_main.setStyleSheet("border-width:3px; border-style:solid; border-color:black;")

                self.le_close_credit_amount = QLineEdit(self.w_close_credit)
                self.le_close_credit_amount.setGeometry(75,220,300,50)
                self.le_close_credit_amount.setPlaceholderText("Money Amount")
                self.le_close_credit_amount.setValidator(QIntValidator(0,99999999))
                self.le_close_credit_amount.setStyleSheet("""  QLineEdit {
                                                                        border-color:black;
                                                                        border-width:3px;
                                                                        border-style:solid;
                                                                        border-radius:15px;
                                                                        background:white;



                                                                       } """)

                self.btn_close_credit_okay = QPushButton("Close Credit",self.w_close_credit)
                self.btn_close_credit_okay.setGeometry(175,285,100,40)
                self.btn_close_credit_okay.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
                self.btn_close_credit_okay.setStyleSheet("""QPushButton {  color:white;
                                                                        font-size:15px;
                                                                        border-radius:10px;
                                                                        border-style:solid;
                                                                        border-width:3px;
                                                                        border-color:black;
                                                                        background-color: rgb(112,108,97);
                                                                        }
                                                                        
                                                                        
                                                        QPushButton:hover {               
                                                                        border-radius:10px;
                                                                        border-style:solid;
                                                                        border-width:5px;
                                                                        border-color:black;  


                                                                        
                                                                       } """)

                


                ####################
                ##    SETTINGS    ##
                ####################

                self.w_setting = QWidget(self.w_main_screen)
                self.w_setting.setGeometry(0,60,450,580)
                self.w_setting.setStyleSheet("background-color:rgb(233,233,233);")
                self.w_setting.hide()

                self.lbl_setting_text = QLabel("Settings",self.w_setting)
                self.lbl_setting_text.setStyleSheet("font-size :40px;")
                self.lbl_setting_text.setGeometry(150,10,300,50)
                
                self.btn_back_from_setting_to_main = QPushButton(self.w_setting)
                self.btn_back_from_setting_to_main.setIcon(QIcon("backarrow.png"))
                self.btn_back_from_setting_to_main.setGeometry(15,520,40,40)
                self.btn_back_from_setting_to_main.setIconSize(QSize(40,40))
                self.btn_back_from_setting_to_main.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
                self.btn_back_from_setting_to_main.setStyleSheet("border-width:3px; border-style:solid; border-color:black;")

                self.btn_change_password = QPushButton("Change Password",self.w_setting)
                self.btn_change_password.setGeometry(85,155,280,70)
                self.btn_change_password.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
                self.btn_change_password.setStyleSheet("""QPushButton {  color:white;
                                                                        font-size:20px;
                                                                        border-radius:10px;
                                                                        border-style:solid;
                                                                        border-width:5px;
                                                                        border-color:black;
                                                                        background-color: rgb(112,108,97);
                                                                        }
                                                                        
                                                                        
                                                        QPushButton:hover {               
                                                                        border-radius:10px;
                                                                        border-style:solid;
                                                                        border-width:7px;
                                                                        border-color:black;  


                                                                        
                                                                       } """)



                self.btn_delete_account = QPushButton("Delete Account",self.w_setting)
                self.btn_delete_account.setGeometry(85,275,280,70)
                self.btn_delete_account.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
                self.btn_delete_account.setStyleSheet("""QPushButton {  color:white;
                                                                        font-size:20px;
                                                                        border-radius:10px;
                                                                        border-style:solid;
                                                                        border-width:5px;
                                                                        border-color:black;
                                                                        background-color: rgb(112,108,97);
                                                                        }
                                                                        
                                                                        
                                                        QPushButton:hover {               
                                                                        border-radius:10px;
                                                                        border-style:solid;
                                                                        border-width:7px;
                                                                        border-color:black;  


                                                                        
                                                                       }                        """)
                
                ##########################
                ##    DELETE ACCOUNT    ##
                ##########################

                self.w_delete_account = QWidget(self.w_main_screen)
                self.w_delete_account.setGeometry(0,60,450,580)
                self.w_delete_account.setStyleSheet("background-color:rgb(233,233,233);")
                self.w_delete_account.hide()

                self.lbl_delete_account_text = QLabel("Delete Account",self.w_delete_account)
                self.lbl_delete_account_text.setStyleSheet("font-size :40px;")
                self.lbl_delete_account_text.setGeometry(95,10,300,50)
                
                self.btn_back_from_dltaccnt_to_main = QPushButton(self.w_delete_account)
                self.btn_back_from_dltaccnt_to_main.setIcon(QIcon("backarrow.png"))
                self.btn_back_from_dltaccnt_to_main.setGeometry(15,520,40,40)
                self.btn_back_from_dltaccnt_to_main.setIconSize(QSize(40,40))
                self.btn_back_from_dltaccnt_to_main.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
                self.btn_back_from_dltaccnt_to_main.setStyleSheet("border-width:3px; border-style:solid; border-color:black;")

                self.le_delete_ctnumber = QLineEdit(self.w_delete_account)
                self.le_delete_ctnumber.setGeometry(75,160,300,50)
                self.le_delete_ctnumber.setPlaceholderText("Citizenship Number")
                self.le_delete_ctnumber.setStyleSheet("""  QLineEdit {
                                                                        border-color:black;
                                                                        border-width:3px;
                                                                        border-style:solid;
                                                                        border-radius:15px;
                                                                        background:white;

                                                                       } """)

                self.le_delete_password = QLineEdit(self.w_delete_account)
                self.le_delete_password.setGeometry(75,220,300,50)
                self.le_delete_password.setEchoMode(QLineEdit.Password)
                self.le_delete_password.setPlaceholderText("Password")
                self.le_delete_password.setStyleSheet("""  QLineEdit {
                                                                        border-color:black;
                                                                        border-width:3px;
                                                                        border-style:solid;
                                                                        border-radius:15px;
                                                                        background:white;

                                                                       } """)


                self.btn_delete_account_okay = QPushButton("Delete Account",self.w_delete_account)
                self.btn_delete_account_okay.setGeometry(175,285,100,40)
                self.btn_delete_account_okay.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
                self.btn_delete_account_okay.setStyleSheet("""QPushButton {  color:white;
                                                                        font-size:12px;
                                                                        border-radius:10px;
                                                                        border-style:solid;
                                                                        border-width:3px;
                                                                        border-color:black;
                                                                        background-color: rgb(112,108,97);
                                                                        }
                                                                        
                                                                        
                                                        QPushButton:hover {               
                                                                        border-radius:10px;
                                                                        border-style:solid;
                                                                        border-width:5px;
                                                                        border-color:black;  


                                                                        
                                                                       } """)

                ##########################
                ##    CHANGE PASSWORD   ##
                ##########################

                self.w_change_password = QWidget(self.w_main_screen)
                self.w_change_password.setGeometry(0,60,450,580)
                self.w_change_password.setStyleSheet("background-color:rgb(233,233,233);")
                self.w_change_password.hide()

                self.lbl_change_pasword_text = QLabel("Change Password",self.w_change_password)
                self.lbl_change_pasword_text.setStyleSheet("font-size :40px;")
                self.lbl_change_pasword_text.setGeometry(70,10,350,50)
                
                self.btn_back_from_chngpass_to_main = QPushButton(self.w_change_password)
                self.btn_back_from_chngpass_to_main.setIcon(QIcon("backarrow.png"))
                self.btn_back_from_chngpass_to_main.setGeometry(15,520,40,40)
                self.btn_back_from_chngpass_to_main.setIconSize(QSize(40,40))
                self.btn_back_from_chngpass_to_main.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
                self.btn_back_from_chngpass_to_main.setStyleSheet("border-width:3px; border-style:solid; border-color:black;")

                self.le_new_password = QLineEdit(self.w_change_password)
                self.le_new_password.setGeometry(75,220,300,50)
                self.le_new_password.setPlaceholderText("New Password")
                self.le_new_password.setEchoMode(QLineEdit.Password)
                self.le_new_password.setStyleSheet("""  QLineEdit {
                                                                        border-color:black;
                                                                        border-width:3px;
                                                                        border-style:solid;
                                                                        border-radius:15px;
                                                                        background:white;
                                                                } """)
                
                self.btn_change_pass_okay = QPushButton("Change Password",self.w_change_password)
                self.btn_change_pass_okay.setGeometry(175,285,100,40)
                self.btn_change_pass_okay.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
                self.btn_change_pass_okay.setStyleSheet("""QPushButton {  color:white;
                                                                        font-size:10px;
                                                                        border-radius:10px;
                                                                        border-style:solid;
                                                                        border-width:3px;
                                                                        border-color:black;
                                                                        background-color: rgb(112,108,97);
                                                                        }
                                                                        
                                                                        
                                                        QPushButton:hover {               
                                                                        border-radius:10px;
                                                                        border-style:solid;
                                                                        border-width:5px;
                                                                        border-color:black;  


                                                                        
                                                                       } """)




        #################
        ##  SHOW ALERT ##
        #################


        def Alert(self,text,type_):
                if type_ == 1 :    # Error Alerts
                        self.mbox_error = QMessageBox()
                        self.mbox_error.setWindowTitle("Online Bank System")
                        self.mbox_error.setWindowIcon(QIcon("bank-logo.png"))
                        self.mbox_error.setText(text)
                        self.mbox_error.setIcon(QMessageBox.Critical)
                        self.mbox_error.setStandardButtons(QMessageBox.Ok)
                        self.mbox_error.exec()

                elif type_== 2 :    # Success Alerts
                        self.mbox_succes = QMessageBox()
                        self.mbox_succes.setWindowTitle("Online Bank System")
                        self.mbox_succes.setWindowIcon(QIcon("bank-logo.png"))
                        self.mbox_succes.setText(text)
                        self.mbox_succes.setIcon(QMessageBox.Information)
                        self.mbox_succes.setStandardButtons(QMessageBox.Ok)
                        self.mbox_succes.exec()

                elif type_==3 : ## Questions
                        self.buttonReply = QMessageBox.question(self, 'Online Bank System', text, QMessageBox.Yes | QMessageBox.No)


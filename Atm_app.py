from atm_db import Atm_Main
from atm_gui import Atm_Gui
from PyQt5.QtWidgets import QMainWindow, QApplication , QMessageBox
import sys
import random


class Atm_App(QMainWindow,Atm_Gui):
    def __init__(self,*args,**kwargs):     
        super(Atm_App, self).__init__(*args, **kwargs)


        self.SetupGui(self)
        self.Connector()

        self.sql = Atm_Main()

        
       
    def Connector(self):
        self.btn_login_button.clicked.connect(self.Login_to_App)
        self.btn_signup_button.clicked.connect(self.Show_Register_Window)
        self.btn_back_to_login_screen.clicked.connect(self.Back_to_Login_Screen)
        self.btn_signup_register_button.clicked.connect(self.Register_To_App)
        self.btn_exit.clicked.connect(self.Exit)

        self.btn_money_withdraw.clicked.connect(self.Money_Withdraw_Screen)
        self.btn_money_deposit.clicked.connect(self.Money_Deposit_Screen)
        self.btn_money_transfer.clicked.connect(self.Money_Transfer_Screen)
        self.btn_take_credit.clicked.connect(self.Take_Credit_Screen)
        self.btn_close_credit.clicked.connect(self.Close_Credit_Screen)
        self.btn_settings.clicked.connect(self.Setting_Screen)
        self.btn_delete_account.clicked.connect(self.Delete_Account_Screen)
        self.btn_change_password.clicked.connect(self.Change_Password_Screen)
        self.btn_back_from_wth_to_main.clicked.connect(self.Back_to_Main_From_Wth)
        self.btn_back_from_dpst_to_main.clicked.connect(self.Back_to_Main_From_Dpst)
        self.btn_back_from_mts_to_main.clicked.connect(self.Back_to_Main_From_Mts)
        self.btn_back_from_tcrdt_to_main.clicked.connect(self.Back_to_Main_From_Tkcrdt)
        self.btn_back_from_clscrdt_to_main.clicked.connect(self.Back_to_Main_From_Clscrdt)
        self.btn_back_from_setting_to_main.clicked.connect(self.Back_to_Main_From_Setting)
        self.btn_back_from_dltaccnt_to_main.clicked.connect(self.Back_to_Main_From_DelAccount)
        self.btn_back_from_chngpass_to_main.clicked.connect(self.Back_to_Main_From_ChangePass)


        self.btn_withdraw_okay.clicked.connect(self.Money_Withdraw_Operation)
        self.btn_deposit_okay.clicked.connect(self.Money_Deposit_Operation)
        self.btn_transfer_okay.clicked.connect(self.Money_Transfer_Operation)
        self.btn_take_credit_okay.clicked.connect(self.Take_Credit_Operation)
        self.le_take_credit_amount.textChanged.connect(self.Update_Loan_Text)
        self.btn_close_credit_okay.clicked.connect(self.Close_Credit_Operation)
        self.btn_change_pass_okay.clicked.connect(self.Change_Password_Operation)
        self.btn_delete_account_okay.clicked.connect(self.Delete_Account_Operation)



    def Login_to_App(self):
        civil_number = self.le_login_ctz_number_bar.text()
        password = self.le_login_password_bar.text()

        self.sql.Login_User(civil_number,password)

        if self.sql.login_status == 1:
            self.Alert("Succesful Login ...",2)
            self.w_main_screen.show()
            self.w_login_screen.hide()

            self.Main_Window()

        elif self.sql.login_status == 0 :
            self.Alert("Citizenship Number or Password is wrong !",1)

    def Register_To_App(self):
        try : 
            id_ = random.randrange(1000000,1000000000)
            citizenship_number = self.le_register_ctz_number_bar.text()
            name = self.le_register_name_bar.text()
            surname = self.le_register_surname_bar.text()
            age = int(self.le_register_age_bar.text())
            birthdate = self.le_register_birthdate_bar.text()
            password = self.le_register_password_bar.text()

            self.sql.Create_New_User(id_,name,surname,age,citizenship_number,birthdate,password)

            if self.sql.error_register_status == 1:
                self.Alert("Error ... Please try again.",1)
            elif self.sql.error_register_status == 0:
                self.Alert("You have registered succesfully ...",2)

                self.le_register_ctz_number_bar.setText("")
                self.le_register_name_bar.setText("")
                self.le_register_surname_bar.setText("")
                self.le_register_age_bar.setText("")
                self.le_register_birthdate_bar.setText("")
                self.le_register_password_bar.setText("")

                
        except ValueError:
            self.Alert("Error ... Please try again.",1)
            
    def Show_Register_Window(self):
        self.w_register_screen.show()
        self.w_login_screen.hide()

    def Back_to_Login_Screen(self):
        self.w_register_screen.hide()

        self.le_register_ctz_number_bar.setText("")
        self.le_register_name_bar.setText("")
        self.le_register_surname_bar.setText("")
        self.le_register_age_bar.setText("")
        self.le_register_birthdate_bar.setText("")
        self.le_register_password_bar.setText("")


        self.w_login_screen.show()
    



    def Main_Window(self):
        self.lbl_user_name_text.setText(self.sql.name +" "+self.sql.surname)
        self.lbl_user_id_text.setText("ID :"+ " "+ str(self.sql.id))

        self.lbl_balance_text.setText(str(int(self.sql.balance)))
        self.lbl_loan_text.setText(str(int((self.sql.loan))))

        self.le_withdraw_money_amount.setText("0")
        self.le_deposit_money_amount.setText("0")
        self.le_transfer_money_amount.setText("0")
        self.le_take_credit_amount.setText("0")

        self.sql.error_withdraw_status = 0
        self.sql.error_deposit_status = 0
        self.sql.error_money_transfer_status = 0
        self.sql.error_take_credit_status = 0


   
    def Money_Withdraw_Screen(self):
        self.w_withdraw_money.show()  

    def Back_to_Main_From_Wth(self):
        self.w_withdraw_money.hide()
        self.Main_Window()

    def Money_Deposit_Screen(self):
        self.w_deposit_money.show()

    def Back_to_Main_From_Dpst(self):
        self.w_deposit_money.hide() 
        self.Main_Window()  

    def Money_Transfer_Screen(self):
        self.w_money_transfer.show()

    def Back_to_Main_From_Mts(self):
        self.w_money_transfer.hide()
        self.Main_Window()

    def Take_Credit_Screen(self):
        self.w_take_credit.show()

    def Back_to_Main_From_Tkcrdt(self):
        self.w_take_credit.hide()
        self.Main_Window()

    def Close_Credit_Screen(self):
        self.w_close_credit.show()

    def Back_to_Main_From_Clscrdt(self):
        self.w_close_credit.hide()
        self.Main_Window()

    def Setting_Screen(self):
        self.w_setting.show()

    def Back_to_Main_From_Setting(self):
        self.w_setting.hide()
        self.Main_Window()





    def Money_Withdraw_Operation(self):
        try:
            money_amount = int(self.le_withdraw_money_amount.text())

            if money_amount > int(self.sql.balance) :
                self.Alert("You don't have {}$".format(money_amount),1)

        

            else :
                self.sql.Money_Withdraw(money_amount)

                if self.sql.error_withdraw_status == 1:
                    self.Alert("Error ! Try Again ... ",1)
                    self.le_withdraw_money_amount.setText("0")

                elif self.sql.error_withdraw_status == 0:
                    self.Alert("You withdrew {}$ succesfully".format(money_amount),2)
                    self.le_withdraw_money_amount.setText("0")
                    self.lbl_balance_text.setText(str(int(self.sql.balance)))
        
        except ValueError:
            self.Alert("Please dont use ' , ' !",1)




    def Money_Deposit_Operation(self):
        try :

            money_amount = int(self.le_deposit_money_amount.text())

            self.sql.Money_Deposit(money_amount)

            if self.sql.error_deposit_status == 1 :

                self.Alert("Error ! Try Again ... ",1)
                self.le_deposit_money_amount.setText("0")

            elif self.sql.error_deposit_status == 0:
                self.Alert("You deposited {}$ succesfully".format(money_amount),2)
                self.le_deposit_money_amount.setText("0")
                self.lbl_balance_text.setText(str(int(self.sql.balance)))

        except ValueError:
            self.Alert("Please dont use ' , ' !",1)




    def Money_Transfer_Operation(self):
        try:
            id_ = self.le_transfer_money_id.text()
            money_amount = int(self.le_transfer_money_amount.text())

            if self.sql.balance < money_amount :
                self.Alert("You dont have {}$".format(money_amount),1)

            else :
                self.sql.Money_Transfer(id_,money_amount)

                if self.sql.error_money_transfer_status == 0:
                    self.Alert("You sent {}$ to '{}' succesfully ".format(money_amount,id_),2)
                    self.le_transfer_money_amount.setText("0")
                    self.le_transfer_money_id.setText("")

                    self.lbl_balance_text.setText(str(int(self.sql.balance)))


                elif self.sql.error_money_transfer_status == 1:
                    self.Alert("Error ! There is not user who has '{}' id number.".format(id_),1)

        except ValueError:
            self.Alert("Please dont use ' , ' !",1)




    def Take_Credit_Operation(self):
        
        credit_amount = int(self.le_take_credit_amount.text())
        self.sql.Take_Credit(credit_amount)

        if self.sql.error_take_credit_status == 0 :
            self.Alert("You took {}$ credit succesfully".format(credit_amount),2)
            self.lbl_balance_text.setText(str(int(self.sql.balance)))
            self.lbl_loan_text.setText(str(int((self.sql.loan))))

            self.le_take_credit_amount.setText("0")

        elif self.sql.error_take_credit_status == 1:
            self.Alert("Error. You couldn't take credit. \n Please Try again!",1)

            self.le_take_credit_amount.setText("0")




    def Update_Loan_Text(self):
        try:
            if self.le_take_credit_amount.text() == "" or self.le_take_credit_amount.text() == "0" :
                self.le_loan_amount.setText("")

            else :
                self.le_loan_amount.setText(str((int(self.le_take_credit_amount.text())*1.2)))
        except ValueError:
            self.Alert("Please dont use ' , ' !",1)
            self.le_take_credit_amount.setText("")




    def Close_Credit_Operation(self):
        try: 
            money_amount = int(self.le_close_credit_amount.text())

            if money_amount <= self.sql.balance :
                self.sql.Close_Credit(money_amount)

                if self.sql.error_close_credit_status == 0 :

                    self.lbl_loan_text.setText(str(int(self.sql.loan)))
                    self.lbl_balance_text.setText(str(int(self.sql.balance)))

                    self.Alert("You closed credit {}$".format(money_amount),2)
                    self.le_close_credit_amount.setText("0")
                    

                elif self.sql.error_close_credit_status == 1:
                    self.Alert("Error ! Please try again ... ",1)
                    self.le_close_credit_amount.setText("0")
            else :
                self.Alert("You dont have {}$".format(money_amount),1)
        except ValueError :
            self.Alert("Please dont use ' , ' !",1)

    

    def Delete_Account_Screen(self):
        self.w_delete_account.show()

    def Back_to_Main_From_DelAccount(self):
        self.w_delete_account.hide()
        self.Main_Window()

    def Change_Password_Screen(self):
        self.w_change_password.show()

    def Back_to_Main_From_ChangePass(self):
        self.w_change_password.hide()
        self.Main_Window()




    def Change_Password_Operation(self):
        if self.le_new_password.text() == "" :
            self.Alert("Password can not be blank",1)
        else :
            if self.sql.password == self.le_new_password.text():
                self.Alert("New password can not be same with old password",1)
            else :
                self.sql.Password_Change(self.le_new_password.text())
                self.Alert("Your password was changed succesfully",2)
                self.le_new_password.setText("")
                


    def Delete_Account_Operation(self):
        ct_number = self.le_delete_ctnumber.text()
        password = self.le_delete_password.text()

        self.Alert("Do you want to delete your account really?",3)

        if self.buttonReply == QMessageBox.Yes:
            if ct_number == "" or password == "":
                self.Alert("Citizenship Number or Password can not be blank!",1)
            else :
                if ct_number != self.sql.citizenship_number or password != self.sql.password:
                    self.Alert("Wrong citizenship number or password!",1)
                else :
                    self.Alert("You deleted your account succesfully.",2)
                    self.sql.Delete_User(ct_number,password)
                    self.le_delete_password.setText("")
                    self.le_delete_ctnumber.setText("")

                    self.w_main_screen.hide()
                    self.w_withdraw_money.hide()
                    self.w_deposit_money.hide()
                    self.w_money_transfer.hide()
                    self.w_take_credit.hide()
                    self.w_close_credit.hide()
                    self.w_setting.hide()
                    self.w_change_password.hide()
                    self.w_delete_account.hide()
                
                    self.w_login_screen.show()
                    self.sql.Logout_User()

                    self.le_login_ctz_number_bar.setText("")
                    self.le_login_password_bar.setText("")




    def Exit(self):
        self.Alert("Do you want to logout? ",3)

        if self.buttonReply == QMessageBox.Yes:

            self.w_main_screen.hide()
            self.w_withdraw_money.hide()
            self.w_deposit_money.hide()
            self.w_money_transfer.hide()
            self.w_take_credit.hide()
            self.w_close_credit.hide()
            self.w_setting.hide()
            self.w_change_password.hide()
            self.w_delete_account.hide()



            self.w_login_screen.show()
            self.sql.Logout_User()

            self.le_login_ctz_number_bar.setText("")
            self.le_login_password_bar.setText("")
        else:
            pass 



app = QApplication(sys.argv)
window = Atm_App()
window.show()
sys.exit(app.exec_())

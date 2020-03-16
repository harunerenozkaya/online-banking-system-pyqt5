import psycopg2 as psg

class Atm_Main():
    def __init__(self):

        self.id = ''
        self.name = ''
        self.surname = ''
        self.age = 0
        self.citizenship_number = 0
        self.birthdate = 0
        self.balance = 0
        self.loan = 0
        self.password = 0
       
        self.login_status = 0
        self.error_register_status = 0
        self.error_withdraw_status = 0
        self.error_deposit_status = 0
        self.error_money_transfer_status = 0
        self.error_take_credit_status = 0
        self.error_close_credit_status = 0
        


    def Create_New_User(self,id_,name='',surname='',age=0,citizenship_number=0,birthdate='',password=123123):

        try :
            ## CONNECT TO DATABASE
            conn = psg.connect(         user = "postgres",
                                        password = "pass",
                                        host = "127.0.0.1",
                                        port = "5432",
                                        database = "atm"
                                    )

            ## OPERATION
            cursor = conn.cursor()

            sql_command = """       INSERT INTO users (id,name,surname,age,citizenship_number,birthdate,password)
                            VALUES (%s,%s,%s,%s,%s,%s,%s)
                                        """
            variables = (id_,name,surname,age,citizenship_number,birthdate,password)
            cursor.execute(sql_command,variables)


            ## COMMIT
            conn.commit()
            

        except :
            self.error_register_status = 1




    def Delete_User(self,citizenship_number,password):

        try:
            ## CONNECT TO DATABASE
            conn = psg.connect(         user = "postgres",
                                        password = "pass",
                                        host = "127.0.0.1",
                                        port = "5432",
                                        database = "atm"
                                    )

            ## OPERATION
            cursor = conn.cursor()

            sql_pass_query = """   SELECT password FROM users 
                                WHERE citizenship_number = '{}'   """.format(citizenship_number)

            cursor.execute(sql_pass_query)

            true_pass = cursor.fetchall()[0][0]

            if str(password) == true_pass :
                sql_command_delete = """    DELETE FROM users 
                                            WHERE citizenship_number = '{}'; """.format(citizenship_number)
                cursor.execute(sql_command_delete)
    
            else:
                pass

            ## COMMIT
            conn.commit()

        except:
            pass
    



    def Login_User(self,citizenship_number,password):

        try:
            ## CONNECT TO DATABASE
            conn = psg.connect(         user = "postgres",
                                        password = "pass",
                                        host = "127.0.0.1",
                                        port = "5432",
                                        database = "atm"
                                    )

            ## OPERATION
            cursor = conn.cursor()

            sql_pass_query = """   SELECT password FROM users 
                                WHERE citizenship_number = '{}'   """.format(citizenship_number)

            cursor.execute(sql_pass_query)

            true_pass = cursor.fetchall()[0][0]

            if str(password) == true_pass :
                self.login_status = 1
                self.Get_and_Process_Datas(citizenship_number)

            else:
                print("Incorrect password or citizenship number")
                self.login_status = 0

            ## COMMIT
            conn.commit()

        except:
            self.login_status = 0
      



    def Get_and_Process_Datas(self,citizenship_number):
        try :
            ## CONNECT TO DATABASE
            conn = psg.connect(         user = "postgres",
                                        password = "pass",
                                        host = "127.0.0.1",
                                        port = "5432",
                                        database = "atm"
                                    )
            ## OPERATION
            cursor = conn.cursor()
            sql_all_data_query = """   SELECT * FROM users 
                                WHERE citizenship_number = '{}'   """.format(citizenship_number)
            cursor.execute(sql_all_data_query)

            personal_data_list = cursor.fetchall()
            self.id = personal_data_list[0][0]
            self.name = personal_data_list[0][1]
            self.surname = personal_data_list[0][2]
            self.age = personal_data_list[0][3]
            self.citizenship_number = personal_data_list[0][4]
            self.birthdate = personal_data_list[0][5]
            self.balance = personal_data_list[0][6]
            self.loan = personal_data_list[0][7]
            self.password = personal_data_list[0][8]

    
            ## COMMIT
            conn.commit()
        except :
            pass




    def Money_Transfer(self,target_id_,money_amount):

        try :
            ## CONNECT TO DATABASE
            conn = psg.connect(         user = "postgres",
                                        password = "pass",
                                        host = "127.0.0.1",
                                        port = "5432",
                                        database = "atm"
                                    )

            ## OPERATION
            cursor = conn.cursor()

            sql_query_id = """  SELECT id FROM users 
                                WHERE id = '{}';
                                                                    """.format(target_id_)

            sql_decrease_balance = """  UPDATE users 
                                        SET balance = balance - {}
                                        WHERE id = '{}' ;   """.format(money_amount,self.id)

            sql_increase_balance = """  UPDATE users
                                        SET balance = balance + {}
                                        WHERE id = '{}' ;
                                                                        """.format(money_amount,target_id_)


            cursor.execute(sql_query_id)
            id_list = cursor.fetchall()

            if id_list[0][0]:
                cursor.execute(sql_decrease_balance)
                cursor.execute(sql_increase_balance)
                conn.commit()
                self.Get_and_Process_Datas(self.citizenship_number)
                self.error_money_transfer_status = 0

            else :
                self.error_money_transfer_status = 1

        except :
            self.error_money_transfer_status = 1
            



    def Money_Withdraw(self,money_amount):

        try:
            ## CONNECT TO DATABASE
            conn = psg.connect(         user = "postgres",
                                        password = "pass",
                                        host = "127.0.0.1",
                                        port = "5432",
                                        database = "atm"
                                    )

            
            cursor = conn.cursor()
            
            sql_money_withdraw_code = """   UPDATE users 
                                            SET balance = balance - {}
                                            WHERE citizenship_number = '{}'          """.format(money_amount,self.citizenship_number)

            cursor.execute(sql_money_withdraw_code)

            ## COMMIT
            conn.commit()

            ## Get Current Data
            self.Get_and_Process_Datas(self.citizenship_number)
            self.error_withdraw_status = 0


        except :
            self.error_withdraw_status = 1




    def Money_Deposit(self,money_amount):

        try :
            ## CONNECT TO DATABASE

            conn = psg.connect(         user = "postgres",
                                        password = "pass",
                                        host = "127.0.0.1",
                                        port = "5432",
                                        database = "atm"
                                    )

            ## OPERATION

            cursor = conn.cursor()
            
            sql_money_withdraw_code = """   UPDATE users 
                                            SET balance = balance + {}
                                            WHERE citizenship_number = '{}'          """.format(money_amount,self.citizenship_number)

            cursor.execute(sql_money_withdraw_code)


            ## Commıt
            conn.commit()

            ## Get Current Data
            self.Get_and_Process_Datas(self.citizenship_number)

            self.error_deposit_status = 0

        except :
            self.error_deposit_status = 1
            



    def Password_Change(self,new_password):

        try :
            ## CONNECT TO DATABASE
            conn = psg.connect(         user = "postgres",
                                        password = "pass",
                                        host = "127.0.0.1",
                                        port = "5432",
                                        database = "atm"
                                    )


            ## OPERATION
            cursor = conn.cursor()
            sql_pass_change_code = """  UPDATE users
                                        SET password = '{}'
                                        WHERE citizenship_number = '{}' """.format(new_password,self.citizenship_number)
            
            cursor.execute(sql_pass_change_code)

            ## COMMIT
            conn.commit()

            ## Get Current Data
            self.Get_and_Process_Datas(self.citizenship_number)

        except :
            pass




    def Take_Credit(self,credit_amount):

        try :
            ## CONNECT TO DATABASE
            conn = psg.connect(         user = "postgres",
                                        password = "pass",
                                        host = "127.0.0.1",
                                        port = "5432",
                                        database = "atm"
                                    )
            
            ## OPERATION

            cursor = conn.cursor()

            sql_take_credit_code = """  UPDATE users
                                        SET loan = loan + {}* 1.2
                                        WHERE citizenship_number = '{}'    """.format(credit_amount,self.citizenship_number)

            sql_take_credit_gain_money_code = """   UPDATE users
                                                    SET balance = balance + {}
                                                    WHERE citizenship_number = '{}'    """.format(credit_amount,self.citizenship_number)
            
            cursor.execute(sql_take_credit_code)
            cursor.execute(sql_take_credit_gain_money_code)


            ## COMMIT
            conn.commit()

            ## Get Current Data
            self.Get_and_Process_Datas(self.citizenship_number)
            self.error_take_credit_status = 0
        except :
            self.error_take_credit_status == 1




    def Close_Credit(self,close_amount):

            try:
                ## CONNECT TO DATABASE
                conn = psg.connect(         user = "postgres",
                                            password = "pass",
                                            host = "127.0.0.1",
                                            port = "5432",
                                            database = "atm"
                                        )

                if self.loan < close_amount or close_amount > self.balance:
                    self.error_close_credit_status = 1

                else :         
                    cursor = conn.cursor()
                    sql_close_credit_loan_code = """    UPDATE users
                                                        SET loan = loan - {}
                                                        WHERE citizenship_number = '{}'     """.format(close_amount,self.citizenship_number)

                    sql_close_credit_balance_code = """     UPDATE users
                                                            SET balance = balance - {}
                                                            WHERE citizenship_number = '{}'     """.format(close_amount,self.citizenship_number)

                    cursor.execute(sql_close_credit_loan_code)
                    cursor.execute(sql_close_credit_balance_code)
                    
                    
                    conn.commit()


                    self.Get_and_Process_Datas(self.citizenship_number)
                    self.error_close_credit_status = 0

            except:
                self.error_close_credit_status = 1
                




    def Logout_User(self):
        self.login_status = 0
        self.error_register_status = 0

        self.id = ''
        self.name = ''
        self.surname = ''
        self.age = 0
        self.citizenship_number = 0
        self.birthdate = 0
        self.balance = 0
        self.loan = 0
        self.password = 0
    

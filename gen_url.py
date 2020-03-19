import pymysql
import csv 

class UserRecords():
    def get_record_dict(self,row):
        # generate a dictionary of user records
        
        record = { 
            'service_provider' : row[0],
            'user_id': row[1],
            'phonenumber':[row[2],row[3],row[4]],
        }
        return record



    def read_records_file(self,csvfile):
        get_dict = self.get_record_dict
        self.file = csvfile
        with open('records.txt', "r") as csv_file:
            csv_reader= csv.reader(csv_file)
            records = []
            for rows in csv_reader:
                data = get_dict(rows)
                records.append(data)
            
            print(records)
        return records

class UrlGeneration():

    def gen_user_url(self, records):
        print(records)


    def gen_url_head(records):
        # check service provider used 

        service_providers = ['Safaricom','Telcom', 'Airtel']
        if isp in service_providers:
            if isp == service_providers[0]:
                url_head = "saf://"
                print(url_head)
            elif isp == service_providers[1]:
                url_head = "tel://"
                print( url_head)
            elif isp == service_providers[2]:
                url_head = "air://"
                print(url_head)
        else:
            return "error occured"
        
        return url_head

    def get_users_in_db():
        # create connection to the database and query user data 

        connection = pymysql.connect(host='localhost',
                                 user='huncho',
                                 password='c11h28no3',
                                 db='dns',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                query = "SELECT * FROM users;"
                cursor.execute(query)
                records = [] 
                records= cursor.fetchall()
        finally:
            connection.close()
        return records

    def insert_user_id(userid):
        # insert new user id into the database
        try:
            with connection.cursor as cursor:
                query = "INSERT INTO users ()"
        

    def check_userid(records):
        # check if user id already exists in database

        user_id_list= []
        records = get_users_in_db()
        for users in records:
            user_id_list.append(users.get("user_id"))
            
            
        if userid in user_id_list:
                print("user id already exists please use a different user name ")
        
        else:
            return userid

        
# def get_phone_numbers(records):
#     for
# 

if __name__ == '__main__':
    csv_file = "records.txt"
    records= UserRecords()
    users = records.read_records_file(csv_file)

import pymysql
import csv 

# def gen_url_head(records):
#     # check service provider used 

#     service_providers = ['Safaricom','Telcom', 'Airtel']
#     if isp in service_providers:
#         if isp == service_providers[0]:
#             url_head = "saf://"
#             print(url_head)
#         elif isp == service_providers[1]:
#             url_head = "tel://"
#             print( url_head)
#         elif isp == service_providers[2]:
#             url_head = "air://"
#             print(url_head)
#     else:
#         return "error occured"
    
#     return url_head

# def get_users_in_db():
#     # create connection to the database and query user data 

#     connection = pymysql.connect(host='localhost',
#                              user='huncho',
#                              password='c11h28no3',
#                              db='dns',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)
#     try:
#         with connection.cursor() as cursor:
#             query = "SELECT * FROM users;"
#             cursor.execute(query)
#             records = [] 
#             records= cursor.fetchall()
#     finally:
#         connection.close()
#     return records

# # def insert_user_id(userid):
# #     # insert new user id into the database
# #     try:
# #         with connection.cursor as cursor:
# #             query = "INSERT INTO users ()"
    

# def check_userid(records):
#     # check if user id already exists in database

#     user_id_list= []
#     records = get_users_in_db()
#     for users in records:
#         user_id_list.append(users.get("user_id"))
        
        
#     if userid in user_id_list:
#             print("user id already exists please use a different user name ")
    
#     else:
#         return userid
        
# def get_phone_numbers(records):
#     for
# 
def read_records_file(csvfile):
    data = []
    with open('records.txt', "r") as csv_file:
        csv_reader= csv.reader(csv_file, delimiter=',')
        line_count = 0

        for row in csv_file:
            if line_count == 0:
                line_count+= 1
            else:
                data.append(row)
    return data

def get_record_dict(data):
    # import ipdb; ipdb.set_trace()
    records = { 
        'service_provider' : data[0],
        'user_id': data[1],
        'phonenumber':[data[2],data[3],data[4]],
    }
    return records

def gen_user_url(records):
    print(records)

if __name__ == '__main__':
    csv_file = "records.txt"
    get_record_dict(read_records_file(csv_file))
    

    gen_user_url (get_record_dict)
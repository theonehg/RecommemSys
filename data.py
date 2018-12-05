import pymysql.cursors  
import time
# Hàm trả về một connection.
def getConnection():
     
    # Bạn có thể thay đổi các thông số kết nối.
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',                             
                                 db='recommendsys',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

# def getUser():
#     conn = getConnection()
#     print("success")
#     id = []
#     try:
#         cursor = conn.cursor()
#         sql = "Select UserID from users"
#         cursor.execute(sql)
#         for row in cursor:
#             i = row["UserID"]
# #             usr = "user" + i
# #             password = "1234"
# #             is_sup = False
# #             is_staff = False
# #             is_active = True
# #             date_join = time.time()
#             id.append(i)

#         print("get")
#     finally:
#     # Đóng kết nối
#         conn.close()
        
#     return id

def getBook():
    conn = getConnection()
    print("success")
    books = []
    try:
        cursor = conn.cursor()
        sql = "Select ISBN, BookTitle, BookAuthor, YearOfPublication, Publisher, ImageURLS, ImageURLM, ImageURLL from books"
        cursor.execute(sql)
        for row in cursor:
            book = []
            book = {"ISBN": row["ISBN"], "BookTitle": row["BookTitle"], "BookAuthor": row["BookAuthor"], "YearOfPublication": row["YearOfPublication"], 
                    "Publisher": row["Publisher"], "ImageURLS": row["ImageURLS"], "ImageURLM": row["ImageURLM"], "ImageURLL": row["ImageURLL"]}
            books.append(book)
        print("get")
    finally:
    # Đóng kết nối
        conn.close()
    return books



def getRating():
    conn = getConnection()
    print("success")
    ratings = []
    try:
        cursor = conn.cursor()
        sql = "Select UserID, ISBN, BookRating from bxbookratings"
        cursor.execute(sql)
        for row in cursor:
            rating = {"UserID": row["UserID"], "ISBN": row["ISBN"], "BookRating": row["BookRating"]}
            ratings.append(rating)
        print("get")
    finally:
    # Đóng kết nối
        conn.close()
    return ratings

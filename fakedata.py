import data
import sqlite3
import time
import random 

db = sqlite3.connect('E:/Năm4/VDHD_VINH/DjangoShopApp/RecommemSys/db.sqlite3')
# id = data.getUser()
books = data.getBook()
# ratings = data.getRating()

# try :
#     cursor = db.cursor()
#     for i in id:
#         uid = i
#         usr = "user" + str(i)
#         password = "1234"
#         last_login = time.time()
#         is_sup = False
#         is_staff = False
#         is_active = True
#         date_join = time.time()
#         # sql =  "Insert into auth_user (id, password, last_login, is_superuser, username, first_name, email, is_staff, is_active, date_joined, last_name) " \
#              # + " values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) " 
     
#     # Thực thi sql và truyền 3 tham số
#         cursor.execute('''Insert into auth_user (id, password, last_login, is_superuser, username, first_name, email, is_staff, is_active, date_joined, last_name) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (uid, password, last_login, is_sup, usr, "", "", is_staff, is_active, date_join, ""))
#     db.commit() 
#     print("ok")
# finally: 
#     db.close()

try:
    cursor = db.cursor()
    i = 1
    for book in books:
        uid = i
        name = book["BookTitle"]
        slug = name.lower().replace(" ", "-")
        price = (random.randint(9,500))*1000 
        avail = True
        stock = 100
        create_at = time.time()
        update_at = time.time()
        cate_id = random.randint(0,10)
        auth = book["BookAuthor"]
        year_pub = book["YearOfPublication"]
        publis = book["Publisher"]
        imgs = book["ImageURLS"]
        imgm = book["ImageURLM"]
        imgl = book["ImageURLL"]
        isbn = book["ISBN"]
        sql =  "Insert into shop_product (id, name, slug, description, price, available, stock, created_at, updated_at, category_id, image, bookAuthor, yearOfPublication, Publisher, ImageURLS, ImageURLM, ImageURLL, ISBN) " \
             + " values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,?, ?, ?) " 
      
    # Thực thi sql và truyền 3 tham số
        cursor.execute(sql, (uid, name, slug,"", price, avail, stock, create_at, update_at, cate_id,"", auth, year_pub, publis, imgs, imgm, imgl, isbn))
        i+=1
    db.commit()
    print("ok") 
  
finally: 
    db.close()
# bid = dict()
# try:
#     cursor = db.cursor()
#     sql = "select id, ISBN from shop_product"
#     cursor.execute(sql)
#     for row in cursor:
#         isbn = row[1]
#         print(isbn)
#         bookid = row[0] 
#         bid[isbn] = bookid
#     db.commit() 
#     print("get bookid")
#     # print(bid['195153448'])
#     for rating in ratings:
#         # uid = rating["UserID"]
#         r = rating["ISBN"]
#         # print(r)
#         # book_id = bid[r]
#         # print(book_id)
#         # rating = rating["BookRating"]
        
#         sql =  "Insert into shop_bookRating (product_id, UserID, BookRating) " \
#              + " values (?, ?, ?) " 
      
#     # Thực thi sql và truyền 3 tham số
#         # cursor.execute(sql, (book_id, uid, rating))
#     db.commit()
#     # print("ok") 
  
# finally: 
#     db.close()

# cf = CF(m, 30, 1)
# cf.fit()
# cf.get_recommend_list(i)
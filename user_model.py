import mysql.connector
from mysql.connector import IntegrityError
import json
class UserModel:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost", user="root", password="357896", database="flask_test")
            self.mycursor = self.conn.cursor(dictionary=True)
            self.conn.autocommit = True
            print("connection successful")
        except:
            print("connection failed")

    def __del__(self):
        self.conn.close()
# read operation: get all users
    def get_all_books(self):
        try:
            self.mycursor.execute("SELECT * FROM books")
            return self.mycursor.fetchall()
        except Exception as e:
            return {"error": str(e)}
        finally:
            self.conn.close()
            print("connection closed")
# create operation: add user
    def add_book(self, data):
        try:
            query = "INSERT INTO books(title, author, published_date) VALUES ('{data['title']}','{data['author']}','{data['published_date']}')"
            values = (data['title'], data['author'], data['published_date'])
            self.mycursor.execute(query, values)
            return {"message": "Book added successfully"}
        except IntegrityError as e:
            return {"error": "Duplicate entry. Book already exists."}
        except Exception as e:
            return {"error": str(e)}
# update operation: update user
    def update_book(self, book_id, data):
        try:
            query = "UPDATE books SET title='{data['title']}', author='{data['author']}', published_date='{data['published_date']}', WHERE id='{data['id']}'"
            values = (data['title'], data['author'], data['published_date'], book_id)
            self.mycursor.execute(query, values)

            if self.mycursor.rowcount > 0:
                return {"message": "Book updated successfully"}
            else:
                return {"message": "Book not found"}
        except Exception as e:
            return {"error": str(e)}
# delete operation: delete user
    def delete_book(self, book_id):
        try:
            query = "DELETE FROM books WHERE id={id}"
            self.mycursor.execute(query, (book_id,))

            if self.mycursor.rowcount > 0:
                return {"message": "Book deleted successfully"}
            else:
                return {"message": "Book not found"}
        except Exception as e:
            return {"error": str(e)}


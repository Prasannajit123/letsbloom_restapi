from flask import Flask, request
from flask_restful import Resource, Api
from model.user_model import UserModel
from app import app


obj=UserModel()
# request handler:
@app.route('/user/getall')
def getall_controller():
    return obj.get_all_books()

@app.route('/user/addone',methods=['POST'])
def addone_controller():
    print(request.form)
    return obj.add_book(request.form)

@app.route('/user/update',methods=['PUT'])
def update_controller():
    print(request.form)
    return obj.update_book(request.form)

@app.route('/user/delete/<id>',methods=['DELETE'])
def delete_controller(id):
    print(id)
    return obj.delete_book(id)

if __name__ == '__main__':
    app.run(debug=True)

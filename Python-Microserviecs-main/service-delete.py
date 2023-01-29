from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_user as us

app = Flask(__name__)

@app.route('/delete', methods=['POST'])
def delete():
    
    user = request.form.get('username')


    _user = us.user_name()
    data = [x for x in _user if x["user"]==user]


    if not data:
        return {"error": "User not found"}, 401
    else:
        us.remove_user(user)
        return "User deleted successfully", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True) #127.0.0.1
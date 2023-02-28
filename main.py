from datetime import datetime
import socket
from flask import Flask, request, make_response
import mysql.connector

app = Flask(__name__)
cnx = mysql.connector.connect(user='root', password='root',
                              host='db', database='test_db')
cursor = cnx.cursor()

@app.route('/')
def index():
    # Add +1 to a global counter and save it to the database.
    cursor.execute("UPDATE access_log SET count = count + 1 WHERE id = 1")
    cnx.commit()

    # Create a cookie for 5 minutes with the value of the internal IP.
    response = make_response(socket.gethostbyname(socket.gethostname()))
    response.set_cookie('server_ip', value=response.get_data(as_text=True), max_age=300)

    # Record the date and time, the client's IP address, and its own internal IP address in a MySQL table named access_log.
    cursor.execute("INSERT INTO access_log (date, client_ip, server_ip) VALUES (%s, %s, %s)",
                   (datetime.now(), request.remote_addr, response.get_data(as_text=True)))
    cnx.commit()

    return response

@app.route('/showcount')
def showcount():
    # Return the global counter number.
    cursor.execute("SELECT count FROM access_log WHERE id = 1")
    row = cursor.fetchone()
    return str(row[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

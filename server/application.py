#!/usr/bin/env python

import sqlite3
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html", ipaddress=get_client_ip())

@app.route("/hello", methods=["GET", "POST"])
def hello():
	if request.method == "POST":
		computer_name = request.form["computer_name"]
		secret = request.form["secret"]
		computer_id = get_computer(computer_name, secret)
		if computer_id is not None:
			update_computer(computer_id)
			return render_template('hello-success.html')
		else:
			app.logger.info("Invalid attempt at saying hello from: %s" % request.remote_addr)
			return render_template('hello-fail.html'), 403
	else:
		return render_template('hello-form.html')

def get_computer(computer_name, secret):
	with get_database_connection() as con:
		result = con.execute("SELECT id FROM computer WHERE name = ? AND secret LIKE ?", (computer_name, secret)).fetchone()
		if result:
			return result[0]
	return None

def get_database_connection():
	return sqlite3.connect("sqlite3.db")

def get_client_ip():
	# Get the IP from the X-Forwarded-For header if present. Fallback to remote_addr.
	return request.headers.get("x-forwarded-for", request.remote_addr).split(", ")[0]

def update_computer(computer_id):
	ip_address = get_client_ip()
	with get_database_connection() as con:
		con.execute("INSERT INTO hello(computer_id, ipaddress) VALUES(?, ?)", (computer_id, ip_address))

if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0', port=8080)

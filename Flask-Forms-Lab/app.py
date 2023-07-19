from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

username = "Ella"
password = "123"                                   
facebook_friends=["Loai","Kenda","Avigail", "George", "Fouad", "Gi"]

@app.route('/',methods = ['GET','POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		if request.form['username'] == username and request.form['password'] == password:
			return redirect(url_for('home'))
		else:
			return render_template('login.html')
@app.route('/home')  # '/' for the default page
def home():
	return render_template('home.html', facebook_friends = facebook_friends)


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True)

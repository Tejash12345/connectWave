from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__ )

# Define a route for the login page
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        # Validate username and password (you should implement proper validation)
        if is_valid_login(username, password):
            # Redirect to a dashboard or another page upon successful login
            return redirect(url_for("dashboard"))
        else:
            error_message = "Invalid username or password"

    return render_template("portfolio.html", error_message=None)

# Define a route for the dashboard
@app.route("/dashboard")
def dashboard():
    # Implement your dashboard logic here
    return "Welcome to the Dashboard!"

def is_valid_login(username, password):
    # Implement user authentication logic here
    # You can query your database to check if the username and password match
    # For this example, we'll use a hardcoded username and password
    return username == "admin" and password == "password"


@app.route("/login" , methods = ['GET' , 'POST'])
def login():
    return render_template("login.html")

@app.route("/valid" , methods = ['GET' , 'POST'])
def valid():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        err = "Invalid Login Credentials.Please Try Again"

        users = { "username" : ["tejesh" , "gangadhar" , "admin" ] , "password" : ["tejesh21", "ganga" ,"admin"]}
        userIds = users["username"]
        userPass = users["password"]

        if username in userIds :
            ind = userIds.index(username)
            if password == userPass[ind]:
                return render_template("index.html")
            else:
                err = "Please Check Your Password"
                return render_template("login.html" , err = err)
            
        else:
            return render_template("login.html", err = err )

        
    else:
        return render_template("login.html")
    

@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/main")
def main():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)

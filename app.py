from flask import Flask, render_template, redirect, request, url_for,session


app = Flask(__name__) 

app.secret_key = "my-secret-key" 

@app.route("/") 
def home(): 
    return render_template("home.html")


@app.route("/login", methods=["POST"])
def login():

    username = request.form["name"] 
    password = request.form["pass"] 
 
    if username == "Mohan" and password == "1234": 

        token = jwt.encode({"user_id": 1,"username":"Mohan", "password":1234},app.secret_key, algorithm="HS256")

        return { 
            "message": "Login Successful", 
            "token": token 
        }
 
        
 
    return redirect(url_for('home')) 

@app.route("/logout") 
def logout(): 
 
    session.pop("username", None) 
 
    return redirect(url_for('home'))

@app.route("/about", methods=["GET"])
def about():
  return render_template("about.html")

@app.route("/course")
def course():
    return render_template("course.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")



if __name__ == "__main__": 
    app.run(debug=True) 

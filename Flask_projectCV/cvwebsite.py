from flask import Flask, redirect, url_for, render_template


app=Flask(__name__)
  # this sets the route to this page
@app.route("/")  
def home():
    return render_template('home.html')

    
if __name__ == "__main__":
    app.run()
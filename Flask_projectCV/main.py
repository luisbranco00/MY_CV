from flask import Flask, redirect, url_for, render_template, request



app=Flask(__name__)
# Handle form submission
# Handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('Name')
    email = request.form.get('Email')
    company = request.form.get('Company')
    propose = request.form.get('Propose')

    # Store data (replace this with your storage logic)
    print(f"Received: Name - {name}, Email - {email}, Company - {company}, Propose - {propose}")
    form_data = (f"Name: {name}\nEmail: {email}\nCompany: {company}\nPropose: {propose}\n")
    with open('form_response.txt', 'a') as file:
        file.write(form_data + '\n\n')
    return "Form submitted successfully!", 302, {'Location': url_for('home')}

@app.route("/")
def home():
    return render_template('home.html',methods = ['GET', 'POST'])

@app.route('/form')
def form():
    return render_template('form.html')
@app.route("/scholar_project")
def scholar_project():
    return render_template('scholar_projects.html',methods = ['GET', 'POST'])


@app.route("/about_me")
def about_me():
    return render_template('about_me.html',methods = ['GET', 'POST'])




if __name__ == "__main__":
    app.run()

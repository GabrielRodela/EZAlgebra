from flask import Flask, redirect, url_for, render_template, request, session, flash, jsonify
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
import random
import questions

rand_func_select = [questions.simple_addition, questions.division_small_div_no_rem, questions.division_med_div_rem, questions.division_small_div_rem, questions.division_big_div_rem, 
              questions.fraction_addition_easy, questions.fraction_addition_hard, questions.fraction_reduction, questions.improper_to_mixed, questions.find_smallest_fraction, 
              questions.fraction_addition_word, questions.volume_box, questions.percent_increase, questions.algebra_1_step, questions.algebra_2_step, questions.algebra_2_step_2_var, 
              questions.percent_decrease_word, questions.surface_area_t1, questions.surface_area_t2, questions.ratio_word, questions.purchase_tax,
              questions.percent_markup, questions.percent_decrease, questions.volume_cube, questions.percent_product, questions.evaluate_smallest_fraction, questions.fraction_division,
              questions.factoring_trinomials]


mixed_func_select = [questions.simple_addition, questions.division_small_div_no_rem, questions.division_med_div_rem, questions.division_small_div_rem, questions.division_big_div_rem, 
              questions.fraction_addition_easy, questions.fraction_addition_hard, questions.fraction_reduction, questions.improper_to_mixed, questions.find_smallest_fraction, 
              questions.volume_box, questions.algebra_1_step, questions.algebra_2_step, questions.algebra_2_step_2_var, questions.pythagorean_theorem, 
              questions.surface_area_t2, questions.volume_cube, questions.percent_product, questions.evaluate_smallest_fraction, questions.fraction_division]


percent_probs_select = [questions.percent_increase, questions.percent_decrease_word, questions.percent_markup, questions.percent_decrease, questions.purchase_tax]

algebra_select = [questions.algebra_1_step, questions.algebra_2_step, questions.algebra_2_step_2_var]


#db = SQLAlchemy()
app = Flask(__name__)
app.secret_key = "secret_key"
app.config['SQLALCHEMY_DATABSE_URI'] = 'sqlite:////users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=1)


#db.init_app(app)
"""

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(70))
    email = db.Column(db.String(70))

    def __init__(self, name, email):
        self.name = name
        self.email = email

"""

@app.route('/')
def splash():
    if "user" in session:
        user = session["user"]
        return render_template("splash_page_logged_in.html", usr = user)
    return render_template("splash_page.html")

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["name"]
        session["user"] = user
        #email = request.form["email"]
        #session["email"] = email        
        #flash("Login Successful!")
        return redirect(url_for("splash"))
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))
        return render_template("login.html")
    
@app.route('/user', methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user = user)
    else:
        flash("Not Logged In!")
        return redirect(url_for("login"))
"""

@app.route('/view')
def view():
    return render_template("view.html", values=users.query.all())

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["name"]
        session["user"] = user
        email = request.form["email"]
        session["user"] = user

        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session["email"] = found_user.email
        else:
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit()
        
        flash("Login Successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route('/user', methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash("Info saved!")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html", email=email)
    else:
        flash("Not Logged In!")
        return redirect(url_for("login"))
"""
    
@app.route('/logout')
def logout():
    flash("You're now logged out!", "info")
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route('/Single_Topic_Practice', methods=['GET'])
def link1():
    q = [questions.simple_addition()]
    return render_template("Single_Topic_Practice.html", q1 = q[0][0], a1 = q[0][1])

@app.route('/Single_Topic_Practice/One_Step_Algebra', methods=['GET'])
def algebra_1_step():
    q = [random.choice(algebra_select)()]
    return render_template("One_Step_Algebra.html", q1 = q[0][0], a1 = q[0][1])

@app.route('/Single_Topic_Practice/Pythagorean_Theorem', methods=['GET'])
def pyth_theorem():
    q = [questions.pythagorean_theorem()]
    return render_template("Pythagorean_Theorem.html", q1 = q[0][0], a1 = q[0][1])

@app.route('/Single_Topic_Practice/Percent_Problems', methods=['GET'])
def perc_prob():
    q = [random.choice(percent_probs_select)()]
    return render_template("Percent_Problems.html", q1 = q[0][0], a1 = q[0][1])

@app.route('/Random_Practice', methods=['GET'])
def link2():
    q = [random.choice(rand_func_select)()]
    return render_template("Random_Practice.html", q1 = q[0][0], a1 = q[0][1])

@app.route('/Mixed_HW')
def link3():
    q = []
    for i in range(12):
        q.append(random.choice(mixed_func_select)())
    return render_template("mixed_HW.html", 
                           q1 = q[0][0], q2 = q[1][0], q3 = q[2][0], 
                           q4 = q[3][0], q5 = q[4][0], q6 = q[5][0], 
                           q7 = q[6][0], q8 = q[7][0], q9 = q[8][0], 
                           q10 = q[9][0], q11 = q[10][0], q12 = q[11][0], 
                           a1 = q[0][1], a2 = q[1][1], a3 = q[2][1],
                           a4 = q[3][1], a5 = q[4][1], a6 = q[5][1],
                           a7 = q[6][1], a8 = q[7][1], a9 = q[8][1],
                           a10 = q[9][1], a11 = q[10][1], a12 = q[11][1])

@app.route('/Guided_Practice', methods=['GET'])
def link4():
    q = [questions.factoring_trinomials()]
    c = abs(q[0][2]*q[0][3])
    factors = []
    for i in range(1,c//2+1):
        if c%i == 0:
            factors.append(i)
    factors.append(c)
    return render_template("Guided_Practice.html", q1 = q[0][0], a1 = q[0][1], f1 = q[0][2], f2 = q[0][3], factors = factors)


@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.get_json()
    user_answer = str(data['answer'])
    correct_answer = str(data['correct_answer'])
    if user_answer == correct_answer:
        result = "Correct!\n Refresh to keep practicing!"
    else:
        result = "Incorrect, try again!"
    return jsonify({'result': result})

if __name__ == "__main__":
    #with app.app_context():
     #   db.create_all()
    app.run(debug=True)
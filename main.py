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


percent_probs_select = [questions.percent_increase, questions.percent_decrease_word, questions.percent_markup, questions.percent_decrease, questions.purchase_tax, questions.percent_product]

fractions_select = [questions.fraction_addition_easy, questions.fraction_addition_hard, questions.fraction_reduction, questions.find_smallest_fraction, 
                questions.fraction_addition_word, questions.evaluate_smallest_fraction, questions.fraction_division]

algebra_select = [questions.algebra_1_step, questions.algebra_2_step, questions.algebra_2_step_2_var]

geometry_select = [questions.volume_box, questions.pythagorean_theorem, questions.surface_area_t1, questions.surface_area_t2, questions.volume_cube]

algebra_II_select = [questions.factoring_trinomials, questions.complete_the_square]

app = Flask(__name__)
app.secret_key = "secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=1)

db = SQLAlchemy(app)
#db.init_app(app)


class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(70))
    email = db.Column(db.String(70))

    def __init__(self, name, email):
        self.name = name
        self.email = email



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

        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session["email"] = found_user.email
        else:
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit()
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
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html", user = user, email = email)
    else:
        flash("Not Logged In!")
        return redirect(url_for("login"))

@app.route('/view')
def view():
    return render_template("view.html", values=users.query.all())

    
@app.route('/logout')
def logout():
    flash("You're now logged out!", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))



@app.route('/Single_Topic_Practice/Algebra_I', methods=['GET'])
def algebra_1():
    if "user" in session:
        user = session["user"]
    else:
        user = "Guest"
    q = [random.choice(algebra_select)()]
    return render_template("algebra_I.html", q1 = q[0][0], a1 = q[0][1], usr = user)

@app.route('/Single_Topic_Practice/Algebra_I/One_step', methods=['GET'])
def algebra_1a():
    q = [questions.algebra_1_step()]
    return render_template("algebra_I.html", q1 = q[0][0], a1 = q[0][1])

@app.route('/Single_Topic_Practice/Algebra_I/Two_step', methods=['GET'])
def algebra_1b():
    q = [questions.algebra_2_step()]
    return render_template("algebra_I.html", q1 = q[0][0], a1 = q[0][1])

@app.route('/Single_Topic_Practice/Algebra_I/Multi_variable', methods=['GET'])
def algebra_1c():
    q = [questions.algebra_2_step_2_var()]
    return render_template("algebra_I.html", q1 = q[0][0], a1 = q[0][1])



@app.route('/Single_Topic_Practice/Geometry', methods=['GET'])
def geometry():
    q = [random.choice(geometry_select)()]
    return render_template("geometry.html", q1 = q[0][0], a1 = q[0][1])

@app.route('/Single_Topic_Practice/Geometry/Pythagorean_theorem', methods=['GET'])
def geometry_a():
    q = [questions.pythagorean_theorem()]
    return render_template("geometry.html", q1 = q[0][0], a1 = q[0][1])

@app.route('/Single_Topic_Practice/Geometry/Volume', methods=['GET'])
def geometry_b():
    choices = [questions.volume_box, questions.volume_cube]
    q = [random.choice(choices)()]
    return render_template("geometry.html", q1 = q[0][0], a1 = q[0][1])

@app.route('/Single_Topic_Practice/Geometry/Surface_area', methods=['GET'])
def geometry_c():
    choices = [questions.surface_area_t1, questions.surface_area_t2]
    q = [random.choice(choices)()]
    return render_template("geometry.html", q1 = q[0][0], a1 = q[0][1])




@app.route('/Single_Topic_Practice/Algebra_II', methods=['GET'])
def algebra_2():
    q = [random.choice(algebra_II_select)()]
    return render_template("algebra_II.html", q1 = q[0][0], a1 = q[0][1])

@app.route('/Single_Topic_Practice/Algebra_II/Factoring_trinomials', methods=['GET'])
def algebra_2a():
    q = [questions.factoring_trinomials()]
    return render_template("algebra_II.html", q1 = q[0][0], a1 = q[0][1])

@app.route('/Single_Topic_Practice/Algebra_II/Completing_the_square', methods=['GET'])
def algebra_2b():
    q = [questions.complete_the_square()]
    return render_template("algebra_II.html", q1 = q[0][0], a1 = q[0][1])




@app.route('/Single_Topic_Practice/Pipefitter_prep', methods=['GET'])
def pipefitter_prep():
    q = [random.choice(rand_func_select)()]
    return render_template("pipefitter_prep.html", q1 = q[0][0], a1 = q[0][1])

@app.route('/Single_Topic_Practice/Pipefitter_prep/Fractions', methods=['GET'])
def pipefitter_prep_a():
    q = [random.choice(fractions_select)()]
    return render_template("pipefitter_prep.html", q1 = q[0][0], a1 = q[0][1])

@app.route('/Single_Topic_Practice/Pipefitter_prep/Percents', methods=['GET'])
def pipefitter_prep_b():
    q = [random.choice(percent_probs_select)()]
    return render_template("pipefitter_prep.html", q1 = q[0][0], a1 = q[0][1])

@app.route('/Single_Topic_Practice/Pipefitter_prep/Geometry', methods=['GET'])
def pipefitter_prep_c():
    choices = [questions.hypoteneuse, questions.pythagorean_theorem]
    q = [random.choice(choices)()]
    return render_template("pipefitter_prep.html", q1 = q[0][0], a1 = q[0][1])



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
    with app.app_context():
        db.create_all()
    app.run(debug=True)
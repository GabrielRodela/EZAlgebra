from flask import Flask, redirect, url_for, render_template, request, jsonify
import random
import questions

rand_func_select = [questions.simple_addition, questions.division_small_div_no_rem, questions.division_med_div_rem, questions.division_small_div_rem, questions.division_big_div_rem, 
              questions.fraction_addition_easy, questions.fraction_addition_hard, questions.fraction_reduction, questions.improper_to_mixed, questions.find_smallest_fraction, 
              questions.fraction_addition_word, questions.volume_box, questions.percent_increase, questions.algebra_1_step, questions.algebra_2_step, questions.algebra_2_step_2_var, 
              questions.pythagorean_theorem, questions.percent_decrease_word, questions.surface_area_t1, questions.surface_area_t2, questions.ratio_word, questions.purchase_tax,
              questions.percent_markup, questions.percent_decrease, questions.volume_cube, questions.percent_product, questions.evaluate_smallest_fraction, questions.fraction_division,
              questions.factoring_trinomials]


mixed_func_select = [questions.simple_addition, questions.division_small_div_no_rem, questions.division_med_div_rem, questions.division_small_div_rem, questions.division_big_div_rem, 
              questions.fraction_addition_easy, questions.fraction_addition_hard, questions.fraction_reduction, questions.improper_to_mixed, questions.find_smallest_fraction, 
              questions.volume_box, questions.algebra_1_step, questions.algebra_2_step, questions.algebra_2_step_2_var, questions.pythagorean_theorem, 
              questions.surface_area_t2, questions.volume_cube, questions.percent_product, questions.evaluate_smallest_fraction, questions.fraction_division]


app = Flask(__name__)

@app.route('/')
def splash():
    return render_template("splash_page.html")

@app.route('/Single_Topic_Practice', methods=['GET'])
def link1():
    q = [questions.simple_addition()]
    return render_template("Single_Topic_Practice.html", q1 = q[0][0], a1 = q[0][1])

@app.route('/Single_Topic_Practice/One_Step_Algebra', methods=['GET'])
def algebra_1_step():
    q = [questions.algebra_1_step()]
    return render_template("One_Step_Algebra.html", q1 = q[0][0], a1 = q[0][1])

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
    return render_template("Guided_Practice.html", q1 = q[0][0], a1 = q[0][1], f1 = q[0][2], f2 = q[0][3])


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
    app.run(debug=True)
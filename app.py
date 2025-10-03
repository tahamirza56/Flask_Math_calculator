from flask import Flask, render_template, request
import math
import cmath

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/area_circle")
def area_circle():
    return render_template('area_circle.html')

@app.route("/calculate_circle", methods=['POST'])
def calculate_circle():
    radius_str = request.form['radius']
    radius_float= float(radius_str)

    circle_area = math.pi * (radius_float ** 2)

    area_final_answer= round(circle_area,2)

    circle_circumfrence= 2 * math.pi * radius_float

    circum_final_answer= round(circle_circumfrence)

    return render_template('calculate_circle.html', area_result = area_final_answer, circum_result=circum_final_answer)

@app.route('/square')
def square_area():
    return render_template('square.html')


@app.route('/calculate_square' , methods = ['POST'])
def calculate_square():
    side_str=request.form['side_length']
    side_float=float(side_str)

    square_area = side_float ** 2
    final_answer=round(square_area,2)

    return render_template('/calculate_square.html', square_result=final_answer)


@app.route('/leap_year')
def leap_year():
    return render_template('leap_year.html')

@app.route('/calculate_year', methods=['POST'])
def calculate_year():
    year_str= request.form['year']
    year_float=float(year_str)

    if year_float % 100 != 0 and year_float % 4 == 0 or year_float % 400 == 0:
        return render_template('calculate_year.html', year="Leap year")
    else:
        return render_template('calculate_year.html',year="Not a Leap Year")
    
@app.route('/equation')
def equation():
    return render_template('equation.html')

@app.route('/calculate_roots', methods=['POST'])
def calculate_roots():
    coff_A_str=request.form['A']
    coff_A=float(coff_A_str)
    coff_B_str=request.form['B']
    coff_B=float(coff_B_str)

    coff_C_str=request.form['C']
    coff_C=float(coff_C_str)

    D=(coff_B**(2) - (4*coff_A*coff_C))
    if D > 0:
        message = "roots are real and distinct"
        root1 = (-coff_B - D**0.5) / (2*coff_A)
        root2 = (-coff_B + D**0.5) / (2*coff_A)
        result1 = root1
        result2 = root2

    elif D == 0:
        message = "The roots are REAL and IDENTICAL:"
        root1 = root2 = -coff_B / (2*coff_A)
        result1 = f"{root1:.2f}"
        result2 = f"{root2:.2f}"

    else:
        message = "The roots are COMPLEX:"
        root1 = (-coff_B - cmath.sqrt(D)) / (2 * coff_A)
        root2 = (-coff_B + cmath.sqrt(D)) / (2 * coff_A)
        result1 = f"{root1.real:.2f} + {root1.imag:.2f}i"
        result2 = f"{root2.real:.2f} + {root2.imag:.2f}i"

    return render_template('calculate_roots.html', result1=root1,result2= root2,Message_result=message)





if __name__ == '__main__':
    app.run(debug=True)
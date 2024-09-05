from flask import Flask, render_template, request, jsonify
from Krutrim_test import code
from process_response import separate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']
    init_para, job_list = separate(code(message))
    return render_template('submitted.html', name = name, para = init_para, job =  job_list)

if __name__ == '__main__':
    app.run()
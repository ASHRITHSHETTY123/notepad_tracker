from flask import Flask, render_template, request, redirect
from git import Repo
import glob, os


app = Flask(__name__)
repo = Repo(r"C:\Users\ASHRITH SHETTY\Desktop\Notepad_Tracker")

@app.route('/')
def index():
    os.chdir(r"C:\Users\ASHRITH SHETTY\Desktop\Notepad_Tracker\docs")
    file_list = glob.glob("*.txt")
    return render_template('index.html', file_list=file_list)

@app.route('/save', methods=['POST'])
def save():
    note = request.form['note']
    repo.git.add('.')
    repo.index.commit(note)
    new_file = repo.working_tree_dir + '/' + request.form['filename'] + '.txt'
    with open(new_file, 'w') as f:
        f.write(note)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)

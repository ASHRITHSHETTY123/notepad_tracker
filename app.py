from flask import Flask, render_template, request, redirect
from git import Repo


app = Flask(__name__)
repo = Repo(r"C:\Users\ASHRITH SHETTY\Desktop\Notepad_Tracker")

@app.route('/')
def index():
 
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    note = request.form['note']
    repo.git.add('.')
    repo.index.commit(note)
    new_file = repo.working_tree_dir + '/' + request.form['filename'] + '.txt'
    with open(new_file, 'w') as f:
        f.write(note)
    return redirect('/')
    # note = request.form['note']
    # filename = request.form['filename'] + '.txt'
    # filepath = os.path.join(repo.working_tree_dir, filename)
    # with open(filepath, 'w') as f:
    #     f.write(note)
    # repo.index.add([filepath])
    # repo.index.commit(request.form['note'])
    # return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

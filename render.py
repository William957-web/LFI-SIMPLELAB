from flask import *
from flaskext.markdown import Markdown
app = Flask(__name__)
Markdown(app)

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/getfile', methods=['GET', 'POST'])
def id():
    if request.method == 'POST':
        file=request.form['file']
        f=open(f'files/{file}', 'rb')
        return render_template('index.html',content=str(f.read().decode()))
    else:
        return "Method not allow"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)

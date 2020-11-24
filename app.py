from flask import Flask, request, render_template
from src import verify_face as vf
from src import frames as fm
import os



app = Flask(__name__)
app._static_folder = os.path.abspath("templates/static/")

#Home Navigation
@app.route('/')
@app.route('/video')
def capture_video():
    return render_template('index.html')

#cheat navigation
@app.route('/cheat')
def is_cheat():
    return fm.frames()
    


if __name__=="__main__":
    app.run(debug=True, port=5000)

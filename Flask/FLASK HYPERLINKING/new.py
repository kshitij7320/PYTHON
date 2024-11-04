#IMPORTING
from flask import Flask, render_template
import os

#INTERACTION
app = Flask(__name__)

picfolder = os.path.join('static')

app.config['UPLOAD_FOLDER'] = picfolder

#MAPPING
@app.route('/')

#INPUT

def first():
    pic = os.path.join(app.config["UPLOAD_FOLDER"], 'p02k6vry.jpg')
    return render_template('home.html',user_image =pic)

@app.route('/second')
def second():
    return render_template('second.html')

#MAIN
if __name__ =='__main__':
    app.run(debug=True)
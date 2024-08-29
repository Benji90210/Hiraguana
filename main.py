import pandas as pd
from flask import Flask, render_template
import shutil
import numpy as np


new_file = r'D:\Python\Hiragana\static\img.gif'
app = Flask(__name__)

son = None
lg = None
gif = None


@app.route('/', methods=['GET', 'POST'])
def form():
    dt = pd.read_csv('data.csv')
    n = np.shape(dt)[0]
    random_number = np.random.randint(0, n)
    son = dt['son'].iloc[random_number]
    lg = dt['langue'].iloc[random_number]
    gif = dt['files'].iloc[random_number]

    shutil.copy(gif, new_file)
    print(gif)
    return render_template('index.html', son=son, lg=lg)


@app.route('/solution', methods=['GET', 'POST'])
def rep():
    return render_template('solution.html', gif=gif)


'''' legacy code to create the file with character from wiki '''
'''
dir_path = r'D:\Git\Hiragana\gif'

def getdata(x, datatype):
    x = x.split('_')
    if datatype == 'son':
        y = x[1]
    elif datatype == 'langue':
        temp = len(x[0])
        y = x[0][temp-8:]
        if y == 'Hiragana':
            y = 'Hiragana'
        else:
            y = 'Katakana'
    return y


def createfile():
    import glob
    files = glob.glob("D:/Python/Hiragana/gif/*.gif")
    files = pd.DataFrame(files, columns=['files'])
    files['son'] = files['files'].apply(lambda x: getdata(x, 'son'))
    files['langue'] = files['files'].apply(lambda x: getdata(x, 'langue'))
    files['Box'] = 1
    files.to_csv('data.csv')
    return 0
'''

if __name__ == '__main__':
    app.run(debug=True)










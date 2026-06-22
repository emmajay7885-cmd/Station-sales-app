from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        start = float(request.form['start'])
        end = float(request.form['end'])
        price = float(request.form['price'])
        
        liters = end - start
        result = liters * price
        
        return render_template('index.html', result=round(result, 2), liters=round(liters, 2))
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

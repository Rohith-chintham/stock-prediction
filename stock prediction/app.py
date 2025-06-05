from flask import Flask, render_template, request
from model import get_stock_data, predict_next_7_days

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ticker = request.form['ticker'].upper()
        try:
            df = get_stock_data(ticker)
            predictions = predict_next_7_days(df)
            return render_template('result.html', ticker=ticker, predictions=predictions)
        except Exception as e:
            return f"Error: {str(e)}"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

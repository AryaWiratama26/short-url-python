from flask import Flask, render_template, request
from shortUrl import short_url
app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    if request == 'POST':
        short_url()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
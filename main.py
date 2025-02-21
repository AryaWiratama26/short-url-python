from flask import Flask, render_template, request
from shortUrl import short_url
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def convert_url():
    get_url = request.form.get("url_user")    
    shortened_url = short_url(get_url)
    return render_template('index.html', shortened_url=shortened_url)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

# monitor the change
if __name__ == '__main__':
    app.run(debug=True)
    app.run(debug=True)

from flask import Flask

app = Flask('counter')
counter = 0


@app.route('/count')
def count():
    global counter
    counter += 10
    return str(counter)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

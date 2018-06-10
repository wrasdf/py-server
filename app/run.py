from bottle import Bottle, run, template
app = Bottle()

@app.route('/hello/<name>')
def index(name="Guest"):
    return template('Hello {{name}}, how are you?', name=name)

run(app, host='0.0.0.0', port=8080, debug=True)

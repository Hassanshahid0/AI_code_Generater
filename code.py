from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def input_form():
  return '''
    <form method="POST">
      <input name="input_field">
      <input type="submit">
    </form>q
  '''

@app.route('/', methods=['POST'])
def input_form_submit():
  input_text = request.form['input_field']
  return f'You entered: {input_text}'

if __name__ == '__main__':
  app.run()

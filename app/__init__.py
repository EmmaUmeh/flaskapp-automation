from flask import Flask
from .automate import add

app = Flask(__name__)

@app.route('/addition')
def addition():
    # Call the add function
    sum_result = add(5, 3)
    return f'Automated Deployment - The sum is: {sum_result}'

@app.route('/')
def default_route():
    return 'Automated Deployment'

if __name__ == '__main__':
    app.run(debug=True)

  

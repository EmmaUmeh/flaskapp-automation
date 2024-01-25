# from flask import Flask
# from .automate import add

# app = Flask(__name__)

# @app.route('/addition')
# def addition():
#     # Call the add function
#     sum_result = add(5, 3)
#     return f'The sum of the Automated Deployment is: {sum_result}'

# @app.route('/')
# def default_route():
#     return 'Automated Deployment'

# if __name__ == '__main__':
#     app.run(debug=True)

  
from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app

# Import the add function from automate module
from .automate import add

# Create the Flask app
app = Flask(__name__)

# Add a route for the addition function
@app.route('/addition')
def addition():
    # Call the add function
    sum_result = add(5, 3)
    return f'The sum of the Automated Deployment is: {sum_result}'

# Add a default route
@app.route('/')
def default_route():
    return 'Automated Deployment'

# Wrap the Flask app with Prometheus WSGI middleware
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

# Run the Flask app
if __name__ == '__main__':
    
    app.run(debug=True)


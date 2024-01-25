from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
from .automate import add

# Install prometheus-flask-exporter
try:
    from prometheus_flask_exporter import PrometheusMetrics
except ImportError:
    print("prometheus-flask-exporter is not installed. Installing...")
    import subprocess
    subprocess.run(["pip", "install", "prometheus-flask-exporter"], check=True)
    from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/addition')
def addition():
    # Call the add function
    sum_result = add(5, 3)
    return f'The sum of the Automated Deployment is: {sum_result}'

@app.route('/')
def default_route():
    return 'Automated Deployment'

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This APP Deployed Via ArgoCD 12-10-2022 Thank you!!!'

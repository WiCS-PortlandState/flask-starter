from flask import Flask
import requests

app = Flask(__name__)

# Here we define the various routes we want users to be able to call (Ex: myurl.com/)
@app.route('/')
def hello_world():
    return 'Hello World!'

# We can use this method to call a web service and get the result as JSON
def rest_service_call():
    r = requests.post("URL for the web resource I want", data={"key for passed data": "value"})
    json_response = r.json()
    print(json_response)


if __name__ == '__main__':
    app.run()

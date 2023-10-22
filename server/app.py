from flask import Flask, request , send_from_directory
from flask_cors import CORS
app = Flask(__name__)
data = '''{
"Temperature":30, 
"Humidity":79,
 "Rain":false
}'''
CORS(app)
@app.route('/' , methods=['GET'])
def Home():
    return send_from_directory("StaticFiles", "index.html")


  
@app.route('/upload', methods=['POST'])
def receive_data():
    global data
    data = request.get_json()
    # Process the received data as needed
    print(data)
    return "Data received successfully", 200
@app.route('/StaticFiles/<filename>')
def shareFile(filename):
    return send_from_directory("StaticFiles", filename)

@app.route('/getData' , methods=['GET'])
def getData():
    global data
    return data
if __name__ == '__main__':
    app.run(host='0.0.0.0')

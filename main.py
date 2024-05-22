import subprocess
from flask import Flask, jsonify, request


app = Flask(__name__)




@app.route('/', methods=['GET', 'POST'])
def index():
   print(request.method)
   if request.method == 'GET':
       return jsonify(request.args)
   elif request.method == 'POST':
       print(request.get_json())
       if 'command' in request.get_json():
           print(request.get_json()['command'])
           if request.get_json()['target'] == 'py':
               output = subprocess.run('py execute.py ' + request.get_json()['command'], capture_output=True, shell=True, text=True)
               print(output.stdout)
               return output.stdout
           output = subprocess.run("powershell.exe " + request.get_json()['command'], capture_output=True, shell=True, text=True)
           print(output.stdout)
           return output.stdout
       if request.get_json() != None:
           return jsonify(request.get_json())
       else:
           return jsonify(request.form)




if __name__ == '__main__':
   app.run(debug=True, port=8888, host='0.0.0.0')

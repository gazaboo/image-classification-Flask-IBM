from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():

    # Get and save image  
    file = request.files['file']
    file.save('./static/images/image.jpg')

    # Post to other container
    # Notice the URL. Only using container name for resolution  
    url = 'http://ibm:5000/model/predict'
    img = {'image': open('./static/images/image.jpg', 'rb')}
    response = requests.post(url, files=img)

    # Get relevant data from response
    result = response.json()['predictions']
    result = map(lambda x: x['label'] + " : " + str(x['probability']), result)
    
    # Build and return HTML 
    return render_template('result.html', filename="image.jpg", result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
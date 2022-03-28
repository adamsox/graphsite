import time
from flask import request
import json
from flask import Flask
from flask_cors import CORS
from course_searcher import search_course 
from graph import codeFormat

# from subject_writer import codeFormat

app = Flask(__name__)
#CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}})
@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}

from flask_cors import cross_origin

@app.route('/api/query', methods=['POST'])
def get_query_from_react():
  if(request.method == 'POST'):
    data = request.get_json()

    list_query = data['data']['input']

    other = search_course(list_query)
    
    return json.dumps(other)

@app.route('/api/graph', methods = ['POST'])
def get_graph():

    data = request.get_json()

    

    return codeFormat(data['data']['name'])


@app.route('/api/work')
@cross_origin()
def helloWorld():
  return "Hello, cross-origin-world!"

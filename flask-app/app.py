import os

from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
import ast, json, requests
from worker_proxy import celery
from flask import jsonify
from constants import *

app = FlaskAPI(__name__)

@app.route("/", methods=['GET', 'POST'])
def get_post_response(variable_name = "fecha"):
    """
    List or create notes.
    """
    if request.method == 'GET':
        csv_string= str(request.args.get('username'))+","+str(request.args.get('from'))+ ","+request.args.get('msisdn')+","+request.args.get('content')+"\n"
        csv_string=csv_string.encode('ascii','ignore').decode('ascii')
        #Now check if have to response
        for key in QUESTION_ANSWERS.keys():
            if QUESTION_ANSWERS[key]["q"] in csv_string:
                task = celery.send_task('mytasks.send_response', args=[request.args.get('msisdn'), QUESTION_ANSWERS[key]["a"]], kwargs={})
                break
        return {'status':'4'}

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True,host="0.0.0.0", port= int(os.getenv('WEBHOOK_PORT', 5000)))

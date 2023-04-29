from flask import Flask
from flask_restful import Resource , Api
from flask import request, render_template
from flask_cors import CORS
import json as json
import csv


    
        
    


skills_app = Flask(__name__)

CORS(skills_app)
api = Api(skills_app)

class prediction(Resource):
    def get(self,asin):
        a = hybridRecomm(asin)
        jsn = json.dumps(a.tolist())
        return jsn

api.add_resource(prediction,'/prediction/<string:asin>')






@skills_app.route("/")
def homepage():
    return render_template('index.html')


@skills_app.route("/addRow" , methods =["POST"])
def writeToCSV ():
    df5= pd.read_csv('C:\\Users\\Sigma\\ecommerce\\university_records.csv')
    row1 = request.form['row1']
    row2 = request.form['row2']
    row3 = request.form['row3']
    row4 = request.form['row4']
    
    

    df6 = pd.DataFrame({
    "Name": [row1],
    "Branch": [row2],
    "Year": [row3],
    "CGPA": [row4]
    }, index=[len(df5.index)])
    #
    # Append a dataframe
    #
    df5 = df5.append(df6 )
    
    
  
    df5.to_csv('C:\\Users\\Sigma\\ecommerce\\university_records.csv',index=False)
    return 'done'
# @skills_app.route("/skill")
# def skill():
#     return "skill"

if __name__ == "__main__":
    skills_app.run(debug = True , port=9000)
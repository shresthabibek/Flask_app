from flask import Flask, request
import pickle

# main variable to use.
app = Flask(__name__)

with open('classifier.pkl', 'rb') as f:
    model = pickle.load(f)


# start creating end-points.
@app.route("/", methods=['GET'])
def hello():
    return "<h1> Loan Approval Application! V2 </h1>"

@app.route("/predict", methods=['GET'])
def predict():
    return "I will make the predictions."

@app.route("/predict", methods=['POST'])
def predict_post():
    loan_req = request.get_json()
    
    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1

    if loan_req['Married'] == "No":
        Married = 0
    else:
        Married = 1

    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount']
    CreditHistory= loan_req['CreditHistory'] 

    input_data = [Gender, Married, ApplicantIncome, LoanAmount, CreditHistory]

    res = model.predict([input_data])

    if res[0] == 1:
        pred = "Approved"
    else:
        pred = "Rejected"

    
    return {"loan_approval_status":pred}
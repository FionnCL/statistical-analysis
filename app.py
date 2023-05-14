from flask import Flask, request
import NumberOfSamples as NoS

app = Flask(__name__)

# Sampling
@app.route("/sampling/sampleSizeCombinatorics", methods=['POST'])
# def info():
def sampleSizeCombinatorics():
    if request.method != 'POST':
        return "Incorrect request type."
    
    littleN = request.form['littleN']
    bigN = request.form['bigN']

    return {
        "orderedNoRep": NoS.orderedNoRep(littleN, bigN),
        "unorderedNoRep": NoS.unorderedNoRep(littleN, bigN),
        "orderedRep": NoS.orderedRep(littleN, bigN),
        "unorderedRep": NoS.unorderedRep(littleN, bigN),
    }
    

# # Linear Regression
# @app.route("/linear-regression/predictedValues", method='POST')
#     def predictedValues():

# @app.route("/linear-regression/model", method='POST')
#     def model():
    
# @app.route("/linear-regression/residuals", method='POST')
#     def residuals():
    
    
# # Hypothesis Testing
# @app.route("/hypothesis-testing/chi-squared", method='POST')
#     def chiSquared():
    

# #Estimation
# @app.route("/estimation/sampleSize", method='POST')
#     def sampleSize():

# @app.route("/estimation/standardError", method='POST')
#     def standardError():
    
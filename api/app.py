from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
import NumberOfSamples as NoS
import LinearRegressionModel as LRM
import LRMPredictedValues as LRMPVs
import Residuals as Residuals
import ChiSquared as Chi
import SampleSize as SS

# creates api app
app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])
api = Api(app)

# Sampling
class sampleSizeCombinatorics(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('littleN', required = True)
        parser.add_argument('bigN', required = True)
        args = parser.parse_args()

        littleN = int(args['littleN'])
        bigN = int(args['bigN'])

        return {
            "orderedNoRep": round(NoS.orderedNoRep(littleN, bigN), 4),
            "unorderedNoRep": round(NoS.unorderedNoRep(littleN, bigN), 4),
            "orderedRep": round(NoS.orderedRep(littleN, bigN), 4),
            "unorderedRep": round(NoS.unorderedRep(littleN, bigN), 4)
        }
    
# Linear Regression
class predictedValues(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('xList', required = True)
        parser.add_argument('yList', required = True)
        parser.add_argument('dependentVariables', required = True)
        args = parser.parse_args()

        xList = list(map(float, args['xList'].strip('][').split(',')))
        yList = list(map(float, args['yList'].strip('][').split(',')))
        dependentVariables = list(map(float, args['dependentVariables'].strip('][').split(',')))

        means = LRM.getMeans(xList, yList)
        beta = LRM.getBeta(xList, yList, means[0], means[1])
        alpha = LRM.getAlpha(means[0], means[1], beta)
        return {
            "values": LRMPVs.getValues(dependentVariables, alpha, beta),
        }

class model(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('xList', required = True)
        parser.add_argument('yList', required = True)
        args = parser.parse_args()

        xList = list(map(float, args['xList'].strip('][').split(',')))
        yList = list(map(float, args['yList'].strip('][').split(',')))

        means = LRM.getMeans(xList, yList)
        beta = LRM.getBeta(xList, yList, means[0], means[1])
        alpha = LRM.getAlpha(means[0], means[1], beta)
        return {
            "xBar": round(means[0], 4),
            "xBar": round(means[1], 4),
            "beta": round(beta, 4),
            "alpha": round(alpha, 4),
            "correlation": round(LRM.getSampleCovariance(xList, yList, means[0], means[1]), 4),
            "populationCovariance": round(LRM.getPopulationCovariance(xList, yList, means[0], means[1]), 4),
            "sampleCovariance": round(LRM.getSampleCovariance(xList, yList, means[0], means[1]), 4),
            "populationVarianceX": round(LRM.getPopulationVariance(xList, means[0]), 4),
            "populationVarianceY": round(LRM.getPopulationVariance(yList, means[1]), 4),
            "sampleVarianceX": round(LRM.getSampleVariance(xList, means[0]), 4),
            "sampleVarianceY": round(LRM.getSampleVariance(yList, means[1]), 4)
        }

class residuals(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('xList', required = True)
        parser.add_argument('yList', required = True)
        args = parser.parse_args()

        xList = list(map(float, args['xList'].strip('][').split(',')))
        yList = list(map(float, args['yList'].strip('][').split(',')))

        means = LRM.getMeans(xList, yList)
        beta = LRM.getBeta(xList, yList, means[0], means[1])
        alpha = LRM.getAlpha(means[0], means[1], beta)
        estimates = Residuals.getEstimatedY(xList, alpha, beta)
        tss = Residuals.getTSS(yList, means[1])
        rss = Residuals.getRSS(yList, estimates)
        ess = Residuals.getESS(yList, estimates, means[1])
        rSquared = ess / tss
        return {
            "estimates": estimates,
            "residuals": Residuals.getResiduals(yList, estimates),
            "tss": round(tss, 4),
            "rss": round(rss, 4),
            "ess": round(ess, 4),
            "r^2": round(rSquared, 4),
        }
    
# Hypothesis Testing
class chiSquared(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('matrix', required = True)
        args = parser.parse_args()

        matrix = create2dMatrix(args['matrix'])
        expectedFrequencies = Chi.getExpectedFrequencies(matrix)
        return {
            "observedFrequencies": matrix,
            "expectedFrequencies": expectedFrequencies,
            "chi^2": Chi.getChiSquared(matrix, expectedFrequencies)
        }
    
def create2dMatrix(matrix):
    array = []
    curr = ""
    for i in range(len(matrix) - 1):
        if not(matrix[i] == "[") and not(matrix[i] == "]"):
            curr += matrix[i]

        if((matrix[i] == "]")):
            array.append(curr)
            curr = ""
    
    for i in range(len(array)):
        if(array[i][0] == ","):
            array[i] = array[i][1:]

    for i in range(len(array)):
        array[i] = list(map(float, array[i].split(",")))

    return array
    


#Estimation
class sampleSize(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('maxWidthOfCI', required = True)
        parser.add_argument('variance', required = True)
        parser.add_argument('zScore', required = True)
        args = parser.parse_args()

        maxWidthOfCI = float(args['maxWidthOfCI'])
        variance = float(args['variance'])
        zScore = float(args['zScore']) # z >> (Alpha/2)

        return {
            "sampleSize": SS.getSampleSize(maxWidthOfCI, variance, zScore)
        }
    
# class standardError(Resource):
#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('littleN', required = True)
#         parser.add_argument('bigN', required = True)
#         args = parser.parse_args()

#         littleN = args['littleN']
#         bigN = args['bigN']

#         return {
#             "orderedNoRep": NoS.orderedNoRep(littleN, bigN),
#             "unorderedNoRep": NoS.unorderedNoRep(littleN, bigN),
#             "orderedRep": NoS.orderedRep(littleN, bigN),
#             "unorderedRep": NoS.unorderedRep(littleN, bigN),
#         }
    
# Add Endpoints
api.add_resource(sampleSizeCombinatorics, '/sampling/sample-size-combinatorics')
api.add_resource(predictedValues, '/lrm/predicted-values')
api.add_resource(model, '/lrm/model')
api.add_resource(residuals, '/lrm/residuals')
api.add_resource(chiSquared, '/hypothesis-testing/chi-squared')
api.add_resource(sampleSize, '/estimation/sample-size')
#api.add_resource(standardError, '/estimation/standard-error')

# runs program if running from this file
if __name__ == '__main__':
    app.run(port=4000, debug=True)
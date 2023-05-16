from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
import NumberOfSamples as NoS
import LinearRegressionModel as LRM
import LRMPredictedValues as LRMPVs
import Residuals as Residuals

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

        littleN = args['littleN']
        bigN = args['bigN']

        return {
            "orderedNoRep": NoS.orderedNoRep(littleN, bigN),
            "unorderedNoRep": NoS.unorderedNoRep(littleN, bigN),
            "orderedRep": NoS.orderedRep(littleN, bigN),
            "unorderedRep": NoS.unorderedRep(littleN, bigN),
        }
    
# Linear Regression
class predictedValues(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('xList', required = True)
        parser.add_argument('yList', required = True)
        parser.add_argument('dependentVariables', required = True)
        args = parser.parse_args()

        xList = (int)(args['xList'])
        yList = (int)(args['yList'])
        dependentVariables = args['dependentVariables']

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

        xList = args['xList'].strip('][').split(',')
        yList = args['yList'].strip('][').split(',')

        return yList
        # means = LRM.getMeans(xList, yList)
        # beta = LRM.getBeta(xList, yList, means[0], means[1])
        # alpha = LRM.getAlpha(means[0], means[1], beta)
        # return {
        #     "xBar": means[0],
        #     "xBar": means[1],
        #     "beta": beta,
        #     "alpha": alpha,
        #     "correlation": LRM.getSampleCovariance(xList, yList, means[0], means[1]),
        #     "populationCovariance": LRM.getPopulationCovariance(xList, yList, means[0], means[1]),
        #     "sampleCovariance": LRM.getSampleCovariance(xList, yList, means[0], means[1]),
        #     "populationVarianceX": LRM.getPopulationVariance(xList, means[0]),
        #     "populationVarianceY": LRM.getPopulationVariance(yList, means[1]),
        #     "sampleVarianceX": LRM.getSampleVariance(xList, means[0]),
        #     "sampleVarianceY": LRM.getSampleVariance(yList, means[1]),
        # }

class residuals(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('xList', required = True)
        parser.add_argument('yList', required = True)
        args = parser.parse_args()

        xList = (int)(args['xList'])
        yList = (int)(args['yList'])

        means = LRM.getMeans(xList, yList)
        beta = LRM.getBeta(xList, yList, means[0], means[1])
        alpha = LRM.getAlpha(means[0], means[1], beta)
        estimates = Residuals.getEstimatedY(xList, alpha, beta)
        tss = Residuals.getESS(yList, means[1])
        rss = Residuals.getRSS(yList, estimates)
        ess = Residuals.getESS(yList, estimates, means[1])
        rSquared = ess / tss
        return {
            "estimates": estimates,
            "residuals": Residuals.getResiduals(yList, estimates),
            "tss": tss,
            "rss": rss,
            "ess": ess,
            "r^2": rSquared
        }
    
# # Hypothesis Testing
# class chiSquared(Resource):
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

# #Estimation
# class sampleSize(Resource):
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

# runs program if running from this file
if __name__ == '__main__':
    app.run(port=4000, debug=True)
import 
{
    Chart as ChartJS,
    LinearScale,
    PointElement,
    LineElement,
    Tooltip,
    Legend,
  } 
  from 'chart.js';
  
  import { Scatter } from 'react-chartjs-2';

import './LRM.css';
import { useState } from 'react';

export default function LRM(){
    ChartJS.register(LinearScale, PointElement, LineElement, Tooltip, Legend);
    let [explanatory, setExplanatory] = useState("");
    let [response, setResponse] = useState("");
    let [results, setResults] = useState({});

    const testX = [0.56,0.23,1.56,0.07,0.13,1.72,0.46,1.27,0.69,0.45,1.22,0.36,0.40,0.11,0.56];
    const testY = [2.18,-0.66,0.21,-2.51,-2.63,1.27,-0.17,0.78,0.02,-0.63,0.07,0.46,-0.04,-3.57,1.63];

    let pairs = testX.map((val, index) => {
        return {
            x: val, 
            y: testY[index]
        }
    });

    let data = {
        datasets: [
            {
                label: 'Points',
                data: pairs,
                backgroundColor: 'rgba(99, 132, 255, 1)',
            }
          ],
        };
        
    let getResults = ((results) => {
        return(
            <div className="container results">
                <p>x̄:&nbsp;{results.xBar}</p>
                <p>ȳ:&nbsp;{results.yBar}</p>
                <p>β:&nbsp;{results.beta}</p>
                <p>α:&nbsp;{results.alpha}</p>
                <p>ρ:&nbsp;{results.correlation}</p>
                <p>Population Covariance:&nbsp;{results.populationCovariance}</p>
                <p>Sample Covariance:&nbsp;{results.sampleCovariance}</p>
                <p>Population Variance(X):&nbsp;{results.populationVarianceX}</p>
                <p>Population Variance(Y):&nbsp;{results.populationVarianceY}</p>
                <p>Sample Variance(X):&nbsp;{results.sampleVarianceX}</p>
                <p>Sample Variance(Y):&nbsp;{results.sampleVarianceY}</p>
            </div>
        );
    });

    // let results = {
    //     "xBar": 2.0,
    //     "yBar": 2.0,
    //     "beta": -1.0,
    //     "alpha": 4.0,
    //     "correlation": -1.0,
    //     "populationCovariance": -0.6667,
    //     "sampleCovariance": -1.0,
    //     "populationVarianceX": 0.6667,
    //     "populationVarianceY": 0.6667,
    //     "sampleVarianceX": 1.0,
    //     "sampleVarianceY": 1.0
    // }

    async function getInfo(endpoint, data){
        console.log("DATA: " + JSON.stringify(data));
        if(!stringIsValid(explanatory) && !stringIsValid(response)) { return "Invalid string."; }
        const res = await fetch('http://fionncl.pythonanywhere.com' + endpoint, {
            method: "POST",
            mode: "no-cors",
            headers: {
                "Content-Type": "application/json"
            },
            body: data
        })

        console.log(res);
        setResults(res);
    }

    function parseData(){
        if(document.getElementById("explanatory") === null || document.getElementById("response") === null ) { return; }

        return JSON.parse(`{"xList": "[${explanatory.split(",").toString()}]","yList": "[${response.split(",").toString()}]"}`)
    }

    function updateText(){
        setExplanatory(document.getElementById("explanatory").value);
        setResponse(document.getElementById("response").value);

        console.log("EXPLANATORY: " + explanatory);
        console.log("RESPONSE: " + response);
    }

    // Perhaps maybe doesn't work.
    function stringIsValid(string) {
        const list = string.split(",");
        console.log(list);
        for(let i = 0; i < list.length; i++){
            if(isNaN(parseFloat(list[i]))) { return false }
        }
        return true;
    }

    return(
        <div className="col">
            <div className="container">
                <h1>LRM Points</h1>
                <form className="lrm-form">
                    <div className='form-input'>
                        <label>Explanatory Variables:</label>
                        <textarea id="explanatory" className="lrm-form-input" type="text" onChange={updateText}/>
                    </div>
                    <div className='form-input'>
                        <label>Response Variables:</label>
                        <textarea id="response" className="lrm-form-input" type="text" onChange={updateText}/>
                    </div>
                </form>
                <button 
                    className="lrm-form-button" 
                    onClick={() => {
                        getInfo(
                            "/lrm/model", 
                            parseData()
                        )
                    }
                }>
                    Submit
                </button>
            </div>
            {getResults(results)}
            <Scatter data={data}/>
        </div>
    );
}
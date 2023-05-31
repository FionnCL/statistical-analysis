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
        console.log(results);
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

    let results = {
        "xBar": 0,
        "yBar": -0.24,
        "beta": 1.7021,
        "alpha": -1.3464,
        "correlation": 0.486,
        "populationCovariance": 0.4536,
        "sampleCovariance": 0.486,
        "populationVarianceX": 0.2665,
        "populationVarianceY": 2.3905,
        "sampleVarianceX": 0.2855,
        "sampleVarianceY": 2.5612
    }

    async function getInfo(endpoint, data){
        if(!stringIsValid(explanatory) && !stringIsValid(response)) { return "Invalid string."; }

        console.log(data);

        let res = await fetch(('http://fionncl.pythonanywhere.com' + endpoint), {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data)
        });
        getResults(res.json());
        // .then((res) => {
        //     console.log(res);
        // }).then((res) => {
        //     results = res;
        //     getResults(results);
        //     console.log(results);
        // });
    }

    function parseData(){
        if(document.getElementById("explanatory") === null || document.getElementById("response") === null ) { return; }

        return {
            "xList": "[" + explanatory.split(",").toString() + "]",
            "yList": "[" + response.split(",").toString() + "]"
        }
    }

    function updateText(){
        setExplanatory(document.getElementById("explanatory").value);
        setResponse(document.getElementById("response").value);
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
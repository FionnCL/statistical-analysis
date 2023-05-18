import React, { useState } from "react";
import './LRM.css';

export default function LRM(){
    const re = /[^0-9a-zA-Z]/;
    // let [inputtingAnswers, setInputtingAnswers] = useState();
    let explanatory = "";
    let response = "";

    async function getInfo(endpoint, data){
        // if(!stringValid(explanatory) && stringValid(response)) { return "Invalid string."; }
        const res = await fetch('http://127.0.0.1:4000' + endpoint, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        return res.json();
    }

    function onInput(){
        explanatory = document.getElementById("explanatory").value;
        response = document.getElementById("response").value;
    }

    function stringValid(string) {
        const list = string.split(",");
        console.log(list);
        for(let i = 0; i < list.length; i++){
            if(isNaN(parseFloat(list[i]))) { return false }
        }
        return true;
    }

    function createResults(){
        return(
            <div className="container">
                    
            </div>
        );
    }

    return(
        <div>
            <div className="container">
                {/* title can be props */}
                <h1>Linear Regression Model</h1>
                {/* These forms can be props. */}
                <form className="lrm-form">
                    <label>Explanatory Variables:</label>
                    <textarea id="explanatory" className="lrm-form-input" type="text" onChange={onInput}/>

                    <label>Response Variables:</label>
                    <textarea id="response" className="lrm-form-input" type="text" onChange={onInput}/>

                    <input 
                    className="lrm-form-button" 
                    type="submit" 
                    // onClick={
                    //     getInfo(
                    //         "/lrm/model", 
                    //         { 
                    //             "xList": explanatory, 
                    //             "yList": response
                    //         }
                    //     )
                    // }
                    />
                </form>
            </div>
            {/* {createResults} */}
        </div>
    );
}
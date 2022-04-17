function displayRadioValue1(){
    var score = 0;
    var ele = document.querySelectorAll("select[data-q='1']");
    var result = document.getElementById("result1");
    for(i = 0; i < ele.length; i++) { 
        score+=parseInt(ele[i].options[ele[i].selectedIndex].value)
    }
    result.innerHTML = "Résultat du QCM : " + score + "/15";
}

function displayRadioValue2(){
    var score = 0;
    var ele = document.querySelectorAll("select[data-q='1']");
    var result = document.getElementById("result2");
    for(i = 0; i < ele.length; i++) { 
        score+=parseInt(ele[i].options[ele[i].selectedIndex].value)
    }
    result.innerHTML = "Résultat du QCM : " + score + "/10";
}
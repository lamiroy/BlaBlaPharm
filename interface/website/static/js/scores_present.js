function displayRadioValue1(){
    var score = 0;
    var ele = document.querySelectorAll("select[data-q='1']");
    var result = document.getElementById("result1");
    for(i = 0; i < ele.length; i++) { 
        score+=parseInt(ele[i].options[ele[i].selectedIndex].value)
    }
    result.innerHTML = "Résultat du QCM : " + score + "/6";
}


function displayTextValue2(){

    var score = 0;
    let elements = [];
    for(i=0;i<6;i++){
        elements.push(document.getElementById("q2-text-".concat("",i+1)))
    }
    var responses = ["Do you live","Do you live","Does he go","Do you work","Do you have","Does she come"]
    for(i=0;i<elements.length;i++){
        if(elements[i].value.localeCompare(responses[i])==0){
            score += 1
        }
    }
    var result = document.getElementById("result2") ;
    result.innerHTML = "Résultat du QCM : " + score + "/6";
}


function displayRadioValue3(){
    var score = 0;
    var ele = document.querySelectorAll("select[data-q='3']");
    var result = document.getElementById("result3");
    for(i = 0; i < ele.length; i++) { 
        score+=parseInt(ele[i].options[ele[i].selectedIndex].value)
    }
    result.innerHTML = "Résultat du QCM : " + score + "/6";
}

function displayTextValue4(){

    var score = 0;
    let elements = [];
    for(i=0;i<6;i++){
        elements.push(document.getElementById("q4-text-".concat("",i+1)))
    }
    var responses = ["doesn't play","don't eat","doesn't live","don't see","doesn't like","don't think"]
    for(i=0;i<elements.length;i++){
        if(elements[i].value.localeCompare(responses[i])==0){
            score += 1
        }
    }
    var result = document.getElementById("result4") ;
    result.innerHTML = "Résultat du QCM : " + score + "/6";
}

function displayRadioValue5(){
    var score = 0;
    var ele = document.querySelectorAll('input[type=radio]')
    var result = document.getElementById("result5");
    for(i = 0; i < ele.length; i++){ 
        if(ele[i].checked){   
            score+=parseInt(ele[i].value)
        }
    }
    result.innerHTML = "Résultat du QCM : " + score + "/5";
}

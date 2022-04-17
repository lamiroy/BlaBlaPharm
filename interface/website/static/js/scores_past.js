function displayTextValue1(){

    var score = 0;
    let elements = [];
    for(i=0;i<6;i++){
        elements.push(document.getElementById("q2-text-".concat("",i+1)))
    }
    var responses = ["have been exercising","was chatting","have been practicing","have been seing","was not sleeping","was thinking","has been digging"]
    for(i=0;i<elements.length;i++){
        if(elements[i].value.localeCompare(responses[i])==0){
            score += 1
        }
    }
    var result = document.getElementById("result1") ;
    result.innerHTML = "Résultat du QCM : " + score + "/7";
}
function displayTextValue2(){

    var score = 0;
    let elements = [];
    for(i=0;i<6;i++){
        elements.push(document.getElementById("q2-text-".concat("",i+1)))
    }
    var responses = ["had left","got","met","had seen","was","had ever been","had said","had","had finished","asked","had just reached","told","had done","decided","didn't want","had just cleaned","was","had forgotten","got","had red"]
    for(i=0;i<elements.length;i++){
        if(elements[i].value.localeCompare(responses[i])==0){
            score += 1
        }
    }
    var result = document.getElementById("result2") ;
    result.innerHTML = "Résultat du QCM : " + score + "/20";
}
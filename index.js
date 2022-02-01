


var switch_value
var button_start_event = document.getElementsByClassName("button-start")
function run(){
    

    //POE A pica de escrever no json antes de executa o programa

    
    const {ipcRenderer} = require('electron')
    // Synchronous message emmiter and handler

    // Async message sender
    button_start_event.onclick(ipcRenderer.send('asynchronous-message', 'sezo'));
    

    
};

function get_switch_value(){
    switch_value = document.getElementById("switch").value;
    console.log(switch_value);
};



/*const btn = document.querySelector("#send");

btn.addEventListener("click", function(e){
    e.preventDefault();
   
    const name = document.querySelector("#name");

    var value = name.value;

    console.log(value);
   

})
  
// module.exports = { value };
// function createID(champion) {
//     champion = value
// }

// function main(){
//     data = fazGet("http://localhost:8080/create-id")
//     id = JSON.parse(data)
// }

// main()*/

const btn = document.querySelector("#send");

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

// main()
// Data types
/*
1.String
2.Integers/Numbers
3.Booleans
4.Arrays
5.Objects
*/

let name ="Tracy"
let height =50

// Onclick events
// Element selctor in JS
function submit (){
    var input=document.getElementById("inputField").value;
    var input= parseInt(input); // data type conversion
    var input = input+1
    console.log(input)

}
let adult = true; // boolean data type
let fruits = ['kiwi', 'pineapple' , 'apple', 30, false] //this is an array or list
let person ={
   firstname: 'Rihanna'
   lastname: 'Lovelace'
   age: 18,
   address:{
    country:'Sudan'
    city: 'Khartoum'
    street:'Bani Bani'
    
   },
   children:['Kelly' , 'Vince']

}
function saveitem(){
    var input=document.getElementById("inputfield").value
    localStorage.setitem('inputItem', input);
    showWelcomeMessage(input)
}
function showWelcomeMessage(inputField){
    var messageElement.textContent="We hav esaved your input as " + input;
}
var storeditem= localStorage.getItem('inputItem');
if(storeditem){
    showWelcomeMessage(storeditem)
}




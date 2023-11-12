let age ='';
// first question---------------------------------
while (true) {
age = prompt("Please enter your age using digits only:");
if (age === null) {
    break;
}
age = Number(age);
if (isNaN(age) || age <= 0) {
    alert("Invalid input. Please enter a positive number.");
    continue;
}
if (age >= 1 && age <= 10) {
    alert(`You are a child.`);
} else if (age >= 11 && age <= 18) {
    alert(`You are a teenager.`);
} else if (age >= 19 && age <= 50) {
    alert(`You are a grown up.`);
} else {
    alert(`You are a old.`);
}
}

// second question----------------------------------
let statment = prompt("Please enter a string:");
const vowels = "aeouiAEOUI";
const A = "aA";
const E = "eE"; 
const O = "oO";
const U = "uU";
const I = "iI";
let vowel = 0;
let a = 0;
let e = 0;
let o = 0;
let u = 0;
let i = 0;
for(let x = 0; x < statment.length; x++){
    if(vowels.indexOf(statment[x]) !== -1){
        vowel++;
    }
    if(A.indexOf(statment[x]) !== -1){
        a++;
    }
    if(E.indexOf(statment[x]) !== -1){
        e++;
    }
    if(O.indexOf(statment[x]) !== -1){
        o++;
    }
    if(U.indexOf(statment[x]) !== -1){
        u++;
    }
    if(I.indexOf(statment[x]) !== -1){
        i++;
    }
}
alert(`The number of vowels in the string is: ${vowel}, 
a= ${a},  e= ${e},  o= ${o},  u= ${u}   and    i= ${i}.`);


// third question----------------------------------
let hour = prompt("please enter the time from 0 to 24");
hour = Number(hour)
if(hour==0 || hour==24){
    alert(`It's 12 AM.`)
}else if(hour==12){
    alert(`It's 12 PM.`)
}else if (hour>=1 && hour<=11){
    alert(`It's ${hour} AM.`)
}else if (hour>=13 && hour<=23){
    alert(`It's ${hour - 12} PM.`)
}

// fourth question----------------------------------
let word = prompt("Please enter the string you converted:");
alert(`the result is ${word.charAt(0).toUpperCase() + word.slice(1)}.` )



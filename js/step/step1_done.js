const sol_2557 = () => {
    console.log("Hello World!");
}

const sol_10718 =() =>{
    const str = "강한친구 대한육군";
    console.log(`${str}\n${str}`);
}

const sol_10171 =() =>{
    const str=`\\    /\\
 )  ( ')
(  /  )
 \\(__)|
`;
    console.log(str);
}

const sol_10172 =() =>{
    const str=`|\\_/|
|q p|   /}
( 0 )"""\\
|"^"\`    |
||_/=\\\\__|`;
    console.log(str);
}

// A+B
const sol_1000 = () =>{
    const fs = require('fs');
    const input = fs.readFileSync('/dev/stdin').toString().split(' ');
    const [a, b] = [Number(input[0]), Number(input[1])];
    console.log(a+b);
}

// A-B
const sol_1001 = ()=>{
    const fs = require('fs');
    const input = fs.readFileSync(0, 'utf8').split(' ');
    // const input = fs.readFileSync('/dev/stdin').toString().split(' ');
    const [a, b] = [Number(input[0]), Number(input[1])];
    console.log(a-b);
} 

// A*B
const sol_10998 = ()=>{
    const fs = require('fs');
    const input = fs.readFileSync(0, 'utf8').split(' ');
    // const input = fs.readFileSync('/dev/stdin').toString().split(' ');
    const [a, b] = [Number(input[0]), Number(input[1])];
    console.log(a*b);
} 

const sol_1008 = ()=>{
    const fs = require('fs'); 
    const input = fs.readFileSync(0, 'utf8').split(' ');
    console.log(Number(input[0])/Number(input[1]));
} 

const sol_10869 = ()=>{
    //첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다
    const fs = require('fs'); 
    const input = fs.readFileSync(0, 'utf8').split(' ');
    console.log(Number(input[0])+Number(input[1]));
    console.log(Number(input[0])-Number(input[1]));
    console.log(Number(input[0])*Number(input[1]));
    console.log(parseInt(Number(input[0])/Number(input[1])));
    console.log(Number(input[0])%Number(input[1]));
}

const sol_10926 = () =>{
    const fs = require('fs');
    // string trim()!!!!
    const input = fs.readFileSync("/dev/stdin").toString().trim();
    console.log(`${input}??!`);
}

const sol_10430 = () =>{
    /*
    입력: A B C
    출력: 
    첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 
    셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C
    */

    const fs = require('fs');
    const [A,B,C] = fs.readFileSync("/dev/stdin").toString().split(' ').map(i=>Number(i));
    console.log((A+B)%C);
    console.log(((A%C) + (B%C))%C);
    console.log((A*B)%C);
    console.log(((A%C) * (B%C))%C);
}

const sol_18108 = () => {
    const fs = require('fs');
    const input = Number(fs.readFileSync("/dev/stdin").toString().trim());
    const diff = 2541-1998;
    console.log(input-diff);
}

const sol_2588 = () =>{
    const fs = require('fs');
    const [A,B] = fs.readFileSync("/dev/stdin").toString().split('\n').map(i=>Number(i));
    const [b1, b2, b3] = B.toString().split('').map(i=>Number(i));
    console.log(A*b3);
    console.log(A*b2);
    console.log(A*b1);
    console.log(A*B);
}

const sol_25083 = () =>{
    const str = `         ,r'"7
r\`-_   ,'  ,/
 \\. ". L_r'
   \`~\\/
      |
      |`;
    console.log(str);
}

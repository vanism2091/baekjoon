const sol_2739 = () =>{
    const fs = require('fs');
    const num = Number(fs.readFileSync(0).toString().trim());
    for (let i = 1; i< 10; i++){
        console.log(`${num} * ${i} = ${num*i}`);
    }
}
const sol_10950 = () =>{
    const fs = require('fs');
    const sep = '\n';
    const [n, ...cases] = fs.readFileSync(0).toString().trim().split(sep);
    for (let i = 0; i < n; i++){
        const [a, b] = cases[i].split(' ').map(Number);
        console.log(a+b);
    }
}
const sol_8393 = (num) =>{
    const fs = require('fs');
    const num = Number(fs.readFileSync(0).toString().trim());
    console.log((num * (num+1)) / 2);
}

// 빠른 A+B
const sol_15552 = () =>{
    const fs = require('fs');
    const sep = '\n';
    const [n, ...cases] = fs.readFileSync(0).toString().trim().split(sep);
    let ans = '';
    for (let i = 0; i < n; i++){
        const [a, b] = cases[i].split(' ').map(Number);
        ans+=`${a+b}\n`;
    }
    console.log(ans);
}

// N 찍기
// https://www.acmicpc.net/problem/2741
const sol_2741 = () =>{
    const fs = require('fs');
    const num = Number(fs.readFileSync(0).toString().trim());
    let res = '';
    for (let i = 1; i <= n; i++){
        res+=`${i}\n`;
    }
    console.log(res);
}


// 기찍 N
// https://www.acmicpc.net/problem/2742
const sol_2742 = () =>{
    const fs = require('fs');
    const num = Number(fs.readFileSync(0).toString().trim());
    let res = '';
    for (let i = num; i > 0; i--){
        res+=`${i}\n`;
    }
    console.log(res);
}

// A+B - 7
// https://www.acmicpc.net/problem/11021
const sol_11021 = () =>{
    const fs = require('fs');
    const sep = '\n';
    const [n, ...cases] = fs.readFileSync(0).toString().trim().split(sep);
    let ans = '';
    for (let i = 0; i < n; i++){
        const [a, b] = cases[i].split(' ').map(Number);
        ans+=`Case #${i+1}: ${a+b}\n`;
    }
    console.log(ans);
}

// A+B - 8
// https://www.acmicpc.net/problem/11022
const sol_11022 = () =>{
    const fs = require('fs');
    const sep = '\n';
    const [n, ...cases] = fs.readFileSync(0).toString().trim().split(sep);
    let ans = '';
    for (let i = 0; i < n; i++){
        const [a, b] = cases[i].split(' ').map(Number);
        ans+=`Case #${i+1}: ${a} + ${b} = ${a+b}\n`;
    }
    console.log(ans);
}

// 별 찍기 - 1
// https://www.acmicpc.net/problem/2438
const sol_2438 = () =>{
    const fs = require('fs');
    const num = Number(fs.readFileSync(0).toString().trim());
    let res = "";
    for (let i = 1; i <= num; i++){
        let star = "";
        for (let j=1; j <= i; j++){
            star += "*";
        }
        res += `${star}\n`;
    }
    console.log(res);
}

// 별 찍기 - 2
// https://www.acmicpc.net/problem/2439
const sol_2439 = () =>{
    const fs = require('fs');
    const num = Number(fs.readFileSync(0).toString().trim());
    let res = "";
    for (let i = 1; i <= num; i++){
        let s = "";
        for (let j=0; j < num-i; j++){
            s += " ";
        }
        for (let j=0; j < i; j++){
            s += "*";
        }
        res += `${s}\n`;
    }
    console.log(res);

}

// X보다 작은 수
// https://www.acmicpc.net/problem/10871
const sol_10871 = () =>{
    // 첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
    // 둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 
    // 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.
    // 10 5
    // 1 10 4 9 2 3 8 5 7 6
    // output
    // 1 4 2 3
    const fs = require('fs');
    const sep = '\n';
    const [n, numArrayString] = fs.readFileSync(0).toString().trim().split(sep);
    const [_, x] = n.split(' ').map(Number);
    let res = '';
    for (const numStr of numArrayString.split(' ')){
        const num = Number(numStr);
        if (num >= x) continue;
        res += `${num} `;
    }
    console.log(res.trim());
}

// A+B - 5
// https://www.acmicpc.net/problem/10952
const sol_10952 = () =>{
    const fs = require('fs');
    const sep = '\n';
    const cases = fs.readFileSync(0).toString().trim().split(sep);
    let res = '';
    while(cases.length){
        const [a, b] = cases.shift().split(" ").map(Number);
        if (a === 0 && b === 0) break;
        res += `${a+b}\n`;
    }
    console.log(res);
}

// A+B - 4
// https://www.acmicpc.net/problem/10951
const sol_10951 = () =>{
    const fs = require('fs');
    const sep = '\n';
    const cases = fs.readFileSync(0).toString().trim().split(sep);
    let res = '';
    while(cases.length){
        const [a, b] = cases.shift().split(" ").map(Number);
        res += `${a+b}\n`;
    }
    console.log(res);
}
const sol_1110 = () =>{
    const fs = require('fs');
    const sep = '\n';
    const [A,B] = fs.readFileSync(0).toString().trim().split(sep).map(Number);

}

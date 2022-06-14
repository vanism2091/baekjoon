// 단계별로 풀어보기 - 4_1차원_배열
// https://www.acmicpc.net/step/6

// TODO: 내 코드가 속도가 느린데, 다른 사람 코드 보면서 차이점 확인 및 왜 더 느리고 빠른지 time complexity 분석하자.

// 최소, 최대
// https://www.acmicpc.net/problem/10818
// 596 / 400
// 1. Infinity? -> 1000000 :: 속도 596 -> 572  ( 무의미 )
// 2. trim() 제거 :: 572 -> 597 (무의미)
// 3. for ... of -> for :: 597 -> 472 
// for ... of 문이 확실히 느리구나 :) 다른 문제들을 돌려봤을 땐 크게 유의미한 차이는 없었는데, 테스트 케이스의 갯수 차이일수도.
const sol_10818 = () => {
    const fs = require('fs');
    const sep = '\n';
    const [n, numArrayString] = fs.readFileSync(0).toString().trim().split(sep);
    let [min, max] = [Infinity, -Infinity];
    for (const numStr of numArrayString.split(" ")){
        const currNum = Number(numStr);
        if (min > currNum) min = currNum;
        if (max < currNum) max = currNum;
    }
    console.log(`${min} ${max}`);
}

// 최댓값
// https://www.acmicpc.net/problem/2562
// 이건 빠른 분들과 속도 차이가 유의미하지는 않은듯. 116 / 100
const sol_2562 = () => {
    const fs = require('fs');
    const sep = '\n';
    const numArr = fs.readFileSync(0).toString().trim().split(sep).map(Number);
    let [maxIdx, maxNum] = [-1, -Infinity];
    for (let i = 0; i < numArr.length; i++){
        if(numArr[i] > maxNum) {
            maxNum = numArr[i];
            maxIdx = i+1;
        }
    }
    console.log(`${maxNum}\n${maxIdx}`);
}

// 숫자의 개수
// https://www.acmicpc.net/problem/2577
// 120 / 40 3배 차이 
// 1. for ... of -> for :: ?? 차이가 없어요 ㅋㅋㅋㅋ
// 최근 푼 사람 중 가장 빠른 사람은 100 정도라 비교할 의미가 없을 듯.
const sol_2577 = () => {
    const fs = require('fs');
    const sep = '\n';
    const calcResStr = fs.readFileSync(0).toString().trim().split(sep).reduce(((acc, val) => acc*=+val), 1).toString();
    const resArr = Array(10).fill(0);
    for (const a of calcResStr){
        resArr[a] += 1;
    }
    console.log(resArr.join('\n'));
}

// 나머지 
// https://www.acmicpc.net/problem/3052
// 120, 9324 / 96, 7076 
// 1. for..of -> for :: 똑같은데..? 이전에는 왜..?
// 2. Number, +, parseInt 이 문제 내에서는 속도에서 큰 차이는 없음.(채점이 빨리 되는걸로 봐서 test case가 작은듯)
// 3. Set -> Array: 차이 없음..:)
const sol_3052 = () => {
    const fs = require('fs');
    const sep = '\n';
    const arr = fs.readFileSync(0).toString().trim().split(sep);
    const remainders = new Set();
    for (const num of arr){
        remainders.add(+num % 42)
    }
    console.log(remainders.size)
}
const sol_3052_2 = () => {
    const fs = require('fs');
    const sep = '\n';
    const arr = fs.readFileSync(0).toString().trim().split(sep);
    const remainders = [];
    for (let i=0; i< arr.length; i++){
        const remainder = +arr[i] % 42;
        if(!remainders.includes(remainder)) remainders.push(remainder);
    }
    console.log(remainders.length)
}

// 평균
// https://www.acmicpc.net/problem/1546
// 124, 9660 / 112, 9620 큰 차이 X
const sol_1546 = () => {
    const fs = require('fs');
    const sep = '\n';
    const [n, scores] = fs.readFileSync(0).toString().trim().split(sep);
    const scoresArr = scores.split(" ").map(Number);
    const maxScore = Math.max(...scoresArr);
    let sum = 0;
    for (const score of scoresArr){
        sum += score/maxScore*100;
    }
    console.log(sum/+n);
}

// OX퀴즈
// https://www.acmicpc.net/problem/8958
// 132, 9372 / 104, 9540
// 1. map 함수 추가해서 length 1번만 사용 :: 132 -> 124 .. 큰 의미 없을듯
const sol_8958 = () => {
    const fs = require('fs');
    const sep = '\n';
    const [n, ...cases] = fs.readFileSync(0).toString().trim().split(sep);
    let res = ""
    for (let i = 0; i < +n; i++){
        const score = cases[i].split("X").map(i=>i.length).reduce((acc, val) => acc+=(val*(val+1)/2), 0)
        res+=`${score}\n`;
    }
    console.log(res);
}

// 평균은 넘겠지
// https://www.acmicpc.net/problem/4344
// 176, 11248 / 104, 9724
const sol_4344 = () => {
    const fs = require('fs');
    const sep = '\n';
    const [caseNum, ...cases] = fs.readFileSync(0).toString().trim().split(sep);
    let res = "";
    for (let i = 0; i < +caseNum; i++){
        const [n, ...scores] = cases[i].split(" ").map(Number);
        const avg = scores.reduce((acc, val)=>acc+=val, 0) / n;
        const aboveAvg = scores.reduce((acc, val)=>{
            if (val > avg) acc += 1;
            return acc;
        }, 0) / n * 100;
        res += `${aboveAvg.toFixed(3)}%\n`;
    }
    console.log(res);
}
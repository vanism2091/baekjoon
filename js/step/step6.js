// 단계별로 풀어보기 - 6_문자열
// https://www.acmicpc.net/step/7

// 아스키 코드
// https://www.acmicpc.net/problem/11654
const sol_11654 = () => {
    const input = require('fs').readFileSync(0).toString().trim();
    console.log(input.charCodeAt(0));
}

// 숫자의 합
// https://www.acmicpc.net/problem/11720
const sol_11720 = () => {
    const fs = require('fs');
    const sep = '\n';
    const [n, numString] = fs.readFileSync(0).toString().trim().split(sep);
    let res = 0;
    for (let i=0; i < +n; i++){
        res+=+numString[i];
    }
    console.log(res);
}

// 알파벳 찾기
// https://www.acmicpc.net/problem/10809
const sol_10809 = () => {
    const input = require('fs').readFileSync(0).toString().trim();
    const res = Array(26).fill(-1);
    const aIdx = "a".charCodeAt(0);
    for(let i=0; i<input.length; i++){
        const idx = input[i].charCodeAt(0) - aIdx;
        if( res[idx] === -1) res[idx] = i;
    }
    console.log(res.join(' '));
}

// 문자열 반복
// https://www.acmicpc.net/problem/2675
const sol_2675 = () => {
    const fs = require('fs');
    const sep = '\n';
    const [n, ...cases] = fs.readFileSync(0).toString().trim().split(sep);
    const res = [];
    for(let i=0; i<+n; i++){
        const [num, str] = cases[i].split(" ");
        let tempRes = "";
        for(let j=0; j<str.length; j++){
            for(let k=0; k<+num; k++){
                tempRes += str[j];
            }
        }
        res.push(tempRes);
    }
    console.log(res.join('\n'));
}

// 단어 공부
// https://www.acmicpc.net/problem/1157
// 188, 12028 / 168, 9672
const sol_1157 = () => {
    const fs = require('fs');
    const word = fs.readFileSync(0).toString().trim();
    const charArray = Array(26).fill(0);
    const getCharIdx = char => (char.charCodeAt(0) - "A".charCodeAt(0))%32;
    for (let i=0; i<word.length; i++){
        charArray[getCharIdx(word[i])] += 1;
    }
    const maxCnt = Math.max(...charArray);
    let resChar = "";
    for (let i=0; i<charArray.length; i++){
        if (maxCnt !== charArray[i]) continue;
        if (resChar !== "") resChar = "?";
        else resChar = String.fromCharCode(i+65);
    }
    console.log(resChar);
}


// 단어의 개수
// https://www.acmicpc.net/problem/1152
const sol_1152 = () => {
    const fs = require('fs');
    const words = fs.readFileSync(0).toString().trim();
    const resArr = words.split(" ");
    console.log(resArr[0] === "" ? 0 : resArr.length);
}

// https://www.acmicpc.net/problem/2908
const sol_2908 = () => {
    const fs = require('fs');
    const [a, b] = fs.readFileSync(0).toString().trim().split(" ");
    const getReversedNum = (str) => +str.split("").reverse().join("");
    if (getReversedNum(a) > getReversedNum(b)) console.log(getReversedNum(a));
    else console.log(getReversedNum(b));
}

// https://www.acmicpc.net/problem/5622
const sol_5622 = () => {
    const fs = require('fs');
    const target = fs.readFileSync(0).toString().trim();
    const refArray = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10];
    let res = 0;
    for (let i=0; i<target.length; i++){
        res += refArray[target[i].charCodeAt(0) - 65];
    }
    console.log(res);
}

// https://www.acmicpc.net/problem/2941
const sol_2941 = () => {
    const fs = require('fs');
    const target = fs.readFileSync(0).toString().trim();
    const repArray = ["dz=","c=","c-","d-","lj","nj","s=","z="];
    let res = [target];
    const getResArrAndCurrLeng = (arr, sep) => {
        const temp = [];
        for (let i=0; i<arr.length; i++){
            if(arr[i].length < 2) temp.push(arr[i]);
            else temp.push(...arr[i].split(sep));
        }
        return [temp, temp.length - arr.length];
    }
    let totalNum = 0;
    for (let i = 0; i<repArray.length; i++){
        let currLeng;
        [res, currLeng] = getResArrAndCurrLeng(res, repArray[i]);
        totalNum += currLeng;
    }
    totalNum += res.join("").length;
    console.log(totalNum);
}

// 그룹 단어 체커
// https://www.acmicpc.net/problem/1316
const sol_1316 = () => {
    const fs = require('fs');
    const sep = '\n';
    const [n, ...cases] = fs.readFileSync(0).toString().trim().split(sep);
    let res = 0;
    for (let i = 0; i < +n; i++){
        let isGroupWord = true;
        let left = 0;
        const charSet = new Set([cases[i][left]]);
        for (let right = 1; right < cases[i].length; right++){
            if (cases[i][left] === cases[i][right]) continue;
            left = right;
            if (charSet.has(cases[i][left])) {
                isGroupWord = false;
                break;
            }
            charSet.add(cases[i][left]);
        }
        if (isGroupWord) res++;
    }
    console.log(res)
}
// 단계별로 풀어보기 - 5_함수
// https://www.acmicpc.net/step/5

// 정수 N개의 합
// https://www.acmicpc.net/problem/15596
const sol_15596 = () =>{
/*
    JS가 없어서 파이썬으로 해결
    def solve(a):
        ans = 0
        for x in a:
            ans += x
        return ans
 */
}

// 셀프 넘버
// https://www.acmicpc.net/problem/4673
// 240, 12364 / 152, 10208
// 비교 ㄱㄱ https://www.acmicpc.net/source/37119273
const sol_4673 = () =>{
    // 10,000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 증가하는 순서로 출력한다.
    const a = [...Array(10000).keys()];
    
    const d = n => n+ n.toString().split("").reduce((acc, val)=>acc+=+val, 0);
    const removeGenerated = (arr, first) => {
        if (first === 0) return;
        let temp = d(first);
        while (temp < 10000){
            arr[temp] = 0;
            temp = d(temp);
        }
    }
    for (let i = 0; i < 10000; i++){
        removeGenerated(a, a[i]);
    }
    console.log(a.filter(i=>i).join('\n'));
}

// 한수
// https://www.acmicpc.net/problem/1065
// 128, 9760 / 112, 7368 
// 비교 ㄱㄱ https://www.acmicpc.net/source/19980506
const sol_1065 = () =>{
    const fs = require('fs');
    const num = Number(fs.readFileSync(0).toString().trim());

    if (num < 100) {
        console.log(num);
        return;
    };

    let cnt = 99;
    const isHansu = (n) =>{
        const [a, b, c] = n.toString();
        if (+b-+a === +c-+b) return true;
        else false;
    }

    for (let i = 111; i<= num; i++){
        if(isHansu(i)) cnt++;
    }
    console.log(cnt);
}
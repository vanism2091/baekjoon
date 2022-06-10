const sol_1330 = () =>{
    const fs = require('fs');
    const sep = ' ';
    const [A,B] = fs.readFileSync("/dev/stdin").toString().split(sep).map(i=>Number(i));
    if (A > B) console.log('>');
    else if (A < B) console.log('<');
    else console.log('==');
}

//시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
const sol_9498 = () =>{
    const fs = require('fs');
    const score = Number(fs.readFileSync("/dev/stdin").toString());
    if (score >= 90) console.log('A');
    else if (score >= 80) console.log('B');
    else if (score >= 70) console.log('C');
    else if (score >= 60) console.log('D');
    else console.log('F');
}

const sol_2753 = () =>{
    // 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
    // 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
    
    const fs = require('fs');
    const year = Number(fs.readFileSync("/dev/stdin").toString());

    if ( year%400 === 0 || (year%100 !== 0 && year%4 === 0)) console.log(1);
    else console.log(0);
}

const sol_14681 = () =>{
    // 점 (x, y)의 사분면 번호(1, 2, 3, 4 중 하나)를 출력한다.
    // const fs = require('fs');
    // const [x, y] = fs.readFileSync(0).toString().trim().split('\n').map(Number);
    const fs = require('fs');
    const sep = '\n';
    const [A,B] = fs.readFileSync(0).toString().trim().split(sep).map(Number);
    if (A > 0){
        if (B>0) console.log(1);
        else console.log(4);
    }else {
        if(B<0) console.log(3);
        else console.log(2);
    }
}

const sol_2884 = () => {
    //첫째 줄에 상근이가 창영이의 방법을 사용할 때, 설정해야 하는 알람 시간을 출력한다. (입력과 같은 형태로 출력하면 된다.)
    const fs = require('fs');
    const sep = ' ';
    const diff = 45;
    const [h,m] = fs.readFileSync(0).toString().trim().split(sep).map(Number);
    if (m>=diff) console.log(`${h} ${m-diff}`);
    else console.log(`${(h+23)%24} ${m+60-diff}`);
}

const sol_2525 = () => {

    const fs = require('fs');
    const [hm,c] = fs.readFileSync(0).toString().trim().split('\n');
    const [h, m] = hm.split(' ').map(Number);
    const [addh, addm] = [parseInt(c/60), parseInt(c%60)];
    console.log(`${(h+addh+parseInt((m+addm)/60))%24} ${(m+addm)%60}`);
}

const sol_2480 = () =>{
    const fs = require('fs');
    const sep = ' ';
    const nums = fs.readFileSync(0).toString().trim().split(sep).map(Number);
    const map1 = new Map();
    for (const num of nums){
        if(map1.get(num) === undefined) map1.set(num, 1);
        else map1.set(num, map1.get(num)+1);
    }

    switch (map1.size){
        case 1:
            console.log(10000+(nums[0]*1000));
            break;
        case 2:
            const [a, b] = Array.from(map1.keys());
            const target1 = map1.get(a) > map1.get(b) ? a : b;
            console.log(1000 + (target1*100));
            break;
        case 3:
            const target2 = Math.max(...map1.keys());
            console.log(target2*100);
            break;
        default:
            break;
    }
}
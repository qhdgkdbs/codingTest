function solution(lottos, win_nums) {
    let answer = [];
    let zero = 0
    let match = 0
    // 몇개 맞았는지.
    // 0의 개수

    for(let i of lottos){
        if(!i){
            zero += 1
            continue
        }

        if(win_nums.includes(i)){
            match += 1
        }
    }

    const win = [6,6,5,4,3,2,1]

    answer.push(win[match+zero])
    answer.push(win[match])



    return answer;
}


function solution(lottos, win_nums) {
    const rank = [6, 6, 5, 4, 3, 2, 1];

    let minCount = lottos.filter(v => win_nums.includes(v)).length;
    let zeroCount = lottos.filter(v => !v).length;

    const maxCount = minCount + zeroCount;

    return [rank[maxCount], rank[minCount]];
}

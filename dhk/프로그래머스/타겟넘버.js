function solution(numbers, target) {
    let rst = 0;
    let arr = [numbers[0], -numbers[0]];

    // 2개 이상 20개 이하
    for (let i = 1; i < numbers.length; i++) {
        let tmp = [];
        for (let num of arr) {
            tmp.push(num + numbers[i]);
            tmp.push(num - numbers[i]);
        }
        arr = tmp;
    }

    return arr.filter((x) => x === target).length;
}

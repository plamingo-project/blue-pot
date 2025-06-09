//readline 모듈 불러오기
const readline = require("readline");
//인터페이스 객체 생성하기
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
//입출력 처리하는 코드
rl.on("line", function (line) {
    //입력 처리하는 코드
    console.log(line); //입력 출력
    rl.close();
}).on("close", function () {
    //입력을 받은 뒤 실행할 코드
    process.exit(); //종료문
});

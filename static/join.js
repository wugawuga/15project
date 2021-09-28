let loginBox = document.querySelector('.outBox');
let loginInputBox = document.querySelector('#email');
loginInputBox.addEventListener('keyup', function(){
    if(!loginInputBox.value == ''){
        //빈 값이 아닌 경우
        loginBox.classList.add('existence');   
    }else{
        //빈 값인 경우
        loginBox.classList.remove('existence');   
    }
});
window.onload = function() {
    main();
};

function main() {
    // const emailMobileRequiredErrorBtn = document.querySelector('#emailMobileRequiredError');
    const numberInp = document.querySelector('#number');
    const passwordInp = document.querySelector('#password');
    const loginBtn = document.querySelector('#loginBtn');
    const okBtn = document.querySelector('#okBtn')
    const showPasswordBtn = document.querySelector('#showPassword')
    showPasswordBtn.style.display = 'none'

    loginBtn.addEventListener('click', function() {
        const numberInpVal = numberInp.value;
        const passwordInpVal = passwordInp.value;

        if(numberInpVal === '' && passwordInpVal === '') {
            emailMobileRequiredErrorBtn.style.display = 'block';
        }
    })
    okBtn.addEventListener('click', function() {
        emailMobileRequiredErrorBtn.style.display = 'none';
    })

    passwordInp.addEventListener('click', function() {
        showPasswordBtn.style.display = 'block'
    })

    showPasswordBtn.addEventListener('click', function() {
        if (passwordInp.type === "password") {
            passwordInp.type = "text";
        } else {
            passwordInp.type = "password";
        }
    })
    

}



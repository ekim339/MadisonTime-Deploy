//DOM Elements
const mainpage = document.querySelector('.main-page');
const loginpage = document.querySelector('.login-page');
const middleContent = document.querySelector('.middle-content');
const btnTop = document.querySelector('.btn-top');
const newsFeedPage = document.querySelector('.feeds-page');
const loginModal = document.querySelector('.login-modal');

/***************************************/
/***************************************/

//Main page
const goToLoginPage = () => {};
mainpage.style.display = 'none';
loginpage.style.display = 'grid';

middleContent.addEventListener('click', (e) => {
    if (e.target.classList[1] === 'main-btn') {
        goToLoginPage();
    }
});
btnTop.addEventListener('click', () => {
    const inputUserInfo = document.querySelector('.user-info');
    const inputPassword = document.querySelector('.password');

    if (inputUserInfo.value !=="" && inputPassword.value !=="") {
        mainpage.style.display = 'none';
        newsFeedPage.style.display = 'block';
    } else {
        goToLoginPage();
        loginModal.style.display = 'block';
    }
});
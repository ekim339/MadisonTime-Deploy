const btnAddCourse = document.querySelector('.add-course-btn');
const modalAdd = document.querySelector('.modal');
const modalWrapper = document.querySelector('.modal-wrapper');
const addModalX = document.querySelector('.modal-header i');
const btnM = document.querySelector('.m-button');
const btnT = document.querySelector('.t-button');
const btnW = document.querySelector('.w-button');
const btnTh = document.querySelector('.th-button');
const btnF = document.querySelector('.f-button');
const btnS = document.querySelector('.s-button');
const btnSu = document.querySelector('.su-button');
const btnAdd = document.querySelector('.add');
// const courseName;
const tbxCourseName = document.querySelector('.course-name-input');
// const location;
const tbxLocation = document.querySelector('.location-input');
// const from;
const timeFrom = document.querySelector('.from-input');
// const to;
const timeTo = document.querySelector('.to-input');
// const courseColor;
const clrCourse = document.querySelector('.course-color');

/*************************************************/
/*************************************************/

// Add modal
btnAddCourse.addEventListener('click', () => {
  modalAdd.style.display = 'block';
  modalWrapper.classList.add('modal-wrapper-display');
})

addModalX.addEventListener('click', () => {
  modalAdd.style.display = 'none';
  modalWrapper.classList.remove('modal-wrapper-display');
});

// days button
function clicked(button) {
  button.classList.toggle('active');
}

btnM.addEventListener('click', function(){
  clicked(btnM);
});


btnT.addEventListener('click', function(){
  clicked(btnT);
});

btnW.addEventListener('click', function(){
  clicked(btnW);
});

btnTh.addEventListener('click', function(){
  clicked(btnTh);
});

btnF.addEventListener('click', function(){
  clicked(btnF);
});

btnS.addEventListener('click', function(){
  clicked(btnS);
});

btnSu.addEventListener('click', function(){
  clicked(btnSu);
});

// add button

btnM.addEventListener('click', () => {
  const courseName = tbxCourseName.value;
  const location = tbxLocation.value;
});
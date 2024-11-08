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
const tbxCourseName = document.querySelector('.course-name-input');
const tbxLocation = document.querySelector('.location-input');
const timeFrom = document.querySelector('.from-input');
const timeTo = document.querySelector('.to-input');
const clrCourse = document.querySelector('.course-color');
const mon = document.querySelector('mon');
const tue = document.querySelector('tue');
const wed = document.querySelector('wed');
const thu = document.querySelector('thu');
const fri = document.querySelector('fri');
const sat = document.querySelector('sat');
const sun = document.querySelector('sun');
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

btnAdd.addEventListener('click', () => {
  const courseName = tbxCourseName.value;
  const location = tbxLocation.value;
  const from = timeFrom.value;
  const to = timeTo.value;
  const color = clrCourse.value;
  createCourse(checkDays(), courseName, location, from, to, color);
});

function checkDays(){
  const days = [];
  if (btnM.classList.contains('active')){
    days.push(mon);
  }
  if (btnT.classList.contains('active')){
    days.push(tue);
  }
  if (btnW.classList.contains('active')){
    days.push(wed);
  }
  if (btnTh.classList.contains('active')){
    days.push(thu);
  }
  if (btnF.classList.contains('active')){
    days.push(fri);
  }
  if (btnS.classList.contains('active')){
    days.push(sat);
  }
  if (btnS.classList.contains('active')){
    days.push(sun);
  }
  return days;
}

function createCourse(daysArray, courseName, location, from, to, color){
  for (var i=0; i<array.length; i++){
    var course = document.createElement('div');
    course.style.backgroundColor(color);
    course.innerHTML += courseName;
    course.innerHtml += location;
    daysArray[i].append(course);
  }
  
}
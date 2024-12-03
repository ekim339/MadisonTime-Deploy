const btnAddCourse = document.querySelector('.add-course-btn');
const modalAdd = document.querySelector('.modal');
const modalWrapper = document.querySelector('.modal-wrapper');
const addModalX = document.querySelector('.modal-header i');
const monInput = document.getElementById('mon');
const tueInput = document.getElementById('tue');
const wedInput = document.getElementById('wed');
const thuInput = document.getElementById('thu');
const friInput = document.getElementById('fri');
const satInput = document.getElementById('sat');
const sunInput = document.getElementById('sun');
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
const monBox = document.querySelector('.monday');
const tueBox = document.querySelector('.tuesday');
const wedBox = document.querySelector('.wednesday');
const thuBox = document.querySelector('.thursday');
const friBox = document.querySelector('.friday');
const satBox = document.querySelector('.saturday');
const sunBox = document.querySelector('.sunday');
const modalCourse = document.querySelector('.course-modal');
const modalCourseWrapper = document.querySelector('.course-modal-wrapper');
const course = document.querySelector('.course');
const btnCM = document.querySelector('.c-m-button');
const btnCT = document.querySelector('.c-t-button');
const btnCW = document.querySelector('.c-w-button');
const btnCTh = document.querySelector('.c-th-button');
const btnCF = document.querySelector('.c-f-button');
const btnCS = document.querySelector('.c-s-button');
const btnCSu = document.querySelector('.c-su-button');
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

function updateInputField(button, inputField){
  if (button.classList.contains('active')) {
    inputField.value = "True"; // Set to True if active
  } else {
      inputField.value = "False"; // Set to False if not active
  }
}

btnM.addEventListener('click', function(){
  clicked(btnM);
  updateInputField(btnM, monInput);
});


btnT.addEventListener('click', function(){
  clicked(btnT);
  updateInputField(btnT, tueInput);
});

btnW.addEventListener('click', function(){
  clicked(btnW);
  updateInputField(btnW, wedInput);
});

btnTh.addEventListener('click', function(){
  clicked(btnTh);
  updateInputField(btnTh, thuInput);
});

btnF.addEventListener('click', function(){
  clicked(btnF);
  updateInputField(btnF, friInput);
});

btnS.addEventListener('click', function(){
  clicked(btnS);
  updateInputField(btnS, satInput);
});

btnSu.addEventListener('click', function(){
  clicked(btnSu);
  updateInputField(btnSu, sunInput);
});

// btnAdd.addEventListener('click', () => {
//   const courseName = tbxCourseName.value;
//   const location = tbxLocation.value;
//   const from = timeFrom.value;
//   const to = timeTo.value;
//   const color = clrCourse.value;
//   createCourse(checkDays(), courseName, location, from, to, color);

//   // Clear inputs
//   tbxCourseName.value = '';
//   tbxLocation.value = '';
//   timeFrom.value = '';
//   timeTo.value = '';
//   clrCourse.value = '#ff0000';

//   // Close modal
//   modalAdd.style.display = 'none';
//   modalWrapper.classList.remove('modal-wrapper-display');
// });

// btnAdd.addEventListener('click', (e) => {
//   const form = document.querySelector('form');
//   form.addEventListener('submit', (event) => {
//     const errors = document.querySelectorAll('.error-message');
    
//     // Prevent closing the modal if there are validation errors
//     if (errors.length !== 0) {
//       e.preventDefault();// Stop form submission
//       modalAdd.style.display = 'block';
//       modalWrapper.classList.add('modal-wrapper-display');
//     }
//     else{
//       // tbxCourseName.value = '';
//       // tbxLocation.value = '';
//       // timeFrom.value = '';
//       // timeTo.value = '';
//       // clrCourse.value = '#ff0000';
//       form.submit()
//       modalAdd.style.display = 'none';
//       modalWrapper.classList.remove('modal-wrapper-display');
//     }
//   });
// });

// // const form = document.querySelector('form');

// form.addEventListener('submit', (e) => {
//   const errors = document.querySelectorAll('.error-message');

//   // Prevent closing the modal if there are validation errors
//   if (errors.length !== 0) {
//     e.preventDefault(); // Stop form submission
//     modalAdd.style.display = 'block';
//     modalWrapper.classList.add('modal-wrapper-display');
//   } else {
//     // Proceed with submission
//     modalAdd.style.display = 'none';
//     modalWrapper.classList.remove('modal-wrapper-display');
//   }
// });


// function checkDays(){
//   const days = [];
//   if (btnM.classList.contains('active')){
//     days.push(monBox);
//   }
//   if (btnT.classList.contains('active')){
//     days.push(tueBox);
//   }
//   if (btnW.classList.contains('active')){
//     days.push(wedBox);
//   }
//   if (btnTh.classList.contains('active')){
//     days.push(thuBox);
//   }
//   if (btnF.classList.contains('active')){
//     days.push(friBox);
//   }
//   if (btnS.classList.contains('active')){
//     days.push(satBox);
//   }
//   if (btnS.classList.contains('active')){
//     days.push(suBoxn);
//   }
//   return days;
// }

// function createCourse(daysArray, courseName, location, from, to, color){
//   for (var i = 0; i < daysArray.length; i++) {
//     var course = document.createElement('div');
//     course.style.backgroundColor = color;
//     course.innerHTML = `
//         <div>${courseName}</div>
//         <div>${location}</div>
//         <div>${from} - ${to}</div>
//     `;
//     course.classList.add('course');
//     daysArray[i].append(course);
// }
  
// Course detail modal
// course.addEventListener('click', () => {
//   console.log('hi');
//   modalCourse.style.display = 'block';
//   modalCourseWrapper.classList.add('modal-course-wrapper-display');
// })

function showModal(courseId, name, location, timeFrom, timeTo, color, mon, tue, wed, thu, fri, sat, sun) {
  // Show modal
  modalCourse.style.display = 'block';
  modalCourseWrapper.classList.add('course-modal-wrapper-display');
  modalCourseWrapper.style.visibility = 'visible';

  // Populate modal content
  document.getElementById('modal-course-name').textContent = name;
  document.getElementById('modal-course-location').textContent = location;
  document.getElementById('modal-course-time-from').textContent = timeFrom;
  document.getElementById('modal-course-time-to').textContent = timeTo;
  document.getElementById('modal-course-color').style.backgroundColor = color;
  console.log(mon);
  pressButton(mon, btnCM);
  pressButton(tue, btnCT);
  pressButton(wed, btnCW);
  pressButton(thu, btnCTh);
  pressButton(fri, btnCF);
  pressButton(sat, btnCS);
  pressButton(sun, btnCSu);
  modalCourseWrapper.style.display = 'flex'; // Use flex to center the modal

  // set course edit link and delete link
  document.getElementById('edit-course-link').href = `?edit_course=${courseId}`;
  document.getElementById('delete-course-link').href = `${courseId}/delete/`;
}

function pressButton(input, button){
  if (input == "True"){
    if (!button.classList.contains('active')){
      clicked(button);
    }
  } else{
    if (button.classList.contains('active')){
      button.classList.remove('active');
    }
  }
}

function closeModal() {
  // Hide modal
  modalCourseWrapper.style.visibility = 'hidden';
  modalCourseWrapper.style.display = 'none';
}

// Close modal if clicked outside of it
window.onclick = function (event) {
  if (event.target === courseModalWrapper) {
    modalCourseWrapper.style.display = 'none';
  }
};
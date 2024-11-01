const btnAddCourse = document.querySelector('.add-course-btn');
const modalAdd = document.querySelector('.modal');
const modalWrapper = document.querySelector('.modal-wrapper');
const addModalX = document.querySelector('.modal-header i');
const btnAdd = document.querySelector('.add');
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
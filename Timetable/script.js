const btnAdd = document.querySelector('add-course-btn');
const modalAdd = document.querySelector('.modal');

/*************************************************/
/*************************************************/

// Default display
btnAdd.addEventListener('click', () => {
  modal.style.displat = 'block';
  modal.classList.add('modal-wrapper-display');
})
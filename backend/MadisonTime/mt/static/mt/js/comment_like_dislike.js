// grab CSRF token from cookie
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}
const csrftoken = getCookie('csrftoken');

async function postJSON(url) {
  const res = await fetch(url, {
    method: 'POST',
    headers: {'X-CSRFToken': csrftoken},
  });
  if (!res.ok) throw new Error('Network error');
  return res.json();
}



document.addEventListener('click', async (e) => {
  const upBtn = e.target.closest('.thumb-up');
  const downBtn = e.target.closest('.thumb-down');
  if (!upBtn && !downBtn) return;

  const wrapper = e.target.closest('.thumbs');
  const id = wrapper.dataset.commentId;
  const likesEl = wrapper.querySelector('.likes-count');
  const dislikesEl = wrapper.querySelector('.dislikes-count');

  try {
    if (upBtn) {
      const data = await postJSON(`/comments/${id}/like/`);
      likesEl.textContent = data.likes;
      if (dislikesEl && typeof data.dislikes === 'number') {
        dislikesEl.textContent = data.dislikes;
      }
    } else if (downBtn) {
      const data = await postJSON(`/comments/${id}/dislike/`);
      dislikesEl.textContent = data.dislikes;
      if (likesEl && typeof data.likes === 'number') {
        likesEl.textContent = data.likes;
      }
    }
  } catch (err) {
    console.error(err);
    alert('Sorry, something went wrong.');
  }
});


<script>
thumbs_up = document.querySelector('.fa-thumbs-up');
comment_Id = {{comment.id}}

thumbs_up.addEventListener('click', () => {
  thumbs_up.classList.toggle('liked');
});
</script>
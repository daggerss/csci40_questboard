const copyBtns = [...document.getElementsByClassName('copy-btn')]

copyBtns.forEach(btn=> btn.addEventListener('click', ()=>{
  const qbLink = btn.getAttribute('data-link')
  navigator.clipboard.writeText(qbLink)
  btn.value = 'Link copied!'
}))

function confirmFunction() {
    response = confirm("Are you sure you want to sign up for this quest?");
    if (response)
    {
      return true;
    }
    else
    {
      return false;
    }
  }
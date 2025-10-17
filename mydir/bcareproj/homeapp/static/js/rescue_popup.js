document.addEventListener('DOMContentLoaded', () => {
  const rescueBtn = document.querySelector('.rescue');     // The "Rescue Now" button on Home
  const rescuePopup = document.getElementById('rescuePopup');
  const closePopup = document.getElementById('closePopup');

  if (rescueBtn && rescuePopup) {
    rescueBtn.addEventListener('click', (e) => {
      e.preventDefault();                  // prevent jumping to top
      rescuePopup.style.display = 'flex';  // show popup
    });
  }

  if (closePopup && rescuePopup) {
    closePopup.addEventListener('click', () => {
      rescuePopup.style.display = 'none';  // hide popup
    });
  }

  // Close when clicking outside the box
  window.addEventListener('click', (e) => {
    if (e.target === rescuePopup) {
      rescuePopup.style.display = 'none';
    }
  });

  // Optional: Close on ESC
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && rescuePopup.style.display === 'flex') {
      rescuePopup.style.display = 'none';
    }
  });
});
// Add this at the end of your DOMContentLoaded
const loginBtn = document.querySelector('.popup-buttons a:last-child button');
if (loginBtn) {
    loginBtn.addEventListener('click', () => {
        window.location.href = '/login/?next=/rescue_form/';
    });
}

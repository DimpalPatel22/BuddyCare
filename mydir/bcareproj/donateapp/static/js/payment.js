// Toggle between UPI/Card methods
function toggleMethod(id) {
  document.querySelectorAll('.method-body').forEach(el => el.style.display = "none");
  document.getElementById(id).style.display = "block";
}

// Store the current OTP globally
let currentOtp = null;
let currentMethod = null;

// Generate OTP and show popup **only after validation**
function generateOtp(event, method){
  event.preventDefault(); // Prevent form submission

  // ----- VALIDATION -----
  if(method === 'UPI'){
    const upi = document.getElementById('upi_id').value.trim();
    const pattern = /^[\w.\-]{2,256}@[a-zA-Z]{2,64}$/; // username@bank
    if(!pattern.test(upi)){
      alert('Invalid UPI ID! Format should be username@bank.');
      document.getElementById('upi_id').focus();
      return false; // stop execution
    }
  }

  if(method === 'Card'){
    const number = document.getElementById('card_number').value.trim();
    const expiry = document.getElementById('expiry').value.trim();
    const cvv = document.getElementById('cvv').value.trim();

    const cardPattern = /^\d{16}$/;
    const cvvPattern = /^\d{3}$/;
    const expiryPattern = /^(0[1-9]|1[0-2])\/\d{2}$/;

    if(!cardPattern.test(number)){
      alert('Invalid card number! Must be 16 digits.');
      document.getElementById('card_number').focus();
      return false;
    }

    if(!expiryPattern.test(expiry)){
      alert('Invalid expiry! Use MM/YY format.');
      document.getElementById('expiry').focus();
      return false;
    }

    const [month, year] = expiry.split('/').map(Number);
    const now = new Date();
    const currentYear = now.getFullYear() % 100;
    const currentMonth = now.getMonth() + 1;
    if(year < currentYear || (year === currentYear && month < currentMonth)){
      alert('Card expiry must be in the future!');
      document.getElementById('expiry').focus();
      return false;
    }

    if(!cvvPattern.test(cvv)){
      alert('Invalid CVV! Must be 3 digits.');
      document.getElementById('cvv').focus();
      return false;
    }
  }

  // ----- IF VALID, GENERATE OTP -----
  currentMethod = method;
  currentOtp = Math.floor(1000 + Math.random() * 9000);

  document.getElementById('generatedOtp').innerText = currentOtp;
  document.getElementById('otp-method').value = method;
  document.getElementById('otpModal').style.display = "block";
}

// Close OTP popup
function closeOtp(){
  document.getElementById('otpModal').style.display = "none";
}

// Close modal if clicked outside
window.onclick = function(event) {
  const modal = document.getElementById('otpModal');
  if(event.target == modal){
    modal.style.display = "none";
  }
}

// Validate OTP before sending to backend
document.getElementById('otp-form').addEventListener('submit', function(e){
  e.preventDefault();
  const enteredOtp = e.target.otp.value.trim();

  if(enteredOtp == currentOtp){
    // OTP matches → submit form to backend
    e.target.submit();
  } else {
    alert("Invalid OTP! Please enter the correct OTP.");
  }
});

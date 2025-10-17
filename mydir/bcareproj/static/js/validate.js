document.addEventListener("DOMContentLoaded", function () {

    // --- Rescue Form ---
    const rescueForm = document.querySelector(".rescue-form");
    if (rescueForm) {
        rescueForm.addEventListener("submit", function(e){
            const contactInput = rescueForm.querySelector("input[name='contact']");
            if(contactInput && contactInput.value.trim() !== ""){
                const val = contactInput.value.trim();
                const phoneRegex = /^\d{10}$/;
                if(!phoneRegex.test(val) || /^(\d)\1{9}$/.test(val)){
                    alert("Please enter a valid 10-digit phone number");
                    e.preventDefault();
                    return;
                }
            }
        });
    }

    // --- Adopt Form ---
    const adoptForm = document.querySelector(".adopt-form-container form");
    if(adoptForm){
        adoptForm.addEventListener("submit", function(e){
            const emailInput = adoptForm.querySelector("input[name='email']");
            const phoneInput = adoptForm.querySelector("input[name='phone']");
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            const phoneRegex = /^\d{10}$/;

            if(!emailRegex.test(emailInput.value.trim())){
                alert("Please enter a valid email address");
                e.preventDefault();
                return;
            }

            if(!phoneRegex.test(phoneInput.value.trim())){
                alert("Please enter a valid 10-digit phone number");
                e.preventDefault();
                return;
            }
        });
    }

    // --- Donate Form ---
    const donateForm = document.querySelector(".donation-form");

    if (donateForm) {
        donateForm.addEventListener("submit", function(e) {
            const contactInput = donateForm.querySelector('input[name="contact"]');
            
            if(contactInput.value.trim() !== ""){
                const val = contactInput.value.trim();
                const phoneRegex = /^\d{10}$/;

                // Reject repeated digits like 1111111111
                if(!phoneRegex.test(val) || /^(\d)\1{9}$/.test(val)){
                    alert("Please enter a valid 10-digit phone number.");
                    e.preventDefault();
                    return;
                }
            }
        });
    }
    // --group form--
    const groupForm = document.querySelector(".group-form");
    if (groupForm) {
        groupForm.addEventListener("submit", function(e){
            const contactInput = groupForm.querySelector("input[name='contact']");
            if(contactInput && contactInput.value.trim() !== ""){
                const val = contactInput.value.trim();
                const phoneRegex = /^\d{10}$/;
                if(!phoneRegex.test(val) || /^(\d)\1{9}$/.test(val)){
                    alert("Please enter a valid 10-digit phone number");
                    e.preventDefault();
                    return;
                }
            }
        });
    }
    

});


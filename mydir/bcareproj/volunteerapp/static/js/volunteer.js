document.addEventListener("DOMContentLoaded", function () {
  const faqQuestions = document.querySelectorAll(".faq-question");

  faqQuestions.forEach((btn) => {
    btn.addEventListener("click", function () {
      const answer = this.nextElementSibling;
      const isOpen = answer.style.display === "block";

      // Close all answers
      document.querySelectorAll(".faq-answer").forEach(a => a.style.display = "none");
      document.querySelectorAll(".faq-question span").forEach(s => s.textContent = "+");

      // Toggle current one
      if (!isOpen) {
        answer.style.display = "block";
        this.querySelector("span").textContent = "−";
      }
    });
  });
});

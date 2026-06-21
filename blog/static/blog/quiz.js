document.addEventListener("click", (event) => {
    const selectedButton = event.target.closest(".quiz-option");

    if (!selectedButton) {
        return;
    }

    const card = selectedButton.closest(".quiz-card");
    const feedback = card.querySelector(".quiz-feedback");
    const correctAnswer = card.dataset.correct;
    const selectedAnswer = selectedButton.dataset.answer;

    card.querySelectorAll(".quiz-option").forEach((button) => {
        const isSelected = button === selectedButton;
        const isCorrect = button.dataset.answer === correctAnswer;

        button.classList.toggle("is-selected", isSelected);
        button.classList.toggle("is-correct", isCorrect);
        button.classList.toggle("is-wrong", isSelected && !isCorrect);
        button.setAttribute("aria-pressed", isSelected ? "true" : "false");
    });

    if (selectedAnswer === correctAnswer) {
        feedback.textContent = "Benar! Jawaban kamu tepat.";
        feedback.className = "quiz-feedback is-correct";
        return;
    }

    feedback.textContent = `Salah. Jawaban yang benar: ${correctAnswer}.`;
    feedback.className = "quiz-feedback is-wrong";
});

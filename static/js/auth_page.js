
// Переключение видимости пароля
document.getElementById('togglePassword').addEventListener('click', function() {
    const passwordInput = document.getElementById('password');
    const icon = this.querySelector('i');

    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        icon.classList.remove('bi-eye');
        icon.classList.add('bi-eye-slash');
    } else {
        passwordInput.type = 'password';
        icon.classList.remove('bi-eye-slash');
        icon.classList.add('bi-eye');
    }
});

// Переключение видимости подтверждения пароля
document.getElementById('toggleConfirmPassword').addEventListener('click', function() {
    const confirmPasswordInput = document.getElementById('confirmPassword');
    const icon = this.querySelector('i');

    if (confirmPasswordInput.type === 'password') {
        confirmPasswordInput.type = 'text';
        icon.classList.remove('bi-eye');
        icon.classList.add('bi-eye-slash');
    } else {
        confirmPasswordInput.type = 'password';
        icon.classList.remove('bi-eye-slash');
        icon.classList.add('bi-eye');
    }
});

// Валидация формы
document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault();

    let isValid = true;

    // Валидация имени
    const firstName = document.getElementById('firstName');
    const firstNameFeedback = document.getElementById('firstNameFeedback');
    if (firstName.value.trim() === '') {
        showError(firstName, firstNameFeedback, 'Пожалуйста, введите ваше имя');
        isValid = false;
    } else if (firstName.value.trim().length < 2) {
        showError(firstName, firstNameFeedback, 'Имя должно содержать не менее 2 символов');
        isValid = false;
    } else {
        showSuccess(firstName, firstNameFeedback, 'Отлично!');
    }

    // Валидация фамилии
    const lastName = document.getElementById('lastName');
    const lastNameFeedback = document.getElementById('lastNameFeedback');
    if (lastName.value.trim() === '') {
        showError(lastName, lastNameFeedback, 'Пожалуйста, введите вашу фамилию');
        isValid = false;
    } else if (lastName.value.trim().length < 2) {
        showError(lastName, lastNameFeedback, 'Фамилия должна содержать не менее 2 символов');
        isValid = false;
    } else {
        showSuccess(lastName, lastNameFeedback, 'Отлично!');
    }

    // Валидация класса
    const classSelect = document.getElementById('class');
    const classFeedback = document.getElementById('classFeedback');
    if (!classSelect.value) {
        showError(classSelect, classFeedback, 'Пожалуйста, выберите ваш класс');
        isValid = false;
    } else {
        showSuccess(classSelect, classFeedback, 'Отлично!');
    }

    // Валидация возраста
    const age = document.getElementById('age');
    const ageFeedback = document.getElementById('ageFeedback');
    if (!age.value) {
        showError(age, ageFeedback, 'Пожалуйста, введите ваш возраст');
        isValid = false;
    } else if (age.value < 12 || age.value > 18) {
        showError(age, ageFeedback, 'Возраст должен быть от 12 до 18 лет');
        isValid = false;
    } else {
        showSuccess(age, ageFeedback, 'Отлично!');
    }

    // Валидация email
    const email = document.getElementById('email');
    const emailFeedback = document.getElementById('emailFeedback');
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email.value) {
        showError(email, emailFeedback, 'Пожалуйста, введите email');
        isValid = false;
    } else if (!emailRegex.test(email.value)) {
        showError(email, emailFeedback, 'Пожалуйста, введите корректный email');
        isValid = false;
    } else {
        showSuccess(email, emailFeedback, 'Отлично!');
    }

    // Валидация пароля
    const password = document.getElementById('password');
    const passwordFeedback = document.getElementById('passwordFeedback');
    if (!password.value) {
        showError(password, passwordFeedback, 'Пожалуйста, придумайте пароль');
        isValid = false;
    } else if (password.value.length < 8) {
        showError(password, passwordFeedback, 'Пароль должен содержать не менее 8 символов');
        isValid = false;
    } else {
        showSuccess(password, passwordFeedback, 'Надежный пароль!');
    }

    // Валидация подтверждения пароля
    const confirmPassword = document.getElementById('confirmPassword');
    const confirmPasswordFeedback = document.getElementById('confirmPasswordFeedback');
    if (!confirmPassword.value) {
        showError(confirmPassword, confirmPasswordFeedback, 'Пожалуйста, подтвердите пароль');
        isValid = false;
    } else if (password.value !== confirmPassword.value) {
        showError(confirmPassword, confirmPasswordFeedback, 'Пароли не совпадают');
        isValid = false;
    } else {
        showSuccess(confirmPassword, confirmPasswordFeedback, 'Пароли совпадают!');
    }

    // Валидация согласия с условиями
    const termsCheck = document.getElementById('termsCheck');
    const termsFeedback = document.getElementById('termsFeedback');
    if (!termsCheck.checked) {
        showError(termsCheck, termsFeedback, 'Необходимо согласиться с условиями');
        isValid = false;
    } else {
        showSuccess(termsCheck, termsFeedback, '');
    }

    // Если форма валидна
    if (isValid) {
        // Здесь обычно отправка данных на сервер
        alert('Регистрация успешна! Данные отправлены на сервер.');
        // Сброс формы
        document.getElementById('registrationForm').reset();
        // Скрытие всех сообщений валидации
        document.querySelectorAll('.validation-feedback').forEach(el => {
            el.style.display = 'none';
        });
    }
});

// Функция показа ошибки
function showError(input, feedbackElement, message) {
    input.classList.add('is-invalid');
    input.classList.remove('is-valid');
    feedbackElement.textContent = message;
    feedbackElement.className = 'validation-feedback validation-invalid';
    feedbackElement.style.display = 'block';
}

// Функция показа успеха
function showSuccess(input, feedbackElement, message) {
    input.classList.remove('is-invalid');
    input.classList.add('is-valid');
    feedbackElement.textContent = message;
    feedbackElement.className = 'validation-feedback validation-valid';
    feedbackElement.style.display = 'block';
}

// Реальная валидация при вводе
document.querySelectorAll('#registrationForm input, #registrationForm select').forEach(input => {
    input.addEventListener('blur', function() {
        // Запускаем базовую валидацию при потере фокуса
        if (this.value.trim() !== '' || (this.type === 'checkbox' && this.checked)) {
            this.classList.remove('is-invalid');
            this.classList.add('is-valid');
        }
    });
});

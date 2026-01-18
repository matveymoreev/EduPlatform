
// Инициализация при загрузке страницы
document.getElementById('login-form').addEventListener('submit', function(event) {
    // Обработка формы входа
    const loginForm = document.getElementById('login-form');
    const errorMessage = document.getElementById('error-message');
    const errorText = document.getElementById('error-text');

    loginForm.addEventListener('submit', function(e) {
        // e.preventDefault();

        // Получаем значения полей
        // const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const password = document.getElementById('password').value.trim();

        // Простая валидация
        let isValid = true;
        let errorMsg = '';

//        if (!name) {
//            isValid = false;
//            errorMsg = 'Пожалуйста, введите имя и фамилию';
//        } else
        if (!email) {
            isValid = false;
            errorMsg = 'Пожалуйста, введите email';
        } else if (!isValidEmail(email)) {
            isValid = false;
            errorMsg = 'Пожалуйста, введите корректный email';
        } else if (!password) {
            isValid = false;
            errorMsg = 'Пожалуйста, введите пароль';
        } else if (password.length < 8) {
            isValid = false;
            errorMsg = 'Пароль должен содержать не менее 8 символов';
        }

        if (!isValid) {
            // errorText.textContent = errorMsg;
            errorMessage.style.display = 'block';
            return;
        }

        // Скрываем сообщение об ошибке, если валидация прошла
        // errorMessage.style.display = 'none';

        // В реальном приложении здесь был бы запрос к серверу
        // Для демонстрации просто показываем сообщение об успехе
        // alert(`Добро пожаловать! Вход выполнен успешно.`);

        // Здесь обычно происходит перенаправление на защищенную страницу
        // window.location.href = '/dashboard.html';
    });

    // Функция проверки email
    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    // Обработчики для социальных кнопок
    document.querySelectorAll('.social-btn').forEach(button => {
        button.addEventListener('click', function() {
            const platform = this.querySelector('i').className.split(' ')[1].replace('fa-', '');
            alert(`Вход через ${getPlatformName(platform)} временно недоступен. Используйте форму входа.`);
        });
    });

    // Функция для получения названия платформы
    function getPlatformName(className) {
        const platforms = {
            'google': 'Google',
            'vk': 'ВКонтакте',
            'yandex': 'Яндекс'
        };
        return platforms[className] || className;
    }

    // Обработчик для ссылки "Забыли пароль?"
    document.querySelector('.forgot-password').addEventListener('click', function(e) {
        // e.preventDefault();
        const email = document.getElementById('email').value.trim();

        if (email && isValidEmail(email)) {
            alert(`Инструкции по восстановлению пароля отправлены на ${email}`);
        } else {
            alert('Пожалуйста, введите ваш email для восстановления пароля');
        }
    });

    // Обработчик для ссылки "Зарегистрироваться"
    document.querySelector('.login-footer a').addEventListener('click', function(e) {
//        e.preventDefault();
//        alert('Переход на страницу регистрации. В реальном приложении здесь была бы ссылка на страницу регистрации.');
    });
});

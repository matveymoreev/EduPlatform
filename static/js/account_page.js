
document.addEventListener('DOMContentLoaded', function() {
    // Элементы профиля
    const userFullName = document.getElementById('userFullName');
    const userStatus = document.getElementById('userStatus');
    const coursesCount = document.getElementById('coursesCount');
    const hoursCount = document.getElementById('hoursCount');
    const progressPercent = document.getElementById('progressPercent');
    const activityBar = document.getElementById('activityBar');
    const todayActivity = document.getElementById('todayActivity');

    // Поля ввода
    const firstNameInput = document.getElementById('firstName');
    const lastNameInput = document.getElementById('lastName');
    const userEmailInput = document.getElementById('userEmail');
    const userClassSelect = document.getElementById('userClass');
    const aboutUserTextarea = document.getElementById('aboutUser');
    const inputCourses = document.getElementById('inputCourses');
    const inputHours = document.getElementById('inputHours');
    const inputProgress = document.getElementById('inputProgress');
    const inputActivity = document.getElementById('inputActivity');
    const saveButton = document.getElementById('saveButton');

    // Функция обновления имени
    function updateUserName() {
        const firstName = firstNameInput.value.trim();
        const lastName = lastNameInput.value.trim();

        if (firstName || lastName) {
            userFullName.textContent = `${firstName} ${lastName}`.trim();
            userFullName.classList.add('updating');
            setTimeout(() => userFullName.classList.remove('updating'), 500);
        } else {
            userFullName.textContent = 'Введите имя и фамилию';
        }
    }

    // Функция обновления статуса
    function updateUserStatus() {
        const userClass = userClassSelect.value;
        const about = aboutUserTextarea.value.trim();

        if (userClass) {
            userStatus.textContent = `${userClass} класс`;
            userStatus.classList.add('updating');
            setTimeout(() => userStatus.classList.remove('updating'), 500);
        } else if (about) {
            userStatus.textContent = about.length > 30 ? about.substring(0, 30) + '...' : about;
        } else {
            userStatus.textContent = 'Статус не указан';
        }
    }

    // Функция обновления статистики
    function updateStats() {
        const courses = parseInt(inputCourses.value) || 0;
        const hours = parseInt(inputHours.value) || 0;
        const progress = parseInt(inputProgress.value) || 0;
        const activity = parseInt(inputActivity.value) || 0;

        // Обновляем цифры
        coursesCount.textContent = courses;
        hoursCount.textContent = hours;
        progressPercent.textContent = `${progress}%`;

        // Обновляем активность
        const hoursActivity = Math.floor(activity / 60);
        const minutesActivity = activity % 60;

        if (activity > 0) {
            if (hoursActivity > 0) {
                todayActivity.textContent = `${hoursActivity} час ${minutesActivity} минут обучения`;
            } else {
                todayActivity.textContent = `${minutesActivity} минут обучения`;
            }

            // Рассчитываем прогресс-бар (максимум 8 часов = 480 минут)
            const activityPercent = Math.min((activity / 480) * 100, 100);
            activityBar.style.width = `${activityPercent}%`;
        } else {
            todayActivity.textContent = 'Активность не указана';
            activityBar.style.width = '0%';
        }

        // Анимация обновления
        [coursesCount, hoursCount, progressPercent].forEach(el => {
            el.classList.add('updating');
            setTimeout(() => el.classList.remove('updating'), 500);
        });
    }

    // Слушатели событий для имени и фамилии
    firstNameInput.addEventListener('input', updateUserName);
    lastNameInput.addEventListener('input', updateUserName);

    // Слушатели для статуса
    userClassSelect.addEventListener('change', updateUserStatus);
    aboutUserTextarea.addEventListener('input', updateUserStatus);

    // Слушатели для статистики
    inputCourses.addEventListener('input', updateStats);
    inputHours.addEventListener('input', updateStats);
    inputProgress.addEventListener('input', updateStats);
    inputActivity.addEventListener('input', updateStats);

    // Кнопка сохранения
    saveButton.addEventListener('click', function() {
        updateUserName();
        updateUserStatus();
        updateStats();

        // Показываем сообщение об успешном сохранении
        const alertDiv = document.createElement('div');
        alertDiv.className = 'alert alert-success alert-dismissible fade show mt-3';
        alertDiv.innerHTML = `
            <i class="bi bi-check-circle-fill me-2"></i>
            Данные профиля успешно обновлены!
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;

        document.querySelector('#personal .card-body').appendChild(alertDiv);

        // Автоматически скрываем через 3 секунды
        setTimeout(() => {
            if (alertDiv.parentNode) {
                alertDiv.remove();
            }
        }, 3000);
    });

    // Автоматическое обновление при загрузке
    updateStats();
});

// Управление стрелочками при открытии/закрытии
document.querySelectorAll('.task-card-header').forEach(header => {
    header.addEventListener('click', function() {
        const arrow = this.querySelector('.arrow-icon');
        arrow.classList.toggle('rotated');
    });
});

// Автоматически открываем первое задание при загрузке
/*document.addEventListener('DOMContentLoaded', function() {
    // Первое задание уже открыто по умолчанию (класс "show")
    const firstArrow = document.querySelector('#task1-detail').previousElementSibling.querySelector('.arrow-icon');
    firstArrow.classList.add('rotated');

    // Обработка события при закрытии аккордеона через Bootstrap
    document.querySelectorAll('.task-card-body').forEach(collapseElement => {
        collapseElement.addEventListener('hidden.bs.collapse', function() {
            const header = this.previousElementSibling;
            const arrow = header.querySelector('.arrow-icon');
            arrow.classList.remove('rotated');
        });

        collapseElement.addEventListener('shown.bs.collapse', function() {
            const header = this.previousElementSibling;
            const arrow = header.querySelector('.arrow-icon');
            arrow.classList.add('rotated');
        });
    });
});

// Плавная прокрутка к якорям
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        if (this.getAttribute('href').startsWith('#') && this.getAttribute('href') != '#') {
            e.preventDefault();

            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);

            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 100,
                    behavior: 'smooth'
                });
            }
        }
    });
});

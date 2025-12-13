
document.querySelectorAll('.subject-card').forEach(card => {
    card.addEventListener('click', function(e) {
        if (!e.target.closest('button')) {
            const subject = this.querySelector('.fw-bold').textContent;
            alert(`Вы выбрали предмет: ${subject}\nНачинаем подготовку...`);
        }
    });
});

document.addEventListener("DOMContentLoaded", function() {
    var readMoreLinks = document.querySelectorAll('.read-more');
    readMoreLinks.forEach(function(link) {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            var descriptionContainer = this.parentNode;
            var shortText = descriptionContainer.querySelector('.short-text');
            var fullText = descriptionContainer.querySelector('.full-text');

            // Переключение класса 'expanded' на descriptionContainer
            descriptionContainer.classList.toggle('expanded');

            // Переключение свойства отображения shortText и fullText
            shortText.style.display = shortText.style.display === 'none' ? 'block' : 'none';
            fullText.style.display = fullText.style.display === 'none' ? 'block' : 'none';
        });
    });
});
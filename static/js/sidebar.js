document.addEventListener('DOMContentLoaded', function () {
    const btn = document.getElementById('sidebar-toggle');
    const sidebar = document.querySelector('.sidebar');

    btn.addEventListener('click', function () {
        sidebar.classList.toggle('closed');
    });
});

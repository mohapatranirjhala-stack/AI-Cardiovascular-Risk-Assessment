document.addEventListener("DOMContentLoaded", function () {

    const toggleButton = document.getElementById("darkModeToggle");

    if (!toggleButton) {
        return;
    }

    const savedTheme = localStorage.getItem("theme");

    if (savedTheme === "dark") {
        document.body.classList.add("dark-mode");
        toggleButton.textContent = "☀️ Light Mode";
    }

    toggleButton.addEventListener("click", function () {

        document.body.classList.toggle("dark-mode");

        if (document.body.classList.contains("dark-mode")) {

            localStorage.setItem("theme", "dark");

            toggleButton.textContent = "☀️ Light Mode";

        } else {

            localStorage.setItem("theme", "light");

            toggleButton.textContent = "🌙 Dark Mode";
        }

    });

});
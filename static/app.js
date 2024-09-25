// Funcionalidad de traducción
document.getElementById("translateButton").addEventListener("click", function() {
    const inputText = document.getElementById("inputText").value;
    const targetLanguage = document.getElementById("targetLanguage").value;

    fetch('http://127.0.0.1:5000/translate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            text: inputText,
            target_language: targetLanguage
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.translated_text) {
            document.getElementById("outputText").textContent = `Traducción: ${data.translated_text}`;
        } else {
            document.getElementById("outputText").textContent = `Error: ${data.error}`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

// Funcionalidad para alternar entre temas
document.getElementById("toggle-theme").addEventListener("click", function() {
    const body = document.body;
    const toggleButton = document.getElementById("toggle-theme");

    // Alternar entre modo oscuro y claro
    body.classList.toggle("light-mode");

    // Cambiar el texto del botón según el tema actual
    if (body.classList.contains("light-mode")) {
        toggleButton.textContent = "Cambiar a modo oscuro";
    } else {
        toggleButton.textContent = "Cambiar a modo claro";
    }
});

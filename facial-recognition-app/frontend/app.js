const form = document.getElementById('upload-form');
const resultDiv = document.getElementById('result');

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData(form);
    const response = await fetch('/predict', {
        method: 'POST',
        body: formData,
    });

    if (response.ok) {
        const result = await response.json();
        displayResult(result);
    } else {
        resultDiv.innerHTML = 'Error: Unable to process the image.';
    }
});

function displayResult(result) {
    resultDiv.innerHTML = `
        <h3>Prediction Result:</h3>
        <p>${result.prediction}</p>
    `;
}
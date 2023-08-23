document.addEventListener("DOMContentLoaded", function () {
    const generateButton = document.getElementById("generate-button");
    const promptInput = document.getElementById("prompt-input");
    const errorDiv = document.getElementById("error");
    const imageContainer = document.getElementById("image-container");

    generateButton.addEventListener("click", async function () {
        try {
            const promptText = promptInput.value;
            
            // Make a request to your API endpoint for generating images
            const response = await fetch(`/generate?prompt=${promptText}`);
            const data = await response.json();

            if (data.error) {
                errorDiv.textContent = "An error occurred";
            } else {
                // Clear error message and display the generated image
                errorDiv.textContent = "";
                imageContainer.innerHTML = `<img src="${data.image_url}" alt="Generated Art">`;
            }
        } catch (error) {
            // Handle error
            errorDiv.textContent = "An error occurred";
            console.error(error);
        }
    });
});

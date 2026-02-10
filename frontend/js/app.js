function formatLabel(label) {
    return label.replace(/___/g, " - ").replace(/_/g, " ");
}

function predictDisease() {
    const input = document.getElementById("imageInput");
    const file = input.files[0];
    const preview = document.getElementById("preview");
    const result = document.getElementById("result");

    if (!file) {
        alert("Please upload an image");
        return;
    }

    preview.src = URL.createObjectURL(file);
    preview.style.display = "block";

    result.style.display = "block";
    result.innerText = "Analyzing leaf image...";

    const formData = new FormData();
    formData.append("file", file);

    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        if (data.error) {
            result.innerText = "❌ " + data.error;
        } else {
            result.innerHTML =
                `<strong>Disease Detected:</strong><br>${formatLabel(data.disease)}`;
        }
    })
    .catch(() => {
        result.innerText = "❌ Server not reachable";
    });
}

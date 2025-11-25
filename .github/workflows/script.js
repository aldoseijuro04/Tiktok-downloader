async function downloadVideo() {
    const url = document.getElementById("urlInput").value.trim();
    const resultDiv = document.getElementById("result");

    if (!url) {
        resultDiv.innerHTML = "<p>Masukkan link TikTok!</p>";
        return;
    }

    resultDiv.innerHTML = "<p>Loading...</p>";

    try {
        // Backend gratis (kamu akan deploy nanti)
        const backendURL = "https://your-backend-url.replit.app/api";

        const response = await fetch(`${backendURL}?url=${encodeURIComponent(url)}`);
        const data = await response.json();

        if (data.status !== "success") {
            resultDiv.innerHTML = "<p>Gagal mengambil data!</p>";
            return;
        }

        resultDiv.innerHTML = `
            <video width="300" controls src="${data.video}"></video>
            <br>
            <a href="${data.video}" download>
                <button>Download Video</button>
            </a>
        `;
    } catch (err) {
        resultDiv.innerHTML = "<p>Error server.</p>";
    }
}

const fields = [
    "Time","V1","V2","V3","V4","V5","V6","V7","V8","V9",
    "V10","V11","V12","V13","V14","V15","V16","V17","V18","V19",
    "V20","V21","V22","V23","V24","V25","V26","V27","V28","Amount"
];

// Determine API Base URL
const getApiBaseUrl = () => {
    const host = window.location.hostname;
    if (host === "localhost" || host === "127.0.0.1") {
        return "http://localhost:8080";
    }
    // Live deployed Render backend URL
    return window.ENV_API_URL || "https://fraud-detection-blockchain.onrender.com";

};

// Populate input fields
let html = "";
fields.forEach(f => {
    html += `
        <div class="field">
            <label for="${f}">${f}</label>
            <input type="number" id="${f}" value="0" step="any">
        </div>`;
});
document.getElementById("fields-grid").innerHTML = html;

// Predict button click event listener
document.getElementById("predictBtn").onclick = async () => {
    const resultBox = document.getElementById("result-box");
    const errorBox = document.getElementById("error-box");
    const btn = document.getElementById("predictBtn");

    resultBox.textContent = "Analyzing transaction features...";
    errorBox.textContent = "";
    btn.disabled = true;
    btn.textContent = "Evaluating...";

    let data = {};
    fields.forEach(f => {
        data[f] = Number(document.getElementById(f).value || 0);
    });

    const escapedJson = JSON.stringify(JSON.stringify(data));
    const apiUrl = `${getApiBaseUrl()}/api/ml/predict`;

    try {
        const response = await fetch(apiUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: escapedJson
        });

        const text = await response.text();

        try {
            const json = JSON.parse(text);
            resultBox.textContent = JSON.stringify(json, null, 2);
        } catch {
            errorBox.textContent = text;
            resultBox.textContent = "";
        }

    } catch (err) {
        errorBox.textContent = `API Connection Error: ${err.message}\nMake sure Render backend is running at ${getApiBaseUrl()}`;
        resultBox.textContent = "";
    } finally {
        btn.disabled = false;
        btn.textContent = "Predict Transaction Risk";
    }
};

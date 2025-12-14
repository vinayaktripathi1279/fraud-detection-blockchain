const fields = [
    "Time","V1","V2","V3","V4","V5","V6","V7","V8","V9",
    "V10","V11","V12","V13","V14","V15","V16","V17","V18","V19",
    "V20","V21","V22","V23","V24","V25","V26","V27","V28","Amount"
];

// Build input fields
let html = "";
fields.forEach(f => {
    html += `
        <div class="field">
            <label>${f}</label>
            <input type="number" id="${f}" value="0">
        </div>`;
});
document.getElementById("fields-grid").innerHTML = html;

// Predict button click
document.getElementById("predictBtn").onclick = async () => {

    document.getElementById("result-box").textContent = "";
    document.getElementById("error-box").textContent = "";

    // Build normal JSON object
    let data = {};
    fields.forEach(f => {
        data[f] = Number(document.getElementById(f).value || 0);
    });

    // Convert to escaped JSON string
    const escapedJson = JSON.stringify(JSON.stringify(data));

    try {
        const response = await fetch("/api/ml/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: escapedJson
        });

        const text = await response.text();

        try {
            const json = JSON.parse(text);
            document.getElementById("result-box").textContent =
                JSON.stringify(json, null, 2);
        } catch {
            document.getElementById("error-box").textContent = text;
        }

    } catch (err) {
        document.getElementById("error-box").textContent = err.toString();
    }
};

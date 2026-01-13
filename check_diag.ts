
async function checkDiagnostic() {
    try {
        const res = await fetch('http://localhost:3001/api/smart-money/diagnostic');
        const data = await res.json();
        console.log(JSON.stringify(data, null, 2));
    } catch (e) {
        console.error("Error:", e.message);
    }
}
checkDiagnostic();

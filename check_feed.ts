
async function checkFeed() {
    try {
        const res = await fetch('http://localhost:3001/api/smart-money/feed?universe=all_us&source=confluence&lookbackDays=90');
        const data = await res.json();
        console.log("Root keys:", Object.keys(data));
        if (data.data) console.log("Data keys:", Object.keys(data.data));
        if (data.meta) console.log("Meta keys:", Object.keys(data.meta));
        
        // Check where scoreboard is
        if (data.scoreboard) console.log("Found scoreboard in Root");
        if (data.meta && data.meta.scoreboard) console.log("Found scoreboard in Meta");
        if (data.data && data.data.scoreboard) console.log("Found scoreboard in Data");

        // Inspect upgrades
        const scoreboard = data.scoreboard || (data.meta && data.meta.scoreboard);
        if (scoreboard) {
            console.log("Upgrades:", JSON.stringify(scoreboard.upgrades, null, 2));
        } else {
            console.log("Scoreboard object is missing!");
        }
    } catch (e) {
        console.error("Error:", e.message);
    }
}
checkFeed();

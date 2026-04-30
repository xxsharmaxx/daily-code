const file = {
    expiryTime: Date.now() + 5000 // 5 seconds
};

function checkExpiry() {
    if (Date.now() > file.expiryTime) {
        console.log("❌ Link expired");
    } else {
        console.log("✅ Link still valid");
    }
}

setTimeout(checkExpiry, 6000);

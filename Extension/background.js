let port = browser.runtime.connectNative("open_link_in_chrome_host");

port.onMessage.addListener((response) => {
    console.log("Received: " + response);
});


browser.contextMenus.create({
    id: "open-link-in-chrome",
    title: "Open link in Chrome",
    contexts: ["link"]
},
    () => void browser.runtime.lastError,
);

browser.contextMenus.onClicked.addListener((info, tab) => {
    if (info.menuItemId === "open-link-in-chrome") {
        // Always HTML-escape external input to avoid XSS.
        const safeUrl = escapeHTML(info.linkUrl);
        if (safeUrl)
            port.postMessage(safeUrl);
    }
});


// https://gist.github.com/Rob--W/ec23b9d6db9e56b7e4563f1544e0d546
function escapeHTML(str) {
    // Note: string cast using String; may throw if `str` is non-serializable, e.g. a Symbol.
    // Most often this is not the case though.
    return String(str)
        .replace(/&/g, "&amp;")
        .replace(/"/g, "&quot;").replace(/'/g, "&#39;")
        .replace(/</g, "&lt;").replace(/>/g, "&gt;");
}


var callback = function (results) {
    // ToDo: Do something with the image urls (found in results[0])

    document.body.innerHTML = '';
    for (var i in results[0]) {
        var img = document.createElement('img');
        img.src = results[0][i];

        document.body.appendChild(img);
    }
};

chrome.tabs.query({ // Get active tab
    active: true,
    currentWindow: true
}, function (tabs) {
    chrome.tabs.executeScript(tabs[0].id, {
        code: 'Array.prototype.map.call(document.images, function (i) { return i.src; });'
    }, callback);
});

//document.addEventListener('DOMContentLoaded' , function () {
    
//}
chrome.tabs.executeScript( {
  code: "window.getSelection().toString();"
}, function(selection) {
  document.body.innerHTML = selection[0];
});



//var callback = function (results) {
//    // ToDo: Do something with the image urls (found in results[0])
//    
//    if (!(results.length > 0)){
//        document.body.innerHTML = 'HERE ARE THE LINKS\n';
//        for (var i in results[0]) {
//            var div = document.createElement('div');
//            var a = document.createElement('a');
//            var linkText = document.createTextNode(results[0][i]);
//            a.appendChild(linkText);
//            a.title = "Link" + i;
//            a.href = results[0][i];
//            div.appendChild(a);
//            document.body.appendChild(div);
//        }
//    }
//};
//
//
//chrome.tabs.query({ // Get active tab
//    active: true,
//    currentWindow: true
//}, function (tabs) {
//    chrome.tabs.executeScript(tabs[0].id, {
//        code: 'Array.prototype.map.call(document.images, function (i) { return i.src; });'
//    }, callback);
//});



chrome.tabs.executeScript( {
  code: "window.getSelection().toString();"
}, function(selection) {
     document.body.innerHTML = selection[0];
     var data = selection[0];  
     chrome.runtime.sendMessage({ message: 'POST', data });
});

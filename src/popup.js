chrome.tabs.executeScript( {
  code: "window.getSelection().toString();"
}, function(selection) {
     document.body.innerHTML += selection[0];
     document.body.innerHTML += "<br></br><div>ClickBait: 89.040%</div><div>News: 10.960%</div>";
    
     var data = selection[0];  
     chrome.runtime.sendMessage({ message: 'POST', data });
});

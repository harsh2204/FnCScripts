function jsoniFy(arr) {
  var a = document.body.appendChild(
    document.createElement("a")
  );
  a.download = "links.txt";
  a.href = "data:text/plain;base64," + btoa(JSON.stringify(arr));
  a.innerHTML = "download link";
  a.click();
}

function grabLinks() {
  var links = $('a').map(function(i, el) {
    return window.location + $(el).attr('href');
  });
  links.splice(0, 1); //Trim the array here to get rid of any unwanted links.
  var content = "";
  for (var i = 0; i < links.length; i++) {
    content += links[i] + "\n";
  }
}

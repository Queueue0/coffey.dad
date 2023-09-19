update_preview = () => {
  bodyBox = document.getElementById("bodybox");
  previewBox = document.getElementById("preview");
  converter = new showdown.Converter();

  previewBox.innerHTML = converter.makeHtml(bodyBox.value);
}

document.addEventListener("DOMContentLoaded", update_preview);

function handlePopupResult(result) {
    alert("result of popup is: " + result);
}
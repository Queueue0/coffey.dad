update_preview = () => {
  bodyBox = document.getElementById("bodybox");
  previewBox = document.getElementById("preview");
  converter = new showdown.Converter();

  previewBox.innerHTML = converter.makeHtml(bodyBox.value);
}

update_preview();

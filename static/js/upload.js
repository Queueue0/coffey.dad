document.addEventListener("DOMContentLoaded", () => {
  const fileInputs = document.querySelectorAll('input[type=file]');
  fileInputs.forEach((fileInput) => {
    fileInput.onchange = () => {
      if (fileInput.files.length > 0) {
        const fileName = document.getElementById(fileInput.name + '_name');
        fileName.textContent = fileInput.files[0].name;
      }
    }
  });
});


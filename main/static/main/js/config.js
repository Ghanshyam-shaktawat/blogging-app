//Tinymce text editor controls
tinymce.init({
    selector: ".tinymce",
    plugins: `code wordcount table autosave anchor image link lists media searchreplace visualblocks template`,

    toolbar: `undo redo | styles | bold italic underline strikethrough | align | table link image | bullist numlist outdent indent code`,
    a11ychecker_level: 'aaa',
    style_formats: [
        { title: 'Heading 1', block: 'h1' },
        { title: 'Heading 2', block: 'h2' },
        { title: 'Heading 3', block: 'h3' },
        { title: 'Heading 4', block: 'h4' },
        { title: 'Heading 5', block: 'h5' },
        { title: 'Paragraph', block: 'p' },
        { title: 'Blockquote', block: 'blockquote' },
    ],
    object_resizing: false,
    valid_classes: {
        'img': 'medium',
        'div': 'related-content'
    },
    image_caption: true,

    noneditable_class: 'related-content',

    content_style: `
          img {
            min-height: auto;
            height: 100%;
            margin: auto;
            padding: 40px;
            display: block;
          }

          img.medium {
            max-width: 25%;
          }
        `
});

//change the space with dash in url field in new post url field!
document.querySelector('#id_slug').addEventListener('keyup',({ target }) => target.value = target.value.replace(' ','-'));

//Shows the image preview when uploaded!
const fileSelect = document.getElementById("fileSelect"),
  id_image = document.getElementById("id_image"),
  fileList = document.getElementById("fileList");

fileSelect.addEventListener("click", function (e) {
  if (id_image) {
    id_image.click();
  }
  e.preventDefault(); // prevent navigation to "#"
}, false);

id_image.addEventListener("change", handleFiles, false);

function handleFiles() {
  if (!this.files.length) {
    fileList.innerHTML = "<p>No files selected!</p>";
  } else {
    fileList.innerHTML = "";
    for (let i = 0; i < this.files.length; i++) {
      const img = document.createElement("img");
      img.src = URL.createObjectURL(this.files[i]);
      img.height = 60;
      img.onload = function () {
        URL.revokeObjectURL(this.src);
      }
      fileList.appendChild(img);
      info = `${this.files[i].name}`;
      document.getElementById("img-info").innerHTML = info.substring(0, 5)
    }
  }
}

// When the user clicks on the button, 
//         toggle between hiding and showing the dropdown content
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function (e) {
  if (!e.target.matches('.dropbtn')) {
    var myDropdown = document.getElementById("myDropdown");
    if (myDropdown.classList.contains('show')) {
      myDropdown.classList.remove('show');
    }
  }
}

//Opens and close search overlay
function openSearch() {
  document.getElementById("myOverlay").style.display = "block";
  document.getElementById("mySearch").focus();
}

function closeSearch() {
  document.getElementById("myOverlay").style.display = "none";
}
function complete_next()
{
    document.getElementById('interest-first').style.display='none';
    document.getElementById('next-btn').style.display='none';
    document.getElementById('back-btn').style.display='block';
    document.getElementById('interest-complete').style.display='block';
}
function complete_back()
{
    document.getElementById('interest-first').style.display='block';
    document.getElementById('next-btn').style.display='block';
    document.getElementById('back-btn').style.display='none';
    document.getElementById('interest-complete').style.display='none';
}

var picupload = document.getElementById("picupload");
picupload.onchange = function () {
    if (typeof (FileReader) != "undefined") {
        var preview_img = document.getElementById("bg-ppp");
        preview_img.innerHTML = "";
        var regex = /^([a-zA-Z0-9\s_\\.\-:])+(.jpg|.jpeg|.png)$/;
        for (var i = 0; i < picupload.files.length; i++) {
            var file = picupload.files[i];
            console.log(file)
            if (regex.test(file.name.toLowerCase())) {
                var reader = new FileReader();
                reader.onload = function (e) {
                    var img = document.createElement("IMG");
                    img.height = "300";
                    img.width = "240";
                    img.src = e.target.result;
                    preview_img.appendChild(img);
                   
                }
                reader.readAsDataURL(file);
            } else {
                alert(file.name + " is not a valid image file.");
                preview_img.innerHTML = "";
                return false;
            }
        }
    } else {
        alert("This browser does not support HTML5 FileReader.");
    }
};

function show_p_editor()
{
    document.getElementById('p_update_modal').style.display='block';
    document.getElementById('profile-title').style.display='block';
    document.getElementById('profile-back').style.display='none';
    document.getElementById('profile-info').style.display='block';
    document.getElementById('interest-info').style.display='none';
}
function chg_interest()
{
    document.getElementById('profile-title').style.display='none';
    document.getElementById('profile-info').style.display='none';
    document.getElementById('interest-info').style.display='block';
    document.getElementById('profile-back').style.display='block';
}
function show_picture()
{
    document.getElementById('mypic').style.display='block';
}

var picupload = document.getElementById("picupload");
picupload.onchange = function () {
    if (typeof (FileReader) != "undefined") {
        var preview_img = document.getElementById("pp-preview");
        preview_img.innerHTML = "";
        var regex = /^([a-zA-Z0-9\s_\\.\-:])+(.jpg|.jpeg|.png)$/;
        for (var i = 0; i < picupload.files.length; i++) {
            var file = picupload.files[i];
            if (regex.test(file.name.toLowerCase())) {
                var reader = new FileReader();
                reader.onload = function (e) {
                    var img = document.createElement("IMG");
                    img.height = "240";
                    img.width = "220";
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

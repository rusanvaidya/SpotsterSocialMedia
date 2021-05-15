function complete_next1()
{
    document.getElementById('cc1').style.display='none';
    document.getElementById('next-btn').style.display='none';
    document.getElementById('back-btn').style.display='block';
    document.getElementById('next-btn2').style.display='block';
    document.getElementById('cc2').style.display='block';
    document.getElementById('im1').style.display='none';
    document.getElementById('im2').style.display='block';
}
function complete_back()
{
    document.getElementById('cc1').style.display='block';
    document.getElementById('next-btn').style.display='block';
    document.getElementById('back-btn').style.display='none';
    document.getElementById('next-btn2').style.display='none';
    document.getElementById('cc2').style.display='none';
    document.getElementById('im2').style.display='none';
    document.getElementById('im1').style.display='block';
}
function complete_next2()
{
    document.getElementById('cc2').style.display='none';
    document.getElementById('next-btn2').style.display='none';
    document.getElementById('back-btn').style.display='none';
    document.getElementById('back-btn2').style.display='block';
    document.getElementById('submit-complete').style.display='block';
    document.getElementById('cc3').style.display='block';
    document.getElementById('im2').style.display='none';
    document.getElementById('im3').style.display='block';
}
function complete_back2()
{
    document.getElementById('cc2').style.display='block';
    document.getElementById('next-btn2').style.display='block';
    document.getElementById('back-btn').style.display='block';
    document.getElementById('submit-complete').style.display='none';
    document.getElementById('cc3').style.display='none';
    document.getElementById('im3').style.display='none';
    document.getElementById('back-btn2').style.display='none';
    document.getElementById('im2').style.display='block';
}

var picupload = document.getElementById("picupload");
picupload.onchange = function () {
    if (typeof (FileReader) != "undefined") {
        var regex = /^([a-zA-Z0-9\s_\\.\-:])+(.jpg|.jpeg|.png)$/;
        for (var i = 0; i < picupload.files.length; i++) {
            var file = picupload.files[i];
            console.log(file)
            if (regex.test(file.name.toLowerCase())) {
                var reader = new FileReader();
                reader.onload = function (e) {
                    var img = document.getElementById("defpp");
                    img.height = "300";
                    img.width = "240";
                    img.src = e.target.result;
                }
                reader.readAsDataURL(file);
            } else {
                alert(file.name + " is not a valid image file.");
                return false;
            }
        }
    } else {
        alert("This browser does not support HTML5 FileReader.");
    }
};

// theme
var theme = localStorage.getItem('theme');
if(theme=='dark')
{
    document.getElementById('cm').style.background='rgb(60, 60, 60)';
    document.getElementById('cf').style.color='white';
    document.getElementById('copyright').style.color='white';
    localStorage.setItem('theme','dark');
}
else if (theme == 'light')
{
    document.getElementById('cm').style.background='rgb(209, 209, 209)';
    document.getElementById('cf').style.color='black';
    document.getElementById('copyright').style.color='black';
    localStorage.setItem('theme','light');
}
else
{
    document.getElementById('cm').style.background='rgb(60, 60, 60)';
    document.getElementById('cf').style.color='white';
    document.getElementById('copyright').style.color='white';
    localStorage.setItem('theme','dark');
}

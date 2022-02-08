var posts_show_btn2 = document.getElementById('posts_show_top');
posts_show_btn2.onclick = function()
{
    posts_show.style.display = 'block';
    if(posts_show_btn.classList == 'inactive')
    {
        posts_show_btn.classList.remove('inactive');
        posts_show_btn.classList.toggle('active');
    }
    settings_show.style.display = 'none';
    if(settings_show_btn.classList=='active')
    {
        settings_show_btn.classList.toggle('inactive');
        settings_show_btn.classList.remove('active');
    }
    my_interests_show.style.display = 'none';
    if(my_interests_show_btn.classList=='active')
    {
        my_interests_show_btn.classList.remove('active');
        my_interests_show_btn.classList.toggle('inactive');
    }
}

var posts_show_btn = document.getElementById('posts-btn');
var settings_show_btn = document.getElementById('settings-btn');
var my_interests_show_btn = document.getElementById('interests-btn');
var posts_show = document.getElementById('my-posted-contents');
var settings_show = document.getElementById('my-settings');
var my_interests_show = document.getElementById('my-interests');

posts_show_btn.onclick = function()
{
    posts_show.style.display = 'block';
    if(posts_show_btn.classList == 'inactive')
    {
        posts_show_btn.classList.remove('inactive');
        posts_show_btn.classList.toggle('active');
    }
    settings_show.style.display = 'none';
    if(settings_show_btn.classList=='active')
    {
        settings_show_btn.classList.toggle('inactive');
        settings_show_btn.classList.remove('active');
    }
    my_interests_show.style.display = 'none';
    if(my_interests_show_btn.classList=='active')
    {
        my_interests_show_btn.classList.remove('active');
        my_interests_show_btn.classList.toggle('inactive');
    }
}
settings_show_btn.onclick = function()
{
    posts_show.style.display = 'none';
    if(posts_show_btn.classList == 'active')
    {
        posts_show_btn.classList.remove('active');
        posts_show_btn.classList.toggle('inactive');
    }
    settings_show.style.display = 'block';
    if(settings_show_btn.classList=='inactive')
    {
        settings_show_btn.classList.toggle('active');
        settings_show_btn.classList.remove('inactive');
    }
    my_interests_show.style.display = 'none';
    if(my_interests_show_btn.classList=='active')
    {
        my_interests_show_btn.classList.remove('active');
        my_interests_show_btn.classList.toggle('inactive');
    }
}
my_interests_show_btn.onclick = function()
{
    posts_show.style.display = 'none';
    if(posts_show_btn.classList == 'active')
    {
        posts_show_btn.classList.remove('active');
        posts_show_btn.classList.toggle('inactive');
    }
    settings_show.style.display = 'none';
    if(settings_show_btn.classList=='active')
    {
        settings_show_btn.classList.toggle('inactive');
        settings_show_btn.classList.remove('active');
    }
    my_interests_show.style.display = 'block';
    if(my_interests_show_btn.classList=='inactive')
    {
        my_interests_show_btn.classList.remove('inactive');
        my_interests_show_btn.classList.toggle('active');
    }
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



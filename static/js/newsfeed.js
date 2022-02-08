function post_area()
{
    document.getElementById('modal-title').style.display='block'; 
    document.getElementById('title-back').style.display='none'; 
    document.getElementById('new_post_modal').style.display='block'; 
    document.getElementById('post-create').style.display='block';
    document.getElementById('venue-create').style.display='none';
    document.getElementById('feeling-create').style.display='none';
}

function post_venue()
{
    document.getElementById('modal-title').style.display='none'; 
    document.getElementById('title-back').style.display='block'; 
    document.getElementById('new_post_modal').style.display='block'; 
    document.getElementById('post-create').style.display='none';
    document.getElementById('venue-create').style.display='block';
    document.getElementById('feeling-create').style.display='none';
}

function post_feeling()
{
    document.getElementById('modal-title').style.display='none'; 
    document.getElementById('title-back').style.display='block'; 
    document.getElementById('new_post_modal').style.display='block'; 
    document.getElementById('post-create').style.display='none';
    document.getElementById('venue-create').style.display='none';
    document.getElementById('feeling-create').style.display='block';
}
// activity

function a_1()
{
    var label = 'is organizing event';
    var img_tag = 'activity/event.png';
    document.getElementById('modal-title').style.display='block'; 
    document.getElementById('title-back').style.display='none'; 
    document.getElementById('post-create').style.display='block';
    document.getElementById('venue-create').style.display='none';
    document.getElementById('feeling-label').innerHTML=label;
    document.getElementById('f-label').value=label;
    document.getElementById('feeling-emoji').innerHTML = "<img src='../static/"+img_tag+"'>";
    document.getElementById('f-img-tag').value= img_tag;

}

function a_2()
{
    var label ='is attending event';
    var img_tag ='activity/calender.png';
    document.getElementById('modal-title').style.display='block'; 
    document.getElementById('title-back').style.display='none'; 
    document.getElementById('post-create').style.display='block';
    document.getElementById('venue-create').style.display='none';
    document.getElementById('feeling-label').innerHTML= label;
    document.getElementById('f-label').value= label;
    document.getElementById('feeling-emoji').innerHTML = "<img src='../static/"+img_tag+"'>";
    document.getElementById('f-img-tag').value= img_tag;
}
function a_3()
{
    var label ='is celebrating birthday';
    var img_tag ='activity/birthday.png';
    document.getElementById('modal-title').style.display='block'; 
    document.getElementById('title-back').style.display='none'; 
    document.getElementById('post-create').style.display='block';
    document.getElementById('venue-create').style.display='none';
    document.getElementById('feeling-label').innerHTML= label;
    document.getElementById('f-label').value= label;
    document.getElementById('feeling-emoji').innerHTML = "<img src='../static/"+img_tag+"'>";
    document.getElementById('f-img-tag').value= img_tag;
}
function a_4()
{
    var label ='is celebrating occasion';
    var img_tag ='activity/celebrating.png';
    document.getElementById('modal-title').style.display='block'; 
    document.getElementById('title-back').style.display='none'; 
    document.getElementById('post-create').style.display='block';
    document.getElementById('venue-create').style.display='none';
    document.getElementById('feeling-label').innerHTML= label;
    document.getElementById('f-label').value= label;
    document.getElementById('feeling-emoji').innerHTML = "<img src='../static/"+img_tag+"'>";
    document.getElementById('f-img-tag').value= img_tag;
}
function a_5()
{
    var label ='is celebrating festival';
    var img_tag ='activity/festival.png';
    document.getElementById('modal-title').style.display='block'; 
    document.getElementById('title-back').style.display='none'; 
    document.getElementById('post-create').style.display='block';
    document.getElementById('venue-create').style.display='none';
    document.getElementById('feeling-label').innerHTML= label;
    document.getElementById('f-label').value= label;
    document.getElementById('feeling-emoji').innerHTML = "<img src='../static/"+img_tag+"'>";
    document.getElementById('f-img-tag').value= img_tag;
}
function a_6()
{
    var label ='is watching movie';
    var img_tag ='activity/movie.png';
    document.getElementById('modal-title').style.display='block'; 
    document.getElementById('title-back').style.display='none'; 
    document.getElementById('post-create').style.display='block';
    document.getElementById('venue-create').style.display='none';
    document.getElementById('feeling-label').innerHTML= label;
    document.getElementById('f-label').value= label;
    document.getElementById('feeling-emoji').innerHTML = "<img src='../static/"+img_tag+"'>";
    document.getElementById('f-img-tag').value= img_tag;
}
function a_7()
{
    var label ='is travelling';
    var img_tag ='activity/travelling.png';
    document.getElementById('modal-title').style.display='block'; 
    document.getElementById('title-back').style.display='none'; 
    document.getElementById('post-create').style.display='block';
    document.getElementById('venue-create').style.display='none';
    document.getElementById('feeling-label').innerHTML= label;
    document.getElementById('f-label').value= label;
    document.getElementById('feeling-emoji').innerHTML = "<img src='../static/"+img_tag+"'>";
    document.getElementById('f-img-tag').value= img_tag;
}

// feeling
function feeling_h()
{
    var label ='is feeling happy';
    var img_tag ='emoji/043-happy.png';
    document.getElementById('modal-title').style.display='block'; 
    document.getElementById('title-back').style.display='none'; 
    document.getElementById('post-create').style.display='block';
    document.getElementById('feeling-create').style.display='none';
    document.getElementById('feeling-label').innerHTML= label;
    document.getElementById('f-label').value= label;
    document.getElementById('feeling-emoji').innerHTML = "<img src='../static/"+img_tag+"'>";
    document.getElementById('f-img-tag').value= img_tag;
}

function feeling_s()
{
    var label ='is feeling sad';
    var img_tag ='emoji/011-bored.png';
    document.getElementById('modal-title').style.display='block'; 
    document.getElementById('title-back').style.display='none'; 
    document.getElementById('post-create').style.display='block';
    document.getElementById('feeling-create').style.display='none';
    document.getElementById('feeling-label').innerHTML= label;
    document.getElementById('f-label').value= label;
    document.getElementById('feeling-emoji').innerHTML = "<img src='../static/"+img_tag+"'>";
    document.getElementById('f-img-tag').value= img_tag;
}
function feeling_e()
{
    var label ='is feeling excited';
    var img_tag ='emoji/047-shining.png';
    document.getElementById('modal-title').style.display='block'; 
    document.getElementById('title-back').style.display='none'; 
    document.getElementById('post-create').style.display='block';
    document.getElementById('feeling-create').style.display='none';
    document.getElementById('feeling-label').innerHTML= label;
    document.getElementById('f-label').value= label;
    document.getElementById('feeling-emoji').innerHTML = "<img src='../static/"+img_tag+"'>";
    document.getElementById('f-img-tag').value= img_tag;
}
function feeling_sick()
{
    var label ='is feeling sick';
    var img_tag ='emoji/034-sick.png';
    document.getElementById('modal-title').style.display='block'; 
    document.getElementById('title-back').style.display='none'; 
    document.getElementById('post-create').style.display='block';
    document.getElementById('feeling-create').style.display='none';
    document.getElementById('feeling-label').innerHTML= label;
    document.getElementById('f-label').value= label;
    document.getElementById('feeling-emoji').innerHTML = "<img src='../static/"+img_tag+"'>";
    document.getElementById('f-img-tag').value= img_tag;
}
function feeling_w()
{
    var label ='is feeling wonderful';
    var img_tag ='emoji/031-saint.png';
    document.getElementById('modal-title').style.display='block'; 
    document.getElementById('title-back').style.display='none'; 
    document.getElementById('post-create').style.display='block';
    document.getElementById('feeling-create').style.display='none';
    document.getElementById('feeling-label').innerHTML= label;
    document.getElementById('f-label').value= label;
    document.getElementById('feeling-emoji').innerHTML = "<img src='../static/"+img_tag+"'>";
    document.getElementById('f-img-tag').value= img_tag;
}
function feeling_crazy()
{
    var label ='is feeling crazy';
    var img_tag ='emoji/046-crazy.png';
    document.getElementById('modal-title').style.display='block'; 
    document.getElementById('title-back').style.display='none'; 
    document.getElementById('post-create').style.display='block';
    document.getElementById('feeling-create').style.display='none';
    document.getElementById('feeling-label').innerHTML= label;
    document.getElementById('f-label').value= label;
    document.getElementById('feeling-emoji').innerHTML = "<img src='../static/"+img_tag+"'>";
    document.getElementById('f-img-tag').value= img_tag;
}
function feeling_a()
{
    var label ='is feeling angry';
    var img_tag ='emoji/037-angry.png';
    document.getElementById('modal-title').style.display='block'; 
    document.getElementById('title-back').style.display='none'; 
    document.getElementById('post-create').style.display='block';
    document.getElementById('feeling-create').style.display='none';
    document.getElementById('feeling-label').innerHTML= label;
    document.getElementById('f-label').value= label;
    document.getElementById('feeling-emoji').innerHTML = "<img src='../static/"+img_tag+"'>";
    document.getElementById('f-img-tag').value= img_tag;
}
function feeling_t()
{
    var label ='is feeling tired';
    var img_tag ='emoji/003-tired.png';
    document.getElementById('modal-title').style.display='block'; 
    document.getElementById('title-back').style.display='none'; 
    document.getElementById('post-create').style.display='block';
    document.getElementById('feeling-create').style.display='none';
    document.getElementById('feeling-label').innerHTML= label;
    document.getElementById('f-label').value= label;
    document.getElementById('feeling-emoji').innerHTML = "<img src='../static/"+img_tag+"'>";
    document.getElementById('f-img-tag').value= img_tag;
}
function feeling_afraid()
{
    var label ='is feeling afraid';
    var img_tag ='emoji/021-afraid.png';
    document.getElementById('modal-title').style.display='block'; 
    document.getElementById('title-back').style.display='none'; 
    document.getElementById('post-create').style.display='block';
    document.getElementById('feeling-create').style.display='none';
    document.getElementById('feeling-label').innerHTML= label;
    document.getElementById('f-label').value= label;
    document.getElementById('feeling-emoji').innerHTML = "<img src='../static/"+img_tag+"'>";
    document.getElementById('f-img-tag').value= img_tag;
}
function feeling_d()
{
    var label ='is feeling dissapointed';
    var img_tag ='emoji/024-dissapointment.png';
    document.getElementById('modal-title').style.display='block'; 
    document.getElementById('title-back').style.display='none'; 
    document.getElementById('post-create').style.display='block';
    document.getElementById('feeling-create').style.display='none';
    document.getElementById('feeling-label').innerHTML= label;
    document.getElementById('f-label').value= label;
    document.getElementById('feeling-emoji').innerHTML = "<img src='../static/"+img_tag+"'>";
    document.getElementById('f-img-tag').value= img_tag;
}
function feeling_i()
{
    var label ='is feeling insightful';
    var img_tag ='emoji/039-observing.png';
    document.getElementById('modal-title').style.display='block'; 
    document.getElementById('title-back').style.display='none'; 
    document.getElementById('post-create').style.display='block';
    document.getElementById('feeling-create').style.display='none';
    document.getElementById('feeling-label').innerHTML= label;
    document.getElementById('f-label').value= label;
    document.getElementById('feeling-emoji').innerHTML = "<img src='../static/"+img_tag+"'>";
    document.getElementById('f-img-tag').value= img_tag;
}
function feeling_c()
{
    var label ='is feeling confused';
    var img_tag ='emoji/018-confused.png';
    document.getElementById('modal-title').style.display='block'; 
    document.getElementById('title-back').style.display='none'; 
    document.getElementById('post-create').style.display='block';
    document.getElementById('feeling-create').style.display='none';
    document.getElementById('feeling-label').innerHTML= label;
    document.getElementById('f-label').value= label;
    document.getElementById('feeling-emoji').innerHTML = "<img src='../static/"+img_tag+"'>";
    document.getElementById('f-img-tag').value= img_tag;
}
function feeling_surprised()
{
    var label ='is feeling surprised';
    var img_tag ='emoji/010-surprised.png';
    document.getElementById('modal-title').style.display='block'; 
    document.getElementById('title-back').style.display='none'; 
    document.getElementById('post-create').style.display='block';
    document.getElementById('feeling-create').style.display='none';
    document.getElementById('feeling-label').innerHTML= label;
    document.getElementById('f-label').value= label;
    document.getElementById('feeling-emoji').innerHTML = "<img src='../static/"+img_tag+"'>";
    document.getElementById('f-img-tag').value= img_tag;
}
function feeling_n()
{
    var label ='is feeling nerd';
    var img_tag ='emoji/020-nerd.png';
    document.getElementById('modal-title').style.display='block'; 
    document.getElementById('title-back').style.display='none'; 
    document.getElementById('post-create').style.display='block';
    document.getElementById('feeling-create').style.display='none';
    document.getElementById('feeling-label').innerHTML= label;
    document.getElementById('f-label').value= label;
    document.getElementById('feeling-emoji').innerHTML = "<img src='../static/"+img_tag+"'>";
    document.getElementById('f-img-tag').value= img_tag;
}

var fileUpload = document.getElementById("fileupload");
fileUpload.onchange = function () {
    if (typeof (FileReader) != "undefined") {
        var preview_img = document.getElementById("preview-img");
        preview_img.innerHTML = "";
        var regex = /^([a-zA-Z0-9\s_\\.\-:])+(.jpg|.jpeg|.gif|.png|.bmp|.mp4)$/;
        for (var i = 0; i < fileUpload.files.length; i++) {
            var file = fileUpload.files[i];
            if (regex.test(file.name.toLowerCase())) {
                var reader = new FileReader();
                reader.onload = function (e) {
                    var img = document.createElement("IMG");
                    img.height = "100";
                    img.width = "100";
                    img.src = e.target.result;
                    preview_img.appendChild(img);
                }
                reader.readAsDataURL(file);
            }
            else {
                alert(file.name + " is not a valid image file.");
                preview_img.innerHTML = "";
                return false;
            }
        }
    } else {
        alert("This browser does not support HTML5 FileReader.");
    }
   
};

function myComment()
{
    document.getElementById('i-c').style.display='none';
    document.getElementById('a-c').style.display='inline-block';
    document.getElementById('a-c').style.background='rgb(226, 226, 226)';
    document.getElementById('c-section').style.display='block';
}
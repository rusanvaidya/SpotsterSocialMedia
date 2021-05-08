var des = document.getElementById('show-v-description');
// var d = document.getElementById('d-show').style.display='block';
des.onclick = function()
{
    console.log(document.getElementById('description').classList);
    if(document.getElementById('description').classList=='hide-video')
    {
        document.getElementById('description').classList.toggle('show-video');
        document.getElementById('description').classList.remove('hide-video');
    }
    else if(document.getElementById('description').classList=='show-video')
    {
        document.getElementById('description').classList.remove('show-video');
        document.getElementById('description').classList.toggle('hide-video');
    }
}